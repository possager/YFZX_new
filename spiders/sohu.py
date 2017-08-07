#_*_coding:utf-8_*_
import requests
import json
import time
from bs4 import BeautifulSoup
import cookielib
import threading
from proxy_to_redis import *
from multiprocessing import process
from setting import CONTENT_THREADING_NUM
from setting import COMMENTS_THREADING_NUM
from saveresult import Save_result
import re
import logging


class sohu:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }
        self.urls = [
            'http://v2.sohu.com/public-api/feed?scene=CHANNEL&sceneId=8&page=',#1&size=20
            'https://api.m.sohu.com/autonews/cpool/?n=%E6%96%B0%E9%97%BB&s='#0&c=20&dc=1
        ]
        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容

    def get_Index(self):
        url_to_get_index1=self.urls[0]
        url_to_get_index2=self.urls[1]#带type的
        for i in range(1,900,20):
            response_index_all=self.session1.request(method='get',url=url_to_get_index2+str(i)+'&c=20&dc=1',headers=self.headers)
            datajson=json.loads(response_index_all.text)
            for i in datajson['data']['news']:
                url_index='https://m.sohu.com/'+str(i['type'])+'/'+str(i['id'])
                data_index={
                    'publish_user':i['media'],
                    'title':i['medium_title'],
                    'read_count':int(i['view_count']),
                    'publish_time':i['created_time'].replace('T',' '),
                    'id':i['id'],
                    'url':url_index,
                    'which_website':1#
                         }
                self.content_data_list.append(data_index)
            time.sleep(1)

        # for j in range(900):#一共有两种网页新闻，现在先设计一种
        #     url_index=


        self.global_status_num_index=0

    def get_content(self):

        def get_content_inside(data):
            session1 = requests.session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            # timea = time.time()
            session1.cookies = cookielib.MozillaCookieJar()
            # session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:
                    timea = time.time()
                    session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
                    response_in_function = session1.request(method='get', url=data['url'], headers=headers,
                                                            timeout=5)  # 这里的headers会因为其它的线程使用而有所改变，因为线程安全的原因，这里不好控制，控制的意义不大。
                    break
                except Exception as e:
                    session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
                    timea = time.time()
                    print e
            timeb = time.time()
            response_in_function.encoding = 'utf-8'
            proxy_here = session1.proxies.values()[0].split('//')[1]
            if timeb - timea < 3:
                proxy_sendback(proxy_here)


            img_urls=[]
            content=''
            datasoup=BeautifulSoup(response_in_function.text,'lxml')
            for i in datasoup.select('body > section.article-wrapper > article > p'):
                content+= i.text
            content_data=str(datasoup.select('body > section.article-wrapper > article')[0])
            Re_find_img=re.compile(r'img src=".*?"')
            for img_url in Re_find_img.findall(content_data):
                img_urls.append(img_url)



        threadlist=[]
        while self.global_status_num_index > 0 or self.content_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
            while self.content_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.content_data_list:
                    data_in_while = self.content_data_list.pop()
                    thread_in_while = threading.Thread(target=get_content_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
                    print 'len of threadlist in content---', len(threadlist)
                    print 'len of content_data_list in content is ---', len(self.content_data_list)
                    # time.sleep(1)

        self.global_status_num_content = 0

    def run(self):
        thread1=threading.Thread(target=self.get_Index,args=())
        thread1.start()
        time.sleep(5)
        thread2=threading.Thread(target=self.get_content,args=())
        thread2.start()
        # time.sleep(3)
        # thread3=threading.Thread(target=self.get_comments,args=())
        # thread3.start()
        # thread4=threading.Thread(target=self.save_result,args=())
        # thread4.start()
        pass

if __name__ == '__main__':
    thisclass=sohu()
    thisclass.run()