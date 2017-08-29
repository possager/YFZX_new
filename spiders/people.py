# _*_coding:utf-8_*_
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import json
import time
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

# from visit_page2 import get_response_and_text
from visit_page import get_response_and_text
from KafkaConnector1 import Producer,Consumer
from saveresult import get_result_name
import redis





class people:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'X-Requested-With': 'XMLHttpRequest',  # 重要
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'close',
            'Host': 'm.xilu.com',
            'Upgrade-Insecure-Requests': '1'

        }



        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        # self.index_data_list=['http://bbs1.people.com.cn/board/1.html',#强国论坛
        #                       'http://bbs1.people.com.cn/mobile.do?action=list&boardId=13&pageNo=2',
        #                       'http://bbs1.people.com.cn/board/1/129.html',#新闻论坛
        #                       'http://bbs1.people.com.cn/board/6.html',#纵横国际
        #                       'http://bbs1.people.com.cn/board/7.html',#军迷营地
        #                       'http://bbs1.people.com.cn/board/71.html',#百姓监督
        #                       'http://bbs1.people.com.cn/board/60.html',#煮酒论史
        #                       'http://bbs1.people.com.cn/board/124.html',#人民瓷坛
        #                       'http://bbs1.people.com.cn/board/131.html',#育儿宝
        #                       'http://bbs1.people.com.cn/board/8.html',#教育
        #                       'http://bbs1.people.com.cn/board/57.html',#房产
        #                       'http://bbs1.people.com.cn/board/11.html',#经济
        #                       'http://bbs1.people.com.cn/board/2.html',#深入讨论
        #                       'http://bbs1.people.com.cn/board/1/29.html',#贴图原地
        #                       'http://bbs1.people.com.cn/board/1/27.html',#娱乐杂谈
        #                       'http://bbs1.people.com.cn/mobile.do?action=list&boardId=27&pageNo=2',
        #                       'http://bbs1.people.com.cn/board/26.html',#女性论坛
        #                       'http://bbs1.people.com.cn/board/23.html',#养生生活
        #                       'http://bbs1.people.com.cn/board/44.html',#文化沙龙
        #                       'http://bbs1.people.com.cn/board/24.html',#联谊会馆
        #                       'http://bbs1.people.com.cn/board/80.html',#大学生
        #                       'http://bbs1.people.com.cn/board/13.html',#中日
        #
        #                       ]
        # self.index_data_list='http://bbs1.people.com.cn/mobile.do?action=list&boardId={}&pageNo=2'.format(str(i) for i in [1,13,129,124,131,8,57,11,2,29,27,26,23,44,24,80,13])
        self.index_data_list=['http://bbs1.people.com.cn/mobile.do?action=list&boardId=%s&pageNo=1'%str(i) for i in [1,13,129,124,131,8,57,11,2,29,27,26,23,44,24,80,13]]
        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_data_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_data_list = []  # 这个存储的是已经跑完了的内容

    def get_Index(self):
        def get_index(url):
            response1=get_response_and_text(url=url)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            # print response_in_function_text
            try:
                datajson=json.loads(response_in_function_text)

                for one_data in datajson['elements']:
                    title=one_data['title']
                    reply_count=one_data['replyCount']
                    publish_user=one_data['usernick']
                    read_count=one_data['readCount']
                    like_count=one_data['like']
                    url=one_data['url']
                    id=one_data['id']
                    publish_time=u'2017-'+one_data['createTime'].replace(u'月',u'-').replace(u'日',u'')+u':00'

                    this_index_info={
                        'title':title,
                        'reply_count':reply_count,
                        'publish_user':publish_user,
                        'read_count':read_count,
                        'like_count':like_count,
                        'url':u'http://bbs1.people.com.cn'+url,
                        'id':id,
                        'publish_time':publish_time,
                    }

                    self.content_data_list.append(this_index_info)

            except Exception as e:
                print e







            url_split=response_in_function.url.split('pageNo=')
            urlnext=url_split[0]+'pageNo='+str(int(url_split[1])+1)
            get_index(url=urlnext)




        threadlist=[]
        while self.index_data_list or threadlist:
            for threadi in threadlist:
                if not threadi.is_alive():
                    threadlist.remove(threadi)
            while len(threadlist) < CONTENT_THREADING_NUM and self.index_data_list:
                data_in_while = self.index_data_list.pop()
                thread_in_while = threading.Thread(target=get_index, args=(data_in_while,))
                thread_in_while.setDaemon(True)
                thread_in_while.start()
                threadlist.append(thread_in_while)

    def get_content(self):
        def get_content_inside(data):
            url_for_debug=data['url']
            response1=get_response_and_text(url=url_for_debug)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']

            datasoup=BeautifulSoup(response_in_function_text,'lxml')

            content=datasoup.select('div.artCont')
            if content:
                content_text=content[0].text.strip()
                Re_find_img_url = re.compile(r'src="(.*?)"')
                img_list=Re_find_img_url.findall(str(content[0]))
                if img_list:
                    for i in range(len(img_list)):
                        if 'http' not in img_list[i]:
                            img_list[i]='http://bbs1.people.com.cn'+img_list[i]
                            print img_list[i]
                else:
                    img_list=[]
                data['content']=content_text
                data['img_list']=img_list

                self.comments_data_list.append(data)


        threadlist=[]
        while self.global_status_num_index or self.content_data_list:
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

    def get_comments(self):
        def get_comment_inside(data):
            #http://bbs1.people.com.cn/mobile.do?action=moreComment&threadId=164157231&pageNo=2
            comment_list=[]



            while True:
                comment_url='http://bbs1.people.com.cn/mobile.do?action=moreComment&threadId='+data['id']+'&pageNo=1'
                response1=get_response_and_text(url=comment_url)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                datajson=json.loads(response_in_function_text)
                for i in datajson['elements']:
                    id= i['id']
                    title=i['title']
                    publish_user=i['userNick']



        threadlist = []
        while self.global_status_num_content > 0 or self.comments_url_list:  # content没有完，就别想完，
            while self.comments_url_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.comments_url_list:
                    data_in_while = self.comments_url_list.pop()
                    thread_in_while = threading.Thread(target=get_comment_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
                    print len(threadlist)
                    print len(self.comments_url_list)


    def run(self):
        thread1 = threading.Thread(target=self.get_Index, args=())
        thread1.start()
        # time.sleep(5)
        thread2 = threading.Thread(target=self.get_content, args=())
        thread2.start()
        # time.sleep(3)
        # thread3 = threading.Thread(target=self.get_comments, args=())
        # thread3.start()
        # thread4 = threading.Thread(target=self.save_result, args=())
        # thread4.start()
        pass
if __name__ == '__main__':
    thisclass=people()
    thisclass.run()