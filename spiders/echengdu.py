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
from sava_data_to_MongoDB import save_data_to_mongodb_without_full


CONTENT_THREADING_NUM=2
COMMENTS_THREADING_NUM=2

class echengde:
    def __init__(self):
        self.headers={
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        self.urls=['http://e.chengdu.cn/html/'+datetime.datetime.now().strftime('%Y-%m/%d')+'/node_{}.htm'.format(str(i)) for i in range(2,13)]

        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4
        self.error_num_to_stop=100



        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_data_list = []  # 这个存储的是已经跑完了的内容

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
                thisurl=url_pre + datetime1 + '/' + i.get('href')
                data_content={
                    'url':thisurl,
                    'id':thisurl.split('_')[1].split('.')[0],
                    'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                }
                self.content_data_list.append(data_content)

        for url in self.urls:
            get_index_inside(url)
        time.sleep(5)
        self.global_status_num_content=0
        # print self.content_data_list
        # print len(self.content_data_list)

    def get_content(self):
        def get_content_inside(data):
            try:
                url_debug=data['url']
                response1=self.visit_page(url=url_debug,headers=self.headers,charset='utf-8')
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                datasoup=BeautifulSoup(response_in_function_text,'lxml')
                Re_find_time = re.compile(ur'(\d{4}年\d{1,2}月\d{1,2}日)')

                title= datasoup.select('div.content-news div.content-title > h4')[0].text
                content_text=''
                for i in datasoup.select('td.xilan_content_tt p'):
                    content_text+= i.text.strip()
                div_contain_time = datasoup.select('div.content-info')[0].text.strip()

                publish_time= Re_find_time.findall(div_contain_time)[0].replace(u'年','-').replace(u'月','-').replace(u'日','')+' 00:00:00'
                publish_user= div_contain_time.split('\n')[1].strip()

                content_div = datasoup.select('div.content-news')[0]
                Re_find_img_url = re.compile(r' src="(.*?)"')
                img_list = Re_find_img_url.findall(str(content_div))
                img_set = set()
                for imgurl in img_list:
                    img_set.add(imgurl.replace('../../..', 'http://e.chengdu.cn'))

                data['publish_user']=publish_user
                data['publish_time']=publish_time
                data['title']=title
                data['content']=content_text
                data['img_urls']=list(img_set)
                self.result_data_list.append(data)

            except Exception as e:
                print url_debug,'这就是错误的信息'
                pass



        threadlist = []
        while self.global_status_num_content > 0 or self.content_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
            while self.content_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.content_data_list:
                    data_in_while = self.content_data_list.pop()
                    thread_in_while = threading.Thread(target=get_content_inside, args=(data_in_while,))
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
                for childthread in threadlist:
                    childthread.join(600)
        self.global_status_num_result=0

    def save_result(self):
        def save_result(data):
            result_file = get_result_name(plantform_e='echengdu', plantform_c='成都商报',
                                          date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
                                          datatype='forum', full_data=data)

            if not result_file:
                return
            print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), '--------', result_file
            save_data_to_mongodb(data={'data': data}, item_id=result_file, platform_e='echengdu', platform_c='成都商报',
                                 cache_data_list=self.cache_data_list)


        threadlist = []
        while self.global_status_num_result > 0 or self.result_data_list:
            while self.result_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.result_data_list:
                    # print len(self.result_data_list)
                    data_in_while = self.result_data_list.pop()
                    thread_in_while = threading.Thread(target=save_result, args=(data_in_while,))
                    thread_in_while.start()
                    # thread_in_while.join(timeout=600)
                    threadlist.append(thread_in_while)
                for childthread in threadlist:
                    childthread.join(600)

        while True:
            self.global_status_finish = 0
            time.sleep(10)
            if self.global_status_finish == 0:
                break

    def run(self):
            thread1 = threading.Thread(target=self.get_Index, args=())
            thread1.start()
            thread2 = threading.Thread(target=self.get_content, args=())
            thread2.start()

            thread4 = threading.Thread(target=self.save_result, args=())
            thread4.start()


            thread1.join(6*60*60)
            thread2.join(6*60*60)
            thread4.join(6*60*60)
            self.global_status_finish=0

            save_data_to_mongodb_without_full(self.cache_data_list)
            while self.global_status_num_content != 0:
                print 'index没有获取完'
                print '--------the global status num content--', self.global_status_num_content
                print '------the global status num comment--', self.global_status_num_comments
                print '----the global status num result--', self.global_status_num_result
                print '--the global status finish--', self.global_status_finish
                print '========len of content========', len(self.content_data_list)
                time.sleep(2)

            while self.global_status_num_result != 0:
                print 'result没有获取完'
                print '--------the global status num content--', self.global_status_num_content
                print '------the global status num comment--', self.global_status_num_comments
                print '----the global status num result--', self.global_status_num_result
                print '--the global status finish--', self.global_status_finish
                print '=======len of result========', len(self.result_data_list)
                time.sleep(2)

            print '执行完了'




if __name__ == '__main__':
    while True:
        runthrod=10
        thisclass=echengde()
        thisclass.run()
        while runthrod>1:
            while runthrod and thisclass.global_status_finish==5:
                runthrod=10
                time.sleep(6) # 因为在类里边实在是不好写定时启动任务了，所以写在这里。。。。。
            runthrod-=1
        print '正在等待下一次执行，预估半天'
        #后来增加的防时间等待模块
        time.sleep(60*60*6)