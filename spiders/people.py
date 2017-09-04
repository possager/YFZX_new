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


# from visit_page import get_response_and_text
from visit_page2 import get_response_and_text
from KafkaConnector1 import Producer,Consumer
from saveresult import get_result_name
from saveresult import Save_result
import redis



#特殊之处：再最后存数据处增加一个发言人的记录代码。存入数据库，之后遍历这些发言人，从他们的发言记录中找到所有的主贴，再爬取主贴
#其中需要一个记录已经爬取过后的url的号码

class people:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',

        }


        self.connectpool = redis.ConnectionPool(host='localhost', port=6379)
        self.redis1 = redis.Redis(connection_pool=connectpool)



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
        self.index_data_list=['http://bbs1.people.com.cn/mobile.do?action=list&boardId=%s&pageNo='%str(i) for i in [1,13,129,124,131,8,57,11,2,29,27,26,23,44,24,80,13]]#需要添加page
        # self.index_data_list=[]
        # for i in self.index_data_list2:
        #     for j in range(1,100):
        #         self.index_data_list.append(i+str(j))

        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_data_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_data_list = []  # 这个存储的是已经跑完了的内容
        self.publish_user_url_need_to_visit=[]

    def get_Index(self):
        def get_index(url):
            error_num=5#又是请求过于频繁，会出现eof错误
            while True:
                response1=get_response_and_text(url=url)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                # print response_in_function_text

                try:
                    datajson=json.loads(response_in_function_text)
                    if not datajson['elements']:
                        break#没有数据了，请求完了
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
                            'reply_nodes':[],
                            'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                        }

                        self.content_data_list.append(this_index_info)

                    urlsplit=url.split('pageNo=')
                    url=urlsplit[0]+str(int(urlsplit[1])+1)

                except Exception as e:
                    print e
                    print 'mark1'
                    error_num-=1
                    if error_num<0:
                        break
                    time.sleep(3)







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

            response2=get_response_and_text(url=url_for_debug,headers=self.headers)
            try:
                datasoup=BeautifulSoup(response2['response_in_function_text'],'lxml')
                publish_time=datasoup.select('.replayInfo .float_l.mT10')[0].text.split(u'\xa0')[-1]
                data['publish_time']=publish_time
            except Exception as e:
                print e
                print 'mark1'


            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']

            datasoup=BeautifulSoup(response_in_function_text,'lxml')

            content=datasoup.select('div.artCont .content-text')
            if content:#没有结果content应该回事空
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
                data['img_urls']=img_list

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
            comment_list=[]
            error_time=5
            page_num=1
            while True:
                try:
                    comment_url='http://bbs1.people.com.cn/mobile.do?action=moreComment&threadId='+str(data['id'])+'&pageNo='+str(page_num)
                    response1=get_response_and_text(url=comment_url)
                    response_in_function=response1['response_in_function']
                    response_in_function_text=response1['response_in_function_text']
                    datajson=json.loads(response_in_function_text)
                    if not datajson['elements']:
                        break
                    for i in datajson['elements']:
                        id= i['id']
                        title=i['title']
                        publish_user=i['userNick']

                        one_comment={
                            'id':id,
                            'content':title,
                            'publish_user':publish_user,
                            'parent_id':data['id'],
                            'ancestor_id':data['id']
                        }
                        comment_list.append(one_comment)
                    page_num+=1
                except Exception as e:
                    print e
                    print 'mark3'
                    error_time-=1
                    if error_time<0:
                        break
                    time.sleep(5)

            data['reply_nodes']=comment_list
            self.result_data_list.append(data)



        threadlist = []
        while self.global_status_num_content > 0 or self.comments_data_list:  # content没有完，就别想完，
            while self.comments_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.comments_data_list:
                    data_in_while = self.comments_data_list.pop()
                    thread_in_while = threading.Thread(target=get_comment_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)

    def save_result(self):
        def save_result(data):
            save_user_to_redis(data)




            # host = '192.168.6.187:9092,192.168.6.188:9092,192.168.6.229:9092,192.168.6.230:9092'
            # producer = Producer(hosts=host)
            # result_file = get_result_name(plantform_c='澎湃新闻',plantform_e='thepaper', date_time=data['publish_time'], urlOruid=data['url'],
            #                               newsidOrtid=data['id'],
            #                               datatype='news', full_data=data)
            # producer.send(topic='topic', value={'data': data}, key=result_file, updatetime=data['spider_time'])
            #
            # comsumer = Consumer('topic', host, 'll')
            # what = comsumer.poll()
            # for i in what:
            #     # topic = i.topic
            #     # partition = i.partition
            #     # offset = i.offset
            #     # key = i.key
            #     value = i.value
            #
            #
            #     Save_result(plantform='xilu', date_time=data['publish_time'], urlOruid=data['url'],
            #                 newsidOrtid=data['id'],
            #                 datatype='news', full_data=value['content'])

            Save_result(plantform='people', date_time=data['publish_time'], urlOruid=data['url'],
                        newsidOrtid=data['id'],
                        datatype='forum', full_data=data)


        def save_user_to_redis(data):
            for comment in data['reply_nodes']:
                self.redis1.hset('people_publish_user',comment['publish_user'],0)



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


        self.global_status_num_comments = 0

    def create_new_forum_from_redis(self):
        def get_user_from_redis():
            all_publish_user=self.redis1.hgetall('people_publish_user')
            publish_user_without_visited=filter(lambda x:x[1]=='0',all_publish_user.items())
            for one_publish_user in publish_user_without_visited:
                self.index_data_list.append('http://bbs1.people.com.cn/mobile.do?action=userInfo&opt=thread&userNick='+one_publish_user[0]+'&pageNo=1')#这里的编码刚刚好
                self.redis1.hset('people_publish_user',one_publish_user[0],1)




#根据这个网站来设计的

        while True:
            get_user_from_redis()
            time.sleep(10)


    def run(self):
        thread1 = threading.Thread(target=self.get_Index, args=())
        thread1.start()
        # time.sleep(5)
        thread2 = threading.Thread(target=self.get_content, args=())
        thread2.start()
        # time.sleep(3)
        thread3 = threading.Thread(target=self.get_comments, args=())
        thread3.start()
        thread4 = threading.Thread(target=self.save_result, args=())
        thread4.start()
        thread5=threading.Thread(target=self.create_new_forum_from_redis,args=())
        thread5.start()
        pass
if __name__ == '__main__':
    thisclass=people()
    thisclass.run()