import requests
from bs4 import BeautifulSoup
import time
import json
from proxy_to_redis import redis1
from proxy_to_redis import *
from multiprocessing import process
from multiprocessing.pool import Pool
from multiprocessing import pool
requests.adapters.DEFAULT_RETRIES = 50
import UserAgent





def run1(j):
    # print 'has crawled -----------------------------------',j
    # print redis1.lindex()
    # for i in range(redis1.llen('urltest')):
    # i+=1

    # url=redis1.lpop('urltest')
    url=redis1.lindex('urltest',j)
    proxy1=get_proxy_from_redis()
    sessionq=requests.session()
    sessionq.proxies={'http': 'http://' + proxy1}
    while True:
        try:
            headers={
                'User-Agent':UserAgent.getUserAgentRandom(),
                'Connection':'close'
            }
            sessionq.headers=headers
            response1=sessionq.request(method='get',url=url,timeout=20)
            sessionq.close()
            print '------------------------', j
            # proxydict={'http':proxy1}
            # response1=requests.get(url=url,proxies=proxydict)
            # print response1.text
            break
        except requests.exceptions.ConnectionError as e:
            print e
            print '----------------has wrong   the headers is          ',sessionq.headers
            time.sleep(1)
            redis1.lpush('proxy_good',proxy1)
        # sessionq.keep_alive=False
    redis1.rpush('urltest',url)


if __name__ == '__main__':
    list1=[i for i in range(300)]
    process1=pool.Pool(processes=20)
    process1.map(run1,list1)
    process1.close()
    process1.join()