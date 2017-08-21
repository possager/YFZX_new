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
from datetime import datetime,timedelta

class thepaper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        }
        self.urls = [
            'http://m.thepaper.cn/channel_26916',#视频，单独搞，因为视频模块的网页码不一样
            # 'http://m.thepaper.cn/channel_25950',  # 时事
            # 'http://m.thepaper.cn/channel_25951',#财经
            # 'http://m.thepaper.cn/channel_25952',#思想
            # 'http://m.thepaper.cn/channel_25953',#生活
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
            if 'http://m.thepaper.cn/channel_26916' in url:
                nexturl = 'http://www.thepaper.cn/load_index.jsp?' + url_in_content#发现手机端的数据获得地更多一些,电脑端http://m.thepaper.cn/load_channel.jsp?
            # nexturl='http://www.thepaper.cn/load_index.jsp?nodeids='+url_in_content
            # 'http://www.thepaper.cn/load_index.jsp?nodeids='桌面版的
            else:
                nexturl='http://m.thepaper.cn/load_channel.jsp?'+url_in_content

            thisurls_list.append(nexturl)
        for url_to_visit in thisurls_list:
            for i in range(50):
                self.index_url_list.append(url_to_visit+str(i))


        def get_index_inside_movie(url):
            response2=get_response_and_text(url=url)
            response_in_function=response2['response_in_function']
            response_in_function_text=response2['response_in_function_text']
            if len(response_in_function_text)<10:
                return
            datasoup=BeautifulSoup(response_in_function_text,'lxml')
            for one_url in datasoup.select('body > div'):
                thisurl=one_url.select('h2 > a')[0].get('href')
                publish_user=one_url.select('a')[2].text
                title=one_url.select('a')[1].text
                try:
                    publish_time=one_url.select('a > span')[0].text
                except:
                    publish_time='00:00:00'#这些网页的格式不规则
                try:
                    publish_time_date=one_url.select('span')[1].text
                    if u'天前' in publish_time_date:
                        publish_time_date=publish_time_date.replace(u'天前','')
                        date_now=datetime.now()
                        date_now2=date_now-timedelta(days=int(publish_time_date))
                        publish_time_date=date_now2
                        publish_time_date=str(publish_time_date.strftime('%Y-%m-%d %H-%M'))
                except Exception as e:
                    print e
                    try:
                        publish_time_date=one_url.select('span')[0].text
                    except Exception as e:
                        print e,'两次都没有找到publish_time_data，在index视频处理部分'
                    try:
                        if len(one_url.select('span')[0].text)==10:
                            publish_time_date=one_url.select('span')[0].text
                        else:
                            continue
                    except:
                        continue
                publish_time=publish_time_date+' '+publish_time+':00'
                id=one_url.select('h2 > a')[0].get('id')
                try:
                    reply_count= one_url.select('span.trbszan')[0].text
                    if 'k' in reply_count:
                        reply_count=float(reply_count)*1000
                except:
                    reply_count= 0

                data_index={
                    'url':'http://m.thepaper.cn/'+thisurl,
                    'publish_user':publish_user,
                    'title':title,
                    'publish_time':publish_time,
                    'id':id,
                    'reply_count':reply_count,
                    'is_movie':True
                }
                self.content_data_list.append(data_index)

        def get_index_inside_wenben(url):
            user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
            headers = {
                'User-Agent': user_agent
            }
            response1 = get_response_and_text(url=url,headers=headers)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            datasoup = BeautifulSoup(response_in_function_text, 'lxml')
            for div_content in datasoup.select('body > div'):
                try:
                    url= 'http://m.thepaper.cn/' + div_content.select('div > a')[0].get('href')  # url
                    publish_time = div_content.select('p > span')[0].text  # publish_time

                    title= div_content.select('div > p > a')[1].text  # title
                    publish_user= div_content.select('div > p > a')[0].text  # publish_user
                    # print div_content
                    if u'分钟' in publish_time:
                        minulate = publish_time.replace(u'分钟前', '')
                        time_b = datetime.now() - timedelta(minutes=int(minulate))
                        print time_b
                        time_c = time_b.strftime('%Y-%m-%d %H:%M')
                        publish_time= time_c
                    elif u'小时前' in publish_time:
                        hourse = publish_time.replace(u'小时前', '')
                        time_b = datetime.now() - timedelta(hours=int(hourse))
                        time_c = time_b.strftime('%Y-%m-%d %H:%M')
                        publish_time= time_c
                    elif u'天前' in publish_time:
                        days = publish_time.replace(u'天前', '')
                        time_b = datetime.now() - timedelta(days=int(days))
                        time_c = time_b.strftime('%Y-%m-%d %H:%M')
                        publish_time= time_c

                    print '\n\n\n'
                except Exception as e:
                    print e
                this_dict={
                    'url':url,
                    'publish_time':publish_time,
                    'title':title,
                    'publish_user':publish_user,
                    'is_movie':False
                }
                self.content_data_list.append(this_dict)



        threadlist=[]
        while self.index_url_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
            while self.index_url_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.index_url_list:
                    data_in_while = self.index_url_list.pop()
                    if 'http://www.thepaper.cn/load_index.jsp?' in data_in_while:
                        thread_in_while = threading.Thread(target=get_index_inside_movie, args=(data_in_while,))
                    else:
                        thread_in_while=threading.Thread(target=get_index_inside_wenben,args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)

        self.global_status_num_index=0


    def get_content(self):
        def get_content_inside(data):
            print 'in deal content'
            def get_content_inside_movie(data):
                url_for_debug=data['url']
                response1=get_response_and_text(url=url_for_debug)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                datasoup=BeautifulSoup(response_in_function_text,'lxml')
                Re_find_content = re.compile(r'desc: \'(.*)\'')
                content_data=Re_find_content.findall(response_in_function_text)
                content= content_data[0]
                # publish_time= datasoup.select('#v3cont_id > div.news_content > div:nth-of-type(3)')[0][0:16]
                data['content']=content
                self.comments_url_list.append(data)

            def get_content_inside_no_movie(data):
                url_for_debug=data['url']
                respons1=get_response_and_text(url=url_for_debug)
                response_in_function=respons1['response_in_function']
                response_in_function_text=respons1['response_in_function_text']


                Re_find_img=re.compile(r'src=".*?"')
                datasoup=BeautifulSoup(response_in_function_text,'lxml')
                content=''
                img_urls=[]
                for content_in_soup in datasoup.select('#v3cont_id > div.news_content > div.news_part'):
                    content+=content_in_soup.text
                title=datasoup.select('#v3cont_id > div.news_content > h1')[0].text
                publish_user= datasoup.select('#v3cont_id > div.news_content > p.about_news')[0].text
                publish_time= datasoup.select('#v3cont_id > div.news_content > p.about_news')[1].text
                datasoup_content=datasoup.select('#v3cont_id > div.news_content > div.news_part')[0]
                img_urls_original=Re_find_img.findall(str(datasoup_content))
                img_urls_selected_by_doup=datasoup_content.select('img')
                for url in img_urls_selected_by_doup:
                    print url.get('src')

                for url in img_urls_original:
                    url_split=url.split('"')[1]
                    img_urls.append(url_split)

                data['publish_user']=publish_user
                data['img_urls']=img_urls
                data['content']=content
                data['publish_user']=publish_user
                data['publish_time']=publish_time
                data['title']=title

                self.comments_url_list.append(data)



            if data['is_movie']:
                get_content_inside_movie(data)
            else:
                get_content_inside_no_movie(data)



        threadlist=[]
        while self.content_data_list or self.global_status_num_index:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
            while self.content_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.content_data_list:
                    data_in_while = self.content_data_list.pop()
                    print data_in_while
                    thread_in_while = threading.Thread(target=get_content_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)

    def get_comments(self):
        def get_comment_inside(data,isFirst_req=True,start_id=None,comments_list=[]):#这种写法可能有问题
            if isFirst_req==True:
                comment_req='http://www.thepaper.cn/load_moreFloorComment.jsp?contid='+data['id']
            else:
                comment_req='http://www.thepaper.cn/load_moreFloorComment.jsp?contid='+data['id']+'&startId='+start_id
            response1=get_response_and_text(url=comment_req)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            Re_find_startid = re.compile(r'startId="(.*?)"')
            data_re = Re_find_startid.findall(response1.text)
            start_id=data_re[0]
            datasoup=BeautifulSoup(response_in_function_text,'lxml')
            for one_div in datasoup.select('div'):
                publish_user_photo=one_div.select('div.aqwleft > div > a > img')
                publish_user=one_div.select('div.aqwright > h3 > a')
                id=one_div.select('div.aqwright > h3 > a')[0].split('commentId=')[1]
                publish_user_id=one_div.select('div.aqwright > h3 > a')[0].split('userId=')[1].split('&')[0]
                publish_time=one_div.select('div.aqwright > h3 > span')[0].text
                content=one_div.select('div.aqwright > div.floor_content > div > h3 > span')[0].text
                reply_count=one_div.select('div.aqwright > div.ansright_cont > a')[0].text

                if '小时前' in publish_time:
                    publish_time_num=int(publish_time.replace('小时前',''))
                    publish_time=(datetime.now()-timedelta(hours=publish_time_num)).strftime('%Y-%m-%d %H:%M:%S')
                elif '天前' in publish_time:
                    publish_time_num=int(publish_time.replace('天前',''))
                    publish_time=(datetime.now()-timedelta(days=publish_time_num)).strftime('%Y-%m-%d %H:%M:%S')
                else:
                    publish_time=publish_time


                thisdata={
                    'publish_user_photo':publish_user_photo,
                    'publish_user':publish_user,
                    'id':id,
                    'publish_user_id':publish_user_id,
                    'publish_time':publish_time,
                    'content':content,
                    'reply_count':reply_count
                }
                comments_list.append(thisdata)

            if int(start_id)==0:
                data['reply_node']=comments_list
                data['reply_count']=len(comments_list)
            else:
                get_comment_inside(data,isFirst_req=False,start_id=start_id,comments_list=comments_list)




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
        # time.sleep(10)
        thread2 = threading.Thread(target=self.get_content, args=())
        thread2.start()
        # time.sleep(3)
        # thread3 = threading.Thread(target=self.get_comments, args=())
        # thread3.start()
        # thread4 = threading.Thread(target=self.save_result, args=())
        # thread4.start()
        # pass

if __name__ == '__main__':
    thisclass=thepaper()
    # thisclass.get_Index()
    thisclass.run()