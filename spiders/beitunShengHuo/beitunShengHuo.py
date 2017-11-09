# _*_coding:utf-8_*_
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import json
import time
import urllib
from bs4 import BeautifulSoup
import cookielib
import threading
from proxy_to_redis import *
from multiprocessing import process
from setting import CONTENT_THREADING_NUM
from setting import COMMENTS_THREADING_NUM
import re
import logging
import datetime
from datetime import timedelta
from KafkaConnector import RemoteProducer,Consumer

from KafkaConnector1 import Producer,Consumer
from saveresult import get_result_name
from saveresult import Save_result
import redis

from sava_data_to_MongoDB import save_data_to_mongodb
from visit_page4 import get_response_and_text
import Queue



from beitunShengHuo_index import get_index
from beitunShengHuo_content import get_content


class beitun:
    def __init__(self):
        self.headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'connection':'close',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        }
        self.urls = [
            'http://www.ibeitun.net/xinxi/s0_a0_m0_p1.html'
        ]
        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.index_data_Queue = Queue.Queue()
        self.content_data_Queue = Queue.Queue()  # 下次需要获得的content链接，不是content内容
        self.comments_data_Queue = Queue.Queue()  # 下次需要获得的comment链接，不是comment内容
        self.result_Queue = Queue.Queue()  # 这个存储的是已经跑完了的内容

        self.cache_data_Queue = Queue.Queue()

    def get_index(self):
        get_index(self.content_data_Queue)


    def get_content(self):
        while True:
            while not self.content_data_Queue.empty():
                one_content_data=self.content_data_Queue.get()
                get_content(data=one_content_data,result_queue=self.result_Queue)
            time.sleep(10)

    def save_result(self):
        def save_result(data):
            result_file = get_result_name(plantform_e='BeiTunShengHuoTong', plantform_c='北屯生活通', date_time=data['publish_time'],
                                          urlOruid=data['url'],
                                          newsidOrtid=data['id'],
                                          datatype='news', full_data=data)
            if not result_file:
                return
            print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'--------',result_file
            data['spider_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            save_data_to_mongodb(data={'data':data},item_id=result_file,platform_e='BeiTunShengHuoTong',platform_c='北屯生活通',cache_data_list=self.cache_data_Queue)


        threadlist = []
        while True:

            while self.global_status_num_content > 0 or not self.result_Queue.empty():
                while not self.result_Queue.empty() or threadlist:
                    for threadi in threadlist:
                        if not threadi.is_alive():
                            threadlist.remove(threadi)
                    while len(threadlist) < CONTENT_THREADING_NUM and not self.result_Queue.empty():
                        data_in_while = self.result_Queue.get()
                        thread_in_while = threading.Thread(target=save_result, args=(data_in_while,))
                        thread_in_while.start()
                        threadlist.append(thread_in_while)
            time.sleep(10)
        # self.global_status_num_comments = 0

    def run(self):
        thread1=threading.Thread(target=self.get_index,args=())
        thread1.start()
        time.sleep(10)
        thread2=threading.Thread(target=self.get_content,args=())
        thread2.start()
        time.sleep(10)
        thread3=threading.Thread(target=self.save_result,args=())
        thread3.start()


if __name__ == '__main__':
    beitunclass=beitun()
    beitunclass.run()