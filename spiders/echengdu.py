#_*_coding:utf-8_*_

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


import cookielib
import threading
import requests
from proxy_to_redis import *
from multiprocessing import process
from setting import *
from bs4 import BeautifulSoup
import re
from saveresult import Save_result
from saveresult import get_result_name
import json
from saveresult import BASIC_FILE
import datetime
from visit_page3 import get_response_and_text
from KafkaConnector import RemoteProducer,Consumer
import sqlite3
from sava_data_to_MongoDB import save_data_to_mongodb
import Queue
import datetime


class echengde:
    def __init__(self):
        self.headers={
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        self.urls=['http://e.chengdu.cn/html/2017-10/10/node_{}.htm'.format(str(i)) for i in range(2,13)]

        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4
        self.error_num_to_stop=100



        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容

        self.cache_data_list=Queue.Queue()

    def visit_page(self,url,headers=None,charset=None):
        try:
            response=requests.get(url=url,headers=headers,timeout=8)
            if charset:
                response.encoding=charset
            return {'response_in_function':response,'response_in_function_text':response.text}
        except Exception as e:
            print e

    def get_Index(self):
        need_continue=True
        def get_index_inside(url1):
            response1=self.visit_page(url=url1,headers=self.headers,charset='utf-8')
            if not response1['response_in_function']:
                return
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            # datasoup=BeautifulSoup(response_in_function_text,'lxml')#nowPageArticleList

            # print response.text
            datasoup = BeautifulSoup(response_in_function_text, 'lxml')
            url_pre = 'http://e.chengdu.cn/html/'
            datetime1 = datetime.datetime.now().strftime('%Y-%m/%d')
            for i in datasoup.select('#nowPageArticleList li a'):
                self.content_data_list.append(url_pre + datetime1 + '/' + i.get('href'))

        for url in self.urls:
            get_index_inside(url)
        # print self.content_data_list
        # print len(self.content_data_list)

    def get_content(self):
        def get_content_inside(url):
            response1=self.visit_page(url=url,headers=self.headers,charset='utf-8')
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            datasoup=BeautifulSoup(response_in_function_text,'lxml')






if __name__ == '__main__':
    thisclass=echengde()
    thisclass.get_Index()