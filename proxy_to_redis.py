#_*_coding:utf-8_*_
import requests
import redis
import time
import json
import random
import threading
from multiprocessing import process

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

connectpool = redis.ConnectionPool(host='localhost', port=6379)
redis1 = redis.Redis(connection_pool=connectpool)


# 首先获得一个proxy的代理池，满了之后暂停一段时间，之后再检擦是否是满的，若不是满的，立即补满。此外，另一个线程不断的从这个originalproxy中读取proxy，再ping百度之后筛选出优质的代理，放入一个优质的代理池中，数量是200个
# 没满自动补满。第三个线程维护这个代理池，隔10分钟就扫描一遍。
# 将来若是某个某个网站想用这个代理，根据meta中的plant_form中的字段来生成一个新的proxylist
# proxy_

ratio = 200


def get_Proxy():
    headers = {
        'Accept-Encoding': 'gzip'
    }

    def get_proxy_to_redis():
        session1 = requests.session()
        proxy_url = 'http://svip.kuaidaili.com/api/getproxy/?orderid=953994536123042&num=100&b_pcchrome=1&b_pcie=1&b_pcff=1&protocol=1&method=1&an_an=1&an_ha=1&sp1=1&quality=2&sort=1&format=json&sep=1'
        ################################这个是一般的'
        try:
            webdata = session1.request(method='GET', url=proxy_url, headers=headers,timeout=10)
        except Exception as e:
            print e
            return
        # print webdata
        data_json = json.loads(webdata.text)
        # print data_json
        # print data_json
        for proxyip in data_json['data']['proxy_list']:
            # print proxyip
            redis1.lpush('proxy_original', proxyip)  # 左进右出

    get_proxy_to_redis()
    while True:
        while redis1.llen('proxy_original') < 300:
            time.sleep(random.randint(1, 3))
            get_proxy_to_redis()


def fillte_Proxy():
    url_to_examing = 'https://www.baidu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    }
    while True:
        print 'has get 600 websites proxy_good,now is waiting'
        while redis1.llen('proxy_good') < 600:
            print 'is examing the proxy where fron proxy_original'
            proxy1 = redis1.lpop('proxy_original')
            session1 = requests.session()
            session1.proxies = {
                "http": "http://" + proxy1,
            }
            # time1 = time.time()
            try:
                response1 = session1.request(method='get', url=url_to_examing, headers=headers,timeout=5)
            except Exception as e:
                print e
                break
            session1.close()
            # response1.elapsed
            time.sleep(1)
            if response1.elapsed.microseconds/1000 < 3000:
                redis1.rpush('proxy_good', proxy1)
                print 'has push one,timeused is ',response1.elapsed.microseconds/1000
        time.sleep(2)

def mult_thread_to_fillte_Proxy():
    print '\n'
    threadlist = []
    # while redis1.llen('proxy_good') < 600 or threadlist:
    #     for one in threadlist:
    #         if not one.is_alive():
    #             threadlist.remove(one)
    #     while len(threadlist) < 5 and threadlist:
    # while
    while len(threadlist)<20:
        thread_to_examproxy=threading.Thread(target=fillte_Proxy,args=())
        threadlist.append(thread_to_examproxy)
    for i in threadlist:
        i.start()
    while len(threadlist)>1:
        pass



def examing_Proxy():
    while True:
        if redis1.llen('proxy_good')-ratio>0:
            for i in range(redis1.llen('proxy_good')-ratio):
                proxy = redis1.lpop('proxy_good')
                url_to_examing = 'https://www.baidu.com/'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
                }
                session2 = requests.session()
                session2.proxies = {
                    "http": "http://" + proxy,
                }
                try:
                    response1 = session2.request(method='get', url=url_to_examing, headers=headers)
                except Exception as e:
                    print e
                    continue
                session2.close()
                if response1.elapsed.microseconds/1000 < 3000:
                    # redis1.lpush('proxy_good', proxy)
                    proxy_sendback(proxy)
                    print 'has examing one'
                else:
                    print 'has ignore one,time used ',response1.elapsed.microseconds,' microseconds'
            time.sleep(10)


def get_proxy_from_redis():

    while redis1.llen('proxy_good')<300:
        time.sleep(1)
        print 'proxy is less than 200!!!!!!!!!!!!   is waiting'
    return redis1.lpop('proxy_good')



def proxy_sendback(proxy):
    proxy_at_200 = redis1.lindex('proxy_good', ratio)
    redis1.lset('proxy_good', ratio, proxy)
    redis1.rpush('proxy_good', proxy_at_200)



def runProxy():
    thread1 = threading.Thread(target=get_Proxy, args=())
    thread2 = threading.Thread(target=fillte_Proxy, args=())
    # thread3 = threading.Thread(target=examing_Proxy, args=())

    thread1.start()
    # thread1.setDaemon()
    thread2.start()
    # thread2.setDaemon()
    # thread3.start()
    # thread3.setDaemon()


if __name__ == '__main__':
    process1=process.Process(target=mult_thread_to_fillte_Proxy,args=())
    thread1 = threading.Thread(target=get_Proxy, args=())
    thread2 = threading.Thread(target=fillte_Proxy, args=())
    thread3 = threading.Thread(target=examing_Proxy, args=())

    thread1.start()
    # thread1.setDaemon()
    time.sleep(5)
    # thread2.start()
    # thread2.setDaemon()
    process1.start()
    process1.join()
    thread3.start()
    # thread3.setDaemon()
