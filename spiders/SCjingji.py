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
from get_proxy_from_XMX import get_proxy_couple
from get_proxy_from_TG import getSqliteProxy
from sava_data_to_MongoDB import save_data_to_mongodb
from sava_data_to_MongoDB import save_data_to_mongodb_without_full
import Queue


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

        self.global_status_finish=5

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.index_data_list=[]
        self.index_data_list2 = ['http://www.scjjrb.com/Item/list.asp?id=674&page=1',
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

        self.cache_data_list=Queue.Queue()

    def get_Index(self):
        def get_index_inside(url):
            url_debug=url
            next_page_num=2

            while True:
                response1 = self.visit_page_in_class_post(url=url_debug)
                if not response1:
                    break
                response1.encoding='gb2312'
                response_in_function_text = response1.text
                datasoup=BeautifulSoup(response_in_function_text,'lxml')


                content_div_list=datasoup.select('div.newslist')
                try:
                    newslist = content_div_list[0].select('dl.nl_con1')
                    for i in newslist:
                        title = i.select('h4.nlc_tit a')[0].get('title')  # title
                        href = i.select('h4.nlc_tit a')[0].get('href')  # href
                        publish_time = i.select('p.nlc_time')[0].text.split(u' ')[0]  # publish_time
                        this_index = {
                            'title': title,
                            'url': href,
                            'publish_time': publish_time.replace(u'年', '-').replace(u'月', '-').replace(u'日',
                                                                                                       '') + ' 00:00:00',
                            'id': href.split('/')[-1].split('.')[0],
                            'spider_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                        }
                        self.content_data_list.append(this_index)
                except Exception as e:
                    print e



                next_a = datasoup.select('a.next')  # 下一页链接，这里边的链接就是这样
                try:
                    next_url=next_a[1].get('href')
                    if next_url not in ['javascript:;']:
                        url_debug=url.split('?')[0]+next_url
                        next_page_num-=1
                        if next_page_num<1:
                            break

                    else:
                        break
                except:
                    break

        threadlist=[]
        num_print=0
        self.index_data_list=self.index_data_list2
        while self.index_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
            while self.index_data_list or threadlist:
                num_print+=1
                if num_print>10000:
                    # print '获取content_url_list的线程队列的长度是----',len(threadlist)
                    num_print=0
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.index_data_list:
                    data_in_while = self.index_data_list.pop()
                    thread_in_while = threading.Thread(target=get_index_inside, args=(data_in_while,))
                    # thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    # thread_in_while.join(timeout=600)
                    threadlist.append(thread_in_while)
                for childthread in threadlist:
                    childthread.join(600)
        while True:
            self.global_status_num_content=0
            time.sleep(5)
            if self.global_status_num_content==0:
                break

    def visit_page_in_class_post(self,url,data=None,headers=None,charset=None):
        # session1 = requests.session()
        timeout_value=5
        wrong_time_error_time=0
        if headers:
            this_headers = headers
        else:
            this_headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
                'Connection': 'close'
            }
        while True:
            try:


                proxies1=getSqliteProxy()


                response_in_function = requests.get(url=url, headers=headers, proxies=proxies1,
                                                    timeout=timeout_value)
                if charset:
                    response_in_function.encoding = charset
                response_in_function_text = response_in_function.text



                if response_in_function.status_code in range(200, 300):
                    break
            except Exception as e:
                # print e
                wrong_time_error_time+=1
                if wrong_time_error_time>10:
                    return
        # proxy_sendback(proxies_from_db)
        # session1.close()
        return response_in_function

    def get_content(self):
        Re_find_img_url = re.compile(r' src="(.*?)"')
        def get_content_inside(data):
            url_debug=data['url']
            response1=self.visit_page_in_class_post(url=url_debug)
            if not response1:
                return
            response1.encoding = 'gb2312'

            response_in_function_text=response1.text
            datasoup=BeautifulSoup(response_in_function_text,'lxml')

            try:
                publish_user= datasoup.select('div.articlecontent .info span')[0].text.split(u'：')[1]  # publish_user
            except Exception as e:
                publish_user=''
                # print e
                return
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
            data['source']=publish_user
            data['img_urls']=img_urls

            self.result_data_list.append(data)

        threadlist = []
        while self.global_status_num_content > 0 or self.content_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
            while self.content_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.content_data_list:
                    data_in_while = self.content_data_list.pop()
                    thread_in_while = threading.Thread(target=get_content_inside, args=(data_in_while,))
                    # thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    # thread_in_while.join(timeout=600)
                    threadlist.append(thread_in_while)
                for childthread in threadlist:
                    childthread.join(600)
        while True:
            print 'get_content执行完毕'
            self.global_status_num_result=0
            time.sleep(5)
            if self.global_status_num_result==0:
                break

    def save_result(self):
        def save_result(data):

            result_file = get_result_name(plantform_e='SCjingji', plantform_c='四川经济网',
                                          date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
                                          datatype='forum', full_data=data)

            if not result_file:
                return

            print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'--------',result_file


            save_data_to_mongodb(data={'data':data},item_id=result_file,platform_e='SCjingji',platform_c='四川经济网',cache_data_list=self.cache_data_list)

            # producer.send(topic='1101_STREAM_SPIDER', value={'data': data}, key=result_file,
            #               updatetime=data['spider_time'])

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
            self.global_status_finish=0
            time.sleep(10)
            if self.global_status_finish==0:
                break



    def run(self):
            thread1 = threading.Thread(target=self.get_Index, args=())
            thread1.start()
            thread2 = threading.Thread(target=self.get_content, args=())
            thread2.start()

            thread4 = threading.Thread(target=self.save_result, args=())
            thread4.start()
            # while self.global_status_num_content>0:
            #     print '有新闻列表--',len(self.content_data_list),'  个需要访问'
            #     print 'content_data_list--',len(self.content_data_list)
            #     print 'result_data_list--',len(self.result_data_list)
            #     print 'index_data_list--',len(self.index_data_list)
            #     print 'global_status_index--',self.global_status_num_index
            #     print 'global_status_content--',self.global_status_num_content
            #     print 'global_status_comment--',self.global_status_num_comments
            #     print 'global_status_result--',self.global_status_num_result
            #     print 'global_status_finish--',self.global_status_finish
            #     print '-------------sleep---------------------'
            #     time.sleep(2)
            #
            # while self.global_status_num_result >0:
            #     print '有新闻内容----',len(self.result_data_list),'  个需要访问'
            #     print 'content_data_list--', len(self.content_data_list)
            #     print 'result_data_list--', len(self.result_data_list)
            #     print 'index_data_list--', len(self.index_data_list)
            #     print 'global_status_index--', self.global_status_num_index
            #     print 'global_status_content--', self.global_status_num_content
            #     print 'global_status_comment--', self.global_status_num_comments
            #     print 'global_status_result--', self.global_status_num_result
            #     print 'global_status_finish--',self.global_status_finish
            #     time.sleep(2)
            # while self.global_status_finish > 0:
            #     print '有结果需要存储'

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

            # while self.global_status_num_comments != 0:
            #     print 'content没有获取完'
            #     print '--------the global status num content--', self.global_status_num_content
            #     print '------the global status num comment--', self.global_status_num_comments
            #     print '----the global status num result--', self.global_status_num_result
            #     print '--the global status finish--', self.global_status_finish
            #     print '=======len of comment========', len(self.comments_url_list)
            #     time.sleep(2)

            while self.global_status_num_result != 0:
                print 'result没有获取完'
                print '--------the global status num content--', self.global_status_num_content
                print '------the global status num comment--', self.global_status_num_comments
                print '----the global status num result--', self.global_status_num_result
                print '--the global status finish--', self.global_status_finish
                print '=======len of result========', len(self.result_data_list)
                time.sleep(2)

            # while self.global_status_finish != 0:
            #     print '正在等待finish变为0'
            #     time.sleep(2)

            print '执行完了'

if __name__ == '__main__':
    while True:
        runthrod=10
        thisclass=scjjrb()
        thisclass.run()
        while runthrod>1:
            while runthrod and thisclass.global_status_finish==5:
                runthrod=10
                time.sleep(6) # 因为在类里边实在是不好写定时启动任务了，所以写在这里。。。。。
            runthrod-=1
        print '正在等待着600秒'
        #后来增加的防时间等待模块
        time.sleep(600)