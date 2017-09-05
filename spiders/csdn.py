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


from visit_page import get_response_and_text
# from visit_page2 import get_response_and_text
from KafkaConnector1 import Producer,Consumer
from saveresult import get_result_name
from saveresult import Save_result
import redis


class csdn:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            # 'X-Requested-With': 'XMLHttpRequest',  # 重要
            # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            # 'Cache-Control': 'max-age=0',
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
        def get_index_1():#获得该论坛所有子论坛的
            while True:
                try:#response_in_function_text有时候乱码有时候不乱码
                    url_rukou='http://bbs.csdn.net/home'
                    response1=get_response_and_text(url=url_rukou,headers=self.headers)
                    response_in_function_text=response1['response_in_function_text']
                    datasoup=BeautifulSoup(response_in_function_text,'lxml')
                    for a in datasoup.select('.dropdown-menu a[href]'):
                        url_bankuai= 'http://bbs.csdn.net'+a.get('href')
                        print url_bankuai
                        self.index_data_list.append(url_bankuai)
                    if self.index_data_list:
                        break
                except Exception as e:
                    print e
        def get_index_2(url):
            while True:
                response1=get_response_and_text(url=url,headers=self.headers)
                response_in_function_text=response1['response_in_function_text']
                try:
                    datasoup=BeautifulSoup(response_in_function_text,'lxml')
                    for content in datasoup.select('.content > table > tr')[1:-1]:
                        title=content.select('td.title > a[title]')[0].text.strip()#title
                        url='http://bbs.csdn.net'+content.select('td.title > a[title]')[0].get('href').strip()
                        publish_user=content.select('td.tc a[title]')[0].get('title').strip()#publish_user
                        # content.select('td.tc a[title]')[0].get('href')#publish_user_href
                        reply_count=content.select('td:nth-of-type(4)')[0].text#read_count
                        this_nodes={
                            'url':url,
                            'publish_user':publish_user,
                            'title':title,
                            'reply_count':reply_count,
                            'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                            'id':url.split('/')[-1],
                            'like_count':0,#根本没有
                            'content':None,
                            'reproduce_count':0,
                            'publish_user_photo':'',
                            'reply_nodes':[]

                        }
                        self.content_data_list.append(this_nodes)

                    next_page_url=datasoup.select('a.next')
                    if next_page_url:
                        url_next='http://bbs.csdn.net'+next_page_url[0].get('href')
                        url=url_next
                    else:
                        break

                except Exception as e:
                    print e

        get_index_1()
        threadlist=[]
        while self.index_data_list or threadlist:
            for threadi in threadlist:
                if not threadi.is_alive():
                    threadlist.remove(threadi)
            while len(threadlist) < CONTENT_THREADING_NUM and self.index_data_list:
                data_in_while = self.index_data_list.pop()
                thread_in_while = threading.Thread(target=get_index_2, args=(data_in_while,))
                thread_in_while.setDaemon(True)
                thread_in_while.start()
                threadlist.append(thread_in_while)

    def get_content(self):
        Re_find_img_url = re.compile(r'src="(.*?)"')
        def handleContent(content):  # 去除文章中的html标签以及空格字符
            # html_re = re.compile(r"<.+?>",re.S)
            # content = html_re.sub("",content)
            # space_re = re.compile(r"\s+?",re.S)
            # content = space_re.sub("",content)
            script_re = re.compile(r'<script.*?>\s*[^|]*?<\/script>', re.S)
            content = script_re.sub("", content)
            style_re = re.compile(r'<style.*?>\s*[^|]*?<\/style>', re.S)
            content = style_re.sub("", content)
            # content=Re_replace_js.sub('',content)
            return content.strip()

        def get_content_inside(data):
            url_debug=data['url'] + '?page=1'
            while True:
                response1=get_response_and_text(url=url_debug,headers=self.headers)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                response_in_function_text=handleContent(response_in_function_text)
                datasoup=BeautifulSoup(response_in_function_text,'lxml')

                page_begain=0

                if not data['content']:#用来记录是否需要获取content，publish_user的信息
                    page_begain=1
                    try:
                        content_div=datasoup.select('div.detailed table.post .post_body')[0]
                        content=content_div.text.strip()
                    except Exception as e:
                        print e
                        print data['url']
                        return
                    img_urls_content=Re_find_img_url.findall(str(content_div))
                    publish_user_photo=datasoup.select('div.detailed table.post .user_info .user_head a img')[0].get('src')
                    publish_time=datasoup.select('div.detailed table.post .time')[0].text.strip().split('\n')[1].strip()

                    data['content']=content
                    data['publish_user_photo']=publish_user_photo
                    data['publish_time']=publish_time
                    data['img_urls']=img_urls_content

                for one_reply in datasoup.select('div.detailed table.post')[page_begain:]:
                    try:
                        j = one_reply.select('div.post_body')
                        img_urls = Re_find_img_url.findall(str(j))
                        img_urls2 = []
                        for img_url_maybe_have_js in img_urls:
                            if '.js' not in img_url_maybe_have_js:
                                img_urls2.append(img_url_maybe_have_js)

                        content = one_reply.select('.post_body')[0].text.strip()
                        publish_user_photo=one_reply.select('.user_info .user_head a img')[0].get('src')#publish_user_photo
                        publish_time=one_reply.select('.time')[0].text.strip().split('\n')[1].strip()
                        louceng_url=one_reply.select('.data .fr a[href]')[0].get('href')
                        like_count=one_reply.select(' div.control .fr a.red')[0].text.split('[')[1].split(']')[0]
                        dislike_count=one_reply.select(' div.control .fr a.bury')[0].text.split('[')[1].split(']')[0]
                        publish_user= one_reply.select('.user_info .nickname span')[0].text
                        ancestor_id=data['id']
                        parent_id=data['id']
                        publish_user_id=louceng_url.split('post-')[1]
                        url=data['url']+louceng_url

                        thisnode={
                            'publish_user_photo':publish_user_photo,
                            'publish_time':publish_time,
                            'like_count':like_count,
                            'dislike_count':dislike_count,
                            'publish_user':publish_user,
                            'ancestor_id':ancestor_id,
                            'parent_id':parent_id,
                            'publish_user_id':publish_user_id,
                            'url':url,
                            'img_urls':img_urls2,
                            'content':content
                        }
                        data['reply_nodes'].append(thisnode)
                    except Exception as e:
                        print e


                next_page_div=datasoup.select('.page_nav .next')
                if next_page_div:
                    next_url='http://bbs.csdn.net'+next_page_div[0].get('href')
                    url_debug=next_url
                else:
                    self.result_data_list.append(data)
                    break



                # urlsplit= url.split('page=')
                # url1=urlsplit[0]+'page='+str(int(urlsplit[1])+1)






        threadlist = []
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
                    # print len(threadlist)
                    # print len(self.index_data_list)

    def save_result(self):
        def save_result(data):
            Save_result(plantform='csdn', date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
                        datatype='news', full_data=data)
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
            # # time.sleep(3)
            # thread3 = threading.Thread(target=self.get_comments, args=())
            # thread3.start()
            thread4 = threading.Thread(target=self.save_result, args=())
            thread4.start()
            pass


if __name__ == '__main__':
    thisclass=csdn()
    thisclass.run()