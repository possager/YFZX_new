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
from KafkaConnector1 import Producer,Consumer
# from saveresult import get_result_name


# from visit_page2 import get_response_and_text
# from KafkaConnector1 import Producer,Consumer
from saveresult import get_result_name
from KafkaConnector import RemoteProducer,Consumer
# from get_proxy_from_XMX import get_proxy_couple


from get_proxy_from_TG import getSqliteProxy
from visit_page3 import get_response_and_text
from sava_data_to_MongoDB import save_data_to_mongodb

import Queue
from sava_data_to_MongoDB import save_data_to_mongodb_new



class gerentushuguan360:
    # 没有图片处理模块，对应的图片处理模块导致信息读取不完全。
    # http://wap.chengdu.cn/1700213这是一个典型的图片新闻网页


    def __init__(self):
        self.headers = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    # 'cookie': 'BDTUJIAID=22139bce90aad109451d0cbbeb0fed77; _ga=GA1.1.1036367116.1504236827; doctaobaocookie=1; 360docsn=RSP8U3SW94AQ0RK7; Hm_lvt_d86954201130d615136257dde062a503=1502150932,1504236788,1504492977; Hm_lpvt_d86954201130d615136257dde062a503=' + str(int(time.time())),
                    'Host': 'www.360doc.com',
                    'Proxy-Connection': 'close',
                    'Referer': 'http://www.360doc.com/index.html',
                    'X-Requested-With': 'XMLHttpRequest',  # 重要
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                }
        self.urls = [
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=7&subClassId=0&nType=10&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=6&subClassId=0&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=10&subClassId=0&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],#健康
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=10&subClassId=0&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],#教育
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=3&subClassId=0&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],#职场
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=440&subClassId=0&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],#财经
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=5&subClassId=0&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],#娱乐
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=1&subClassId=0&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],#艺术
            ['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=12&subClassId=0&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(500)],#上网
        ]
        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.index_data_list=[]
        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_data_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容


        self.cache_data_list=Queue.Queue()

        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=9&subClassId=0&iIscream=0&iSort=1&nPage=3&nType=11
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=9&subClassId=0&iIscream=0&iSort=1&nPage=298&nType=11
        #http://www.360doc.com/ajax/ReadingRoom/getCardListData.ashx?artNum=20&newindex=2
        #http://www.360doc.com/ajax/index7/getZTYDData.ashx?artNum=20&nPage=2

        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?classId=7&subClassId=0&nType=10文化
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=163&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11#人生
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=2&subClassId=0&iIscream=0&iSort=1&nPage=3&nType=11#生活
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?classId=6&subClassId=0&nType=10
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=6&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11#健康
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=10&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11#教育
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=3&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11#职场
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=440&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11#财经
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=5&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11#娱乐
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=1&subClassId=0&iIscream=0&iSort=1&nPage=1&nType=11#艺术
        #http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=12&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11#上网
        #http://www.360doc.com/ajax/index7/getYCData.ashx?artNum=20&nPage=2&iIscream=0&iSort=1&_=1504494212465 #原创

    def visit_page_in_class(self,url):
        # session1=requests.session()
        while True:
            # proxy1=get_proxy_from_redis()
            # proxy1=get_proxy_couple(random.randint(1,50))
            # session1.proxies={'http': 'http://' + proxy1}
            proxies1=getSqliteProxy()
            try:
                # response_1=session1.request(method='get',url=url,headers=self.headers,timeout=10)
                response_1=requests.get(url=url,headers=self.headers,proxies=proxies1,timeout=10)
                if response_1.status_code in range(200, 300):
                    break
            except Exception as e:
                # print e
                pass

        # proxy_sendback(proxy1)
        # session1.close()
        return response_1

    def visit_page_in_class_post(self,url,data=None,charset='utf-8',headers=None):
        # session1 = requests.session()
        # while True:
        #     try:
        #         # proxy1 = get_proxy_from_redis()
        #         # proxy1=get_proxy_couple(random.randint(1,50))
        #         # session1.proxies = {'http': 'http://' + proxy1}
        #         # response_1 = session1.request(method='post', url=url, headers=self.headers, timeout=10,data=data)
        #
        #         proxies1 = getSqliteProxy()
        #         response_1=requests.get(url=url,headers=self.headers,proxies=proxies1,timeout=10)
        #
        #         if response_1.status_code in range(200, 300):
        #             break
        #     except Exception as e:
        #         # print e
        #         pass
        # # proxy_sendback(proxy1)
        # session1.close()
        # return response_1
        while True:
            try:
                while True:
                    proxy = getSqliteProxy()
                    if proxy:
                        break
                while True:
                    response1 = requests.post(url=url, headers=headers, proxies=proxy, timeout=5, data=data)
                    response1.encoding = charset
                    response = response1.text
                    response1.close()
                    response_code = response1.status_code
                    if response_code != 200:
                        continue
                    else:
                        return response1
            except:
                pass

    def get_Index(self):

        for urllist in self.urls:
            self.index_data_list=self.index_data_list+urllist
        pass
        def get_index_inside(url):
            response1=self.visit_page_in_class(url)
            response_in_function_text=response1.text
            try:
                datajson=json.loads(response_in_function_text)
                datajson[0]['data']
            except Exception as e:
                # print e
                return
            for i in datajson[0]['data']:
                title= i['StrArtidetitle']  # title
                # print i['StrDescription']  # 简述
                publish_time= i['StrSaveDate'] + ' 00:00:00'  # publish_time
                publish_user_id= i['StrSaverUserId']  # publish_user_id
                # publish_user= i['StrSource']  # publish_user
                url= i['StrUrl']  # url
                publish_user= i['StrUserName']  # publish_user
                reproduce_num= i['StrSaverNum']  # 转载数量
                id= i['StrArtideid']
                # print '--------------------------------------------------------------'
                self.content_data_list.append(
                    {
                        'title':title,
                        'publish_time':publish_time,
                        'publish_user_id':publish_user_id,
                        'publish_user':publish_user,
                        'url':url,
                        'reproduce_count':int(reproduce_num)-1,
                        'id':id,
                        'reply_nodes':[],
                        'reply_count':0,
                        'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                )

        threadlist=[]
        while self.global_status_num_index > 0 or self.index_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
            while self.index_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.index_data_list:
                    data_in_while = self.index_data_list.pop()
                    thread_in_while = threading.Thread(target=get_index_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)

    def get_content(self):
        Re_find_img_url = re.compile(r' src="(.*?)"')
        def get_content_inside(data):
            url_debug=data['url']
            response1=get_response_and_text(url_debug)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            datasoup=BeautifulSoup(response_in_function_text,'lxml')

            img_list = []#会报错，从try中提出来
            result_read_count=0
            video_urls = []

            try:
                content_raw=datasoup.select('#artContent')
                content=content_raw[0].text.strip()
                img_list2 = Re_find_img_url.findall(str(content_raw[0]))
                for img_url_raw in img_list2:
                    if img_url_raw not in ['http://image21.360doc.com/DownloadImg/2010/12/2413/7923021_1.gif']:
                        if 'swf' not in img_url_raw:
                            img_list.append(img_url_raw)
                        else:
                            video_urls.append(img_url_raw)
            except Exception as e:
                # print e
                content=''
            try:
                url_debug2='http://webservice.360doc.com/GetArtInfo20130912NewV.ashx?UID=-100,'+data['publish_user_id']+',GetBookTwo,'+data['id']+',0,0@cg@0&jsoncallback=jsonp'
                response2=get_response_and_text(url_debug2)
                response_in_function_text2=response2['response_in_function_text']
                result_read_count=response_in_function_text2.split(u'@c@g@tl@c@g@t')[1].split(u'l@c@g@t')[0]
            except Exception as e:
                # print e
                pass

            data['content']=content
            data['read_count']=int(result_read_count)
            data['img_urls']=img_list
            data['video_urls']=video_urls

            self.comments_data_list.append(data)


        threadlist = []
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

    def get_comments(self):
        def get_comment_inside(data):
            post_url='http://www.360doc.cn/ajax/refmore.ashx'
            for i in range(1,100):
                artid_debug=data['id']
                data_to_post_for_comment={
                    'pagenum': str(i),
                    'artid': artid_debug
                }
                response1=self.visit_page_in_class_post(url=post_url,data=data_to_post_for_comment)
                if response1.text ==u'cNullg' or len(response1.text) < 20:
                    break
                comment_datasoup=BeautifulSoup(response1.text,'lxml')
                for i in comment_datasoup.select('.pllist1,.pllist2'):
                    comment_content= i.select('.plbox')[0].text
                    comment_publish_user_photo= i.select('img')[0].get('src')
                    comment_publish_user= i.select('.name1 > a')[0].text
                    # print i.select('.name1 > a')[0].get('href')
                    comment_publish_user_id= i.select('.name1 > a')[0].get('href').split('userid=')[-1]
                    comment_publish_time= i.select('div.time')[0].text.split(u'\xa0')[-1] + ':00'

                    thiscomment={
                        'content':comment_content,
                        'publish_user_photo':comment_publish_user_photo,
                        'publish_user':comment_publish_user,
                        'publish_user_id':comment_publish_user_id,
                        'publish_time':comment_publish_time,
                        'ancestor_id':data['id'],
                        'parent_id':data['id'],
                    }
                    data['reply_nodes'].append(thiscomment)
            data['reply_count']=len(data['reply_nodes'])
            self.result_list.append(data)

        threadlist = []
        while self.global_status_num_index > 0 or self.comments_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
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
            # print 'deal result'
            # host = '192.168.6.187:9092,192.168.6.188:9092,192.168.6.229:9092,192.168.6.230:9092'
            # producer = Producer(hosts=host)
            # result_file = get_result_name(plantform_c='350gerentushuguan',plantform_e='360个人图书馆', date_time=data['publish_time'], urlOruid=data['url'],
            #                               newsidOrtid=data['id'],
            #                               datatype='news', full_data=data)
            #
            # producer.send(topic='1101_STREAM_SPIDER', value={'data': data}, key=result_file, updatetime=data['spider_time'])
            #
            # comsumer = Consumer('topic', host, 'll')
            # what = comsumer.poll()
            # for i in comsumer.poll():
            #     print i.topic
            # for i in what:
            #     # print i.topic,i.partition,i.offset,i.key,i.value
            #     topic = i.topic
            #     partition = i.partition
            #     offset = i.offset
            #     key = i.key
            #     value = i.value
            #     # datalist=enumerate(what)


                # Save_result(plantform='xilu', date_time=data['publish_time'], urlOruid=data['url'],
                #             newsidOrtid=data['id'],
                #             datatype='news', full_data=value['content'])
            # Save_result(plantform='360gerentushuguan', date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
            #             datatype='news', full_data=data)

            # host = '182.150.63.40'
            # port = '12308'
            # username = 'silence'
            # password = 'silence'

            # producer = Producer(hosts=host)
            # producer = RemoteProducer(host=host, port=port, username=username, password=password)
            result_file = get_result_name(plantform_e='360gerentushuguan', plantform_c='360个人图书馆', date_time=data['publish_time'],
                                          urlOruid=data['url'],
                                          newsidOrtid=data['id'],
                                          datatype='news', full_data=data)
            print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'--------',result_file



            save_data_to_mongodb(data={'data':data},item_id=result_file,platform_e='360gerentushuguan',platform_c='360个人图书馆',cache_data_list=self.cache_data_list)

            # producer.send(topic='1101_STREAM_SPIDER', value={'data': data}, key=result_file,
            #               updatetime=data['spider_time'])

        threadlist = []
        while self.global_status_num_comments > 0 or self.result_list:
            while self.result_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.result_list:
                    # print len(self.result_list)
                    data_in_while = self.result_list.pop()
                    thread_in_while = threading.Thread(target=save_result, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
                    # print len(threadlist)
                    # print len(self.result_list)
        self.global_status_num_comments = 0

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
        pass


        time.sleep(1800)
        while True:
            if thread1.is_alive():
                time.sleep(10)
            else:
                time.sleep(10)
                thread1.run()



if __name__ == '__main__':
    thisclass=gerentushuguan360()

    thisclass.run()