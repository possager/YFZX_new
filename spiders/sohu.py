#_*_coding:utf-8_*_
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


class sohu:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }
        self.urls = [
            'http://v2.sohu.com/public-api/feed?scene=CHANNEL&sceneId=8&page=',#1&size=20
            # 'https://api.m.sohu.com/autonews/cpool/?n=%E6%96%B0%E9%97%BB&s='#0&c=20&dc=1#这里边貌似都是汽车新闻
        ]
        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容

    def get_Index(self):
        url_to_get_index1=self.urls[0]
        # url_to_get_index2=self.urls[1]#带type的
        for i in range(1,900):
            response_index_all=self.session1.request(method='get',url=url_to_get_index1+str(i)+'&size=20',headers=self.headers)
            datajson=json.loads(response_index_all.text)
            for i in datajson:
                url_index='https://m.sohu.com/a/'+str(i['id'])+'_'+str(i['authorId'])
                publish_time=i['publicTime']
                publish_time = int(publish_time) / 1000
                time_format = '%Y-%m-%d %h:%m:%s'
                publish_time_stamp_9 = time.localtime(float(publish_time))
                publish_time = time.strftime(time_format, publish_time_stamp_9)
                data_index={
                    'publish_user':i['authorName'],
                    'title':i['title'],
                    'publish_time':publish_time,
                    'id':i['id'],
                    'url':url_index,
                    'cmsid':i['cmsId'],
                    # 'which_website':1
                         }
                self.content_data_list.append(data_index)
            time.sleep(1)




        self.global_status_num_index=0

    def get_content(self):

        def get_content_inside(data):
            session1 = requests.session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            session1.cookies = cookielib.MozillaCookieJar()
            while True:  # 强制请求
                try:
                    timea = time.time()
                    session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
                    response_in_function = session1.request(method='get', url=data['url'], headers=headers,
                                                            timeout=5)  # 这里的headers会因为其它的线程使用而有所改变，因为线程安全的原因，这里不好控制，控制的意义不大。
                    break
                except Exception as e:
                    session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
                    timea = time.time()
                    print e
            timeb = time.time()
            response_in_function.encoding = 'utf-8'
            proxy_here = session1.proxies.values()[0].split('//')[1]
            if timeb - timea < 3:
                proxy_sendback(proxy_here)


            img_urls=[]
            content=''
            datasoup=BeautifulSoup(response_in_function.text,'lxml')
            if datasoup.select('#articleContent > div.display-content > p'):
                for i in datasoup.select('#articleContent > div.display-content > p'):
                    content+= i.text
            else:
                for i in datasoup.select('#articleContent > div.display-content'):
                    content+=i

            try:
                content_data=str(datasoup.select('#articleContent > div.display-content')[0])
            except Exception as e:
                print e
                try:
                    content_data=str(datasoup.select('#articleContent')[0])
                except:
                    return
            Re_find_img=re.compile(r'img src=".*?"')
            for img_url in Re_find_img.findall(content_data):
                img_urls.append(img_url)
            data['content']=content
            data['img_urls']=img_urls
            data['reply_nodes']=[]

            self.comments_url_list.append(data)




        threadlist=[]
        while self.global_status_num_index > 0 or self.content_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
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
                    print 'len of threadlist in content---', len(threadlist)
                    print 'len of content_data_list in content is ---', len(self.content_data_list)
                    # time.sleep(1)

        self.global_status_num_content = 0

    def get_comments(self):
        def get_comment_inside(data,cmspagenum=1,comments_data=[],topicid=None,cmspage_taotalnum=0):
            session1 = requests.session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }

            timea = time.time()
            session1.cookies = cookielib.MozillaCookieJar()
            session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:
                    if not topicid:
                        comment_url = 'https://apiv2.sohu.com/api/topic/load?page_size=10&topic_source_id=' + \
                                  str(data['id'])+'&page_no=10'
                    else:
                        comment_url='https://apiv2.sohu.com/api/comment/list?page_size=10&topic_id='+topicid+'&page_no='+cmspagenum
                    response_in_function = session1.request(method='get', url=comment_url, headers=headers,
                                                            timeout=5)  # 这里的headers会因为其它的线程使用而有所改变，因为线程安全的原因，这里不好控制，控制的意义不大。
                    break
                except Exception as e:
                    print e
            timeb = time.time()
            proxy_here = session1.proxies.values()[0].split('//')[1]
            if timeb - timea < 3:
                proxy_sendback(proxy_here)
            data_json = json.loads(response_in_function.text.encode('utf-8'))
            if cmspagenum==1:
                try:
                    cmspage_taotalnum=data_json['jsonObject']['total_page_no']
                except:
                    cmspage_taotalnum=data_json['jsonObject']['outer_cmt_sum']
            for one_comment in data_json['jsonObject']['comments']:
                id=one_comment['comment_id']
                content=one_comment['content']
                url=response_in_function.url
                publish_time=one_comment['create_time']
                publish_time = int(publish_time) / 1000
                time_format = '%Y-%m-%d'
                publish_time_stamp_9 = time.localtime(float(publish_time))
                publish_time = time.strftime(time_format, publish_time_stamp_9)
                publish_user_id=one_comment['user_id']
                like_count=one_comment['support_count']
                reply_count=one_comment['reply_count']
                publish_user=one_comment['passport']['nickname']
                publish_user_photo=one_comment['passport']['img_url']


                thisnode={
                    'id':id,
                    'content':content,
                    'url':url,
                    'publish_time':publish_time,
                    'publish_user_id':publish_user_id,
                    'like_count':like_count,
                    'reply_count':reply_count,
                    'publish_user':publish_user,
                    'publish_user_photo':publish_user_photo
                }


                comments_data.append(thisnode)

            cmspagenum+=1
            if cmspagenum<cmspage_taotalnum+1:
                get_comment_inside(data,cmspagenum,comments_data,cmspage_taotalnum)
            else:
                data['reply_nodes']=comments_data
                self.result_list.append(data)








            # self.result_list.append(data)

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
        self.global_status_num_comments = 0

    def save_result(self):
        def save_result(data):
            print 'deal result'
            print data
            Save_result(plantform='sohu',date_time=data['publish_time'],urlOruid=data['url'],newsidOrtid=data['id'],datatype='news',full_data=data)
        threadlist = []
        while self.global_status_num_comments > 0 or self.result_list:
            while self.result_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.result_list:
                    print len(self.result_list)
                    data_in_while = self.result_list.pop()
                    thread_in_while = threading.Thread(target=save_result, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
                    print len(threadlist)
                    print len(self.result_list)
        self.global_status_num_comments = 0





    def run(self):
        thread1=threading.Thread(target=self.get_Index,args=())
        thread1.start()
        time.sleep(5)
        thread2=threading.Thread(target=self.get_content,args=())
        thread2.start()
        time.sleep(3)
        thread3=threading.Thread(target=self.get_comments,args=())
        thread3.start()
        thread4=threading.Thread(target=self.save_result,args=())
        thread4.start()
        pass

if __name__ == '__main__':
    thisclass=sohu()
    thisclass.run()