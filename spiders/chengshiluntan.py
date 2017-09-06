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
# from visit_page import get_response_and_text
import json
from saveresult import BASIC_FILE
import datetime
from KafkaConnector1 import Producer,Consumer
from visit_page2 import get_response_and_text



class chengshiluntan:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'close',
        }

        self.connectpool = redis.ConnectionPool(host='localhost', port=6379)
        self.redis1 = redis.Redis(connection_pool=connectpool)

        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.index_data_list = []
        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_data_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_data_list = []  # 这个存储的是已经跑完了的内容
        self.publish_user_url_need_to_visit = []

    def get_Index(self):
        def get_index_inside():
            for i in range(101,6000000):
                if self.global_status_num_index==0:
                    return #用来判断何时停止
                while True:
                    if len(self.content_data_list)<100:
                        self.content_data_list.append(
                            {
                                'url':'http://www.chengshiluntan.com/'+str(i)+'-1.html'
                            }
                                                      )
                        break
                    else:
                        time.sleep(5)
        get_index_inside()
    def get_content(self):
        def get_content_inside(data):
            url_debug=data['url']
            response1=get_response_and_text(url=url_debug,headers=self.headers)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            datasoup=BeautifulSoup(response_in_function_text,'lxml')

            datasoup.select('')