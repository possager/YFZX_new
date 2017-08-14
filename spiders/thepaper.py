# _*_coding:utf-8_*_
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
from visit_page import get_response_and_text

class thepaper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        }
        self.urls = [
            'http://m.thepaper.cn/channel_25950',#时事
            'http://m.thepaper.cn/channel_26916',#视频
            'http://m.thepaper.cn/channel_25951',#财经
            'http://m.thepaper.cn/channel_25952',#思想
            'http://m.thepaper.cn/channel_25953',#生活
            # 'http://m.thepaper.cn/ask_index.jsp',#问吧
            # 'http://m.thepaper.cn/gov_publish.jsp'#问政

        ]
        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.index_url_list=[]
        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容

    def get_Index(self):
        thisurls_list=[]
        for url in self.urls:
            response1=get_response_and_text(url=url)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            Re_pattern = re.compile(r'data.*?\:.*?\".*?Math\.random\b')
            datare = Re_pattern.findall(response_in_function_text)

            url_in_content = datare[0].split('"')[1]
            nexturl = 'http://m.thepaper.cn/load_channel.jsp?' + url_in_content#发现手机端的数据获得地更多一些
            # nexturl='http://www.thepaper.cn/load_index.jsp?nodeids='+url_in_content
            # 'http://www.thepaper.cn/load_index.jsp?nodeids='桌面版的

            thisurls_list.append(nexturl)
        for url_to_visit in thisurls_list:
            for i in range(50):
                # self.index_url_list.append(url_to_visit+str(i))
                pass

        # threadlist=[]
        # while self.global_status_num_index > 0 or self.content_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
        #     while self.content_data_list or threadlist:
        #         for threadi in threadlist:
        #             if not threadi.is_alive():
        #                 threadlist.remove(threadi)
        #         while len(threadlist) < CONTENT_THREADING_NUM and self.content_data_list:
        #             data_in_while = self.content_data_list.pop()
        #             thread_in_while = threading.Thread(target=get_content_inside, args=(data_in_while,))
        #             thread_in_while.setDaemon(True)
        #             thread_in_while.start()
        #             threadlist.append(thread_in_while)
        #             print 'len of threadlist in content---', len(threadlist)
        #             print 'len of content_data_list in content is ---', len(self.content_data_list)
        #             # time.sleep(1)
        #
        # self.global_status_num_content = 0



if __name__ == '__main__':
    thisclass=thepaper()
    thisclass.get_Index()