# _*_coding:utf-8_*_
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import requests
import json
import time
from bs4 import BeautifulSoup
import cookielib
import threading
from proxy_to_redis import *
from proxy_to_redis import proxy_sendback
from multiprocessing import process
from setting import CONTENT_THREADING_NUM
from setting import COMMENTS_THREADING_NUM
from saveresult import Save_result
import re
import logging
# from visit_page import get_response_and_text
from visit_page2 import get_response_and_text
import datetime
from datetime import timedelta
# from KafkaConnector1 import Producer,Consumer
# from saveresult import get_result_name
from KafkaConnector import RemoteProducer,Consumer
from saveresult import get_result_name




class scjjrb():
    def __init__(self):
        self.session1 = requests.session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()


        self.index_data_list = ['http://www.scjjrb.com/Item/list.asp?id=674&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=690&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=689&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=688&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=684&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=683&page=1',#视频
                                'http://www.scjjrb.com/Item/list.asp?id=682&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=680&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=674&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=675&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=689&page=1',
                                'http://www.scjjrb.com/Item/list.asp?id=1202&page=1',#没抓图片的，就几个新闻
                                ]
        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_data_list = []  # 这个存储的是已经跑完了的内容

    def get_Index(self):
        def get_index_inside(url):
            url_debug=url
            while True:

                # response1=get_response_and_text(url=url_debug)
                # response_in_function=response1['response_in_function']
                # response_in_function_text=response1['response_in_function_text']
                response1 = self.visit_page_in_class_post(url=url_debug)
                response1.encoding='gb2312'
                response_in_function_text = response1.text
                datasoup=BeautifulSoup(response_in_function_text,'lxml')


                content_div_list=datasoup.select('div.newslist')
                try:
                    newslist = content_div_list[0].select('dl.nl_con1')
                except Exception as e:
                    print e
                for i in newslist:
                    title= i.select('h4.nlc_tit a')[0].get('title')  # title
                    href= i.select('h4.nlc_tit a')[0].get('href')  # href
                    publish_time= i.select('p.nlc_time')[0].text.split(u' ')[0]  # publish_time
                    # print i.select('p.nlc_info')[0].text
                    this_index={
                        'title':title,
                        'url':href,
                        'publish_time':publish_time.replace(u'年','-').replace(u'月','-').replace(u'日','')+' 00:00:00',
                        'id':href.split('/')[-1].split('.')[0]
                        # 'url':url_debug
                    }
                    self.content_data_list.append(this_index)

                next_a = datasoup.select('a.next')  # 下一页链接，这里边的链接就是这样
                next_url=next_a[1].get('href')
                if next_url not in ['javascript:;']:
                    url_debug=url.split('?')[0]+next_url
                else:
                    break

        threadlist=[]
        while self.global_status_num_index > 0 or self.index_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
            while self.index_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.index_data_list:
                    data_in_while = self.index_data_list.pop()
                    thread_in_while = threading.Thread(target=get_index_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)

    def visit_page_in_class_post(self,url,data=None):
        session1 = requests.session()
        while True:
            try:
                proxy1 = get_proxy_from_redis()
                session1.proxies = {'http': 'http://' + proxy1}
                response_1 = session1.request(method='get', url=url, headers=self.headers, timeout=10,data=data)
                if response_1.status_code in range(200, 300):
                    break
            except Exception as e:
                print e
        proxy_sendback(proxy1)
        session1.close()
        return response_1


    def get_content(self):
        Re_find_img_url = re.compile(r' src="(.*?)"')
        def get_content_inside(data):
            url_debug=data['url']
            # response1=get_response_and_text(url=url_debug)
            # response_in_function=response1['response_in_function']
            # response_in_function_text=response1['response_in_function_text']
            response1=self.visit_page_in_class_post(url=url_debug)
            response1.encoding = 'gb2312'
            response_in_function_text=response1.text
            datasoup=BeautifulSoup(response_in_function_text,'lxml')

            publish_user= datasoup.select('div.articlecontent .info span')[0].text.split(u'：')[1]  # publish_user
            content_div_raw= datasoup.select('#MyContent')
            content_div=str(content_div_raw)
            content=content_div_raw[0].text.strip()
            img_urls2=Re_find_img_url.findall(content_div)
            img_urls=[]
            for img_url in img_urls2:
                if 'http://www.scjjrb.com' not in img_url:
                    img_url='http://www.scjjrb.com'+img_url
                img_urls.append(img_url)

            data['content']=content
            data['publish_user']=publish_user
            data['img_urls']=img_urls

            self.result_data_list.append(data)

        threadlist = []
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

    def save_result(self):
        def save_result(data):
            # Save_result(plantform='scjj', date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
            #             datatype='news', full_data=data)


            host = '182.150.63.40'
            port = '12308'
            username = 'silence'
            password = 'silence'

            producer = RemoteProducer(host=host, port=port, username=username, password=password)
            result_file = get_result_name(plantform_e='SCjingji', plantform_c='四川经济网',
                                          date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
                                          datatype='forum', full_data=data)

            producer.send(topic='1101_STREAM_SPIDER', value={'data': data}, key=result_file,
                          updatetime=data['spider_time'])

        threadlist = []
        while self.global_status_num_comments > 0 or self.result_data_list:
            while self.result_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.result_data_list:
                    print len(self.result_data_list)
                    data_in_while = self.result_data_list.pop()
                    thread_in_while = threading.Thread(target=save_result, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
                    print len(threadlist)
                    print len(self.result_data_list)

    def run(self):
            thread1 = threading.Thread(target=self.get_Index, args=())
            thread1.start()
            thread2 = threading.Thread(target=self.get_content, args=())
            thread2.start()

            thread4 = threading.Thread(target=self.save_result, args=())
            thread4.start()
            pass

if __name__ == '__main__':
    thisclass=scjjrb()
    thisclass.run()