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
from KafkaConnector import RemoteProducer,Consumer



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
            for i in range(101,10000000):
                if self.global_status_num_index==0:
                    return #用来判断何时停止
                while True:
                    if len(self.content_data_list)<100:
                        self.content_data_list.append(
                            {
                                'url':'http://www.chengshiluntan.com/'+str(i)+'-1.html',
                                'content':'',
                                'publish_user':'',
                                'publish_time':'',
                                'reply_nodes':[],
                                'id':'',
                                'read_count':0,
                                'reply_count':0,
                                'title':'',
                                'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            }
                                                      )
                        break
                    else:
                        time.sleep(1)
        get_index_inside()

    def get_content(self):
        Re_find_img_url = re.compile(r'src="(.*?)"')
        def get_content_inside(data):
            is_first=0
            url_debug = data['url']

            while True:
                response1=get_response_and_text(url=url_debug,headers=self.headers)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                datasoup=BeautifulSoup(response_in_function_text,'lxml')

                if is_first==0:
                    is_first=1
                    try:
                        data['title']=datasoup.select('#thread_subject')[0].text
                    except Exception as e:
                        print e
                        return #有些帖子是没有的
                        # print data['url']
                    data['reply_count']= datasoup.select('#postlist > div.bm_h.comiis_snvbt > span.y.comiis_hfs > strong')[0].text
                    data['read_count']= datasoup.select('#postlist > div.bm_h.comiis_snvbt > span.y.comiis_cks > strong')[0].text
                    content_div=datasoup.select('#postlist > div[id]')[0]
                    content_div_str=str(content_div)
                    img_urls=Re_find_img_url.findall(content_div_str)
                    data['img_urls']=img_urls
                    data['publish_user']= content_div.select('tr:nth-of-type(1) > td.plc > div.pi > div.pti > div.authi > a.xi2.kmyzz')[
                        0].text  # publish_user
                    publish_time_content= content_div.select('tr:nth-of-type(1) > td.plc > div.pi > div.pti > div.authi  > em')[
                        0].text.replace(u'发表于', '').strip()+':00'  # pubtlish_time
                    data['publish_time']=time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(publish_time_content,'%Y-%m-%d %H:%M:%S'))
                    data['content']= content_div.select(' div.t_fsz > div.t_f')[0].text.strip()  # content

                follow_div=datasoup.select('#postlist > div[id]')[is_first:-1]
                for one_reply in follow_div:
                    comment_reply_nodes=[]
                    publish_user=one_reply.select('tr:nth-of-type(1) > td.plc > div.pi > div.pti > div.authi > a.xi2.kmyzz')[
                        0].text  # publish_user
                    publish_time= one_reply.select('tr:nth-of-type(1) > td.plc > div.pi > div.pti > div.authi  > em')[
                        0].text.replace(u'发表于', '').strip()  # pubtlish_time
                    content= one_reply.select(' div.t_fsz > div.t_f')[0].text.strip()  # content
                    id=one_reply.get('id')
                    if one_reply.select('div.cm')[0].text.strip():
                        id= one_reply.select('div.cm')[0].get('id')  # comment_id
                        publish_user_photo= one_reply.select('div.cm div.pstl div.psta a > img')[0].get('src')  # publish_photo
                        content= one_reply.select('div.pstl div.psti')[0].text.split(u'详情')[0].strip()  # content
                        publish_user= one_reply.select('div.pstl div.psta a.xi2')[0].text  # publish_user
                        publish_time= one_reply.select('div.pstl div.psti span.xg1')[0].text.replace(u'发表于',
                                                                                                   '').strip()  # publish_time

                        comment_reply_node={
                            'id':id,
                            'publish_user_photo':publish_user_photo,
                            'content':content,
                            'publish_user':publish_user,
                            'publish_time':publish_time,

                        }
                        comment_reply_nodes.append(comment_reply_node)

                    img_urls_reply = Re_find_img_url.findall(str(one_reply))

                    try:
                        publish_user_id= one_reply.select('td.pls > div.pls')[0].get('id')  # id
                        publish_user_photo= one_reply.select('td.pls > div.pls div div.avatar a img')[0].get(
                            'src')  # publish_user_photo
                        # publish_user_id= one_reply.select('td.pls > div.pls div.m.z div[id]')[0].get('id')  # publish_user_id
                    except Exception as e:
                        print e
                        id=''
                        publish_user_photo=''
                        publish_user_id=''

                    this_comment_node={
                        'publish_user':publish_user,
                        'publish_time':time.strftime('%Y-%m-%d %H:%M:%S',time.strptime(publish_time+':00','%Y-%m-%d %H:%M:%S')),
                        'content':content,
                        'id':id,
                        'publish_user_photo':publish_user_photo,
                        'publish_user_id':publish_user_id,
                        'reply_nodes':comment_reply_nodes,
                        'url':url_debug+"#"+id,
                        'img_urls':img_urls_reply
                    }
                    data['reply_nodes'].append(this_comment_node)
                url_next_div=datasoup.select('a.nxt')
                if url_next_div:
                    url_next=url_next_div[0].get('href')
                    # if len(url_next)<7:
                    url_debug='http://www.chengshiluntan.com/'+url_next
                    # else:
                    #     print len(url_next)
                    #     break
                else:
                    self.result_data_list.append(data)
                    break

        threadlist=[]
        while self.global_status_num_comments > 0 or self.content_data_list:
            while self.content_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.content_data_list:
                    print len(self.content_data_list)
                    data_in_while = self.content_data_list.pop()
                    thread_in_while = threading.Thread(target=get_content_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)

    def save_result(self):
        def save_result(data):
            # Save_result(plantform='chengshiluntan', date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
            #             datatype='forum', full_data=data)

            host = '182.150.63.40'
            port = '12308'
            username = 'silence'
            password = 'silence'

            producer = RemoteProducer(host=host, port=port, username=username, password=password)
            result_file = get_result_name(plantform_e='csdn', plantform_c='城市论坛',
                                          date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
                                          datatype='forum', full_data=data)

            producer.send(topic='1101_STREAM_SPIDER', value={'data': data}, key=result_file,
                          updatetime=data['spider_time'])




        threadlist=[]
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
            # time.sleep(5)
            thread2 = threading.Thread(target=self.get_content, args=())
            thread2.start()

            thread4 = threading.Thread(target=self.save_result, args=())
            thread4.start()
            pass

if __name__ == '__main__':
    thisclass=chengshiluntan()
    thisclass.run()