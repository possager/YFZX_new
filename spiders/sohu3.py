#_*_coding:utf-8_*_


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
from multiprocessing import process
from setting import CONTENT_THREADING_NUM
from setting import COMMENTS_THREADING_NUM
from saveresult import Save_result
import re
import logging
# from visit_page import get_response_and_text
import datetime



# from visit_page2 import get_response_and_text
# from visit_page3 import get_response_and_text
from sava_data_to_MongoDB import save_data_to_mongodb
from sava_data_to_MongoDB import save_data_to_mongodb_without_full
# from KafkaConnector1 import Producer,Consumer
from KafkaConnector import RemoteProducer,Consumer
from saveresult import get_result_name
import Queue
# from visit_page4 import get_response_and_text
from visit_page3 import get_response_and_text

class sohu:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Host': 'v2.sohu.com',
            'Proxy-Connection': 'closed',
        }
        self.urls = [
            'http://v2.sohu.com/public-api/feed?scene=CHANNEL&sceneId=8&page=',#1&size=20
            # 'https://api.m.sohu.com/autonews/cpool/?n=%E6%96%B0%E9%97%BB&s='#0&c=20&dc=1#这里边貌似都是汽车新闻
        ]
        #https://v2.sohu.com/public-api/articles/pv?articleIds=165322282,165273199,165318164,165298110,165305002,165320082,165305781,165276842,165322275,165319473,165314176,165319328,165319326,165318177,165317519,165319091,165262411,165318821,165315981,165270688
        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容


        self.global_status_finish=5
        self.cache_data_list=Queue.Queue()

    def get_Index(self):
        url_to_get_index1=self.urls[0]
        for i in range(1,300):
            response1=get_response_and_text(url=url_to_get_index1+str(i)+'&size=20',headers=self.headers)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            try:
                datajson=json.loads(response_in_function_text)
            except Exception as e:
                e
                pass
                continue
            this_url_index_list=[]#专为获取评论浏览数量而设计
            for i in datajson:
                try:
                    url_index='https://m.sohu.com/a/'+str(i['id'])+'_'+str(i['authorId'])
                except Exception as e:
                    # print e
                    pass
                try:
                    publish_time=i['publicTime']
                except Exception as e:
                    e
                    pass
                    continue
                publish_time = int(publish_time) / 1000
                time_format = '%Y-%m-%d %H:%M:%S'
                publish_time_stamp_9 = time.localtime(float(publish_time))
                publish_time = time.strftime(time_format, publish_time_stamp_9)
                data_index={
                    'publish_user':i['authorName'],
                    'title':i['title'],
                    'publish_time':publish_time,
                    'id':i['id'],
                    'url':url_index,
                    'cmsid':i['cmsId'],
                    'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                         }
                this_url_index_list.append(data_index)
                # self.content_data_list.append(data_index)#因为获得浏览量是单独的一个请求，所以
                # break
            viewernum_url='https://v2.sohu.com/public-api/articles/pv?articleIds='
            for viewernum_id in this_url_index_list:
                viewernum_url=viewernum_url+','+str(viewernum_id['id'])
            viewernum_url=viewernum_url.replace('articleIds=,','articleIds=')
            while True:
                try:
                    viewernum_info=requests.get(url=viewernum_url,headers=self.headers)
                    break
                except Exception as e:
                    print e
            viewernum_info_json=json.loads(viewernum_info.text)
            data_index_list_temp=[]#8-22日临时添加
            for data_index_no_viewer in this_url_index_list:
                noviewer_id=data_index_no_viewer['id']
                # print noviewer_id
                data_index_no_viewer['read_count']=viewernum_info_json['%s' %(str(noviewer_id))]#这里逻辑错误，从列表里边取出来的那个不是原来的那个，而是新的那个。
                #8-23日添加
                data_index_list_temp.append(data_index_no_viewer)#把结果存起来


            self.content_data_list=self.content_data_list+data_index_list_temp




            # break
            time.sleep(1)

        while True:
            self.global_status_num_index=0
            time.sleep(3)
            if self.global_status_num_result==0:
                break



    def get_content(self):

        def get_content_inside(data):
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
                }
                url_for_debug=data['url']
                response1=get_response_and_text(url=url_for_debug,headers=headers)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']



                img_urls=[]
                content=''
                datasoup=BeautifulSoup(response_in_function_text,'lxml')
                if datasoup.select('#articleContent > div.display-content > p'):
                    for i in datasoup.select('#articleContent > div.display-content > p'):
                        content+= i.text
                else:
                    for i in datasoup.select('#articleContent > div.display-content'):
                        content+=i.text

                try:
                    content_data=str(datasoup.select('#articleContent')[0])
                except Exception as e:
                    # print e
                    try:
                        content_data=str(datasoup.select('#articleContent')[0])
                    except:
                        return
                Re_find_img=re.compile(r'src=".*?"')
                imgs_find_by_re=Re_find_img.findall(content_data)
                for img_url in imgs_find_by_re:
                    img_url=img_url.split('"')[1]
                    if 'http' not in img_url:
                        img_url='https:'+img_url
                    img_urls.append(img_url)
                data['content']=content
                data['img_urls']=img_urls
                data['reply_nodes']=[]
                data['spider_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                self.comments_url_list.append(data)
            except Exception as e:
                print e




        threadlist=[]
        while self.global_status_num_index > 0 or self.content_data_list:  # 如果index中的任务完了,content_url_list中是空的的时候，就停止
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
            self.global_status_num_content = 0
            time.sleep(5)
            if self.global_status_num_content==0:
                break

    def get_comments(self):
        def get_comment_inside(data):#这里的下一页请求只需要在cmspagenum上加1即可。
            #初始化
            topicid=None
            cmspage_taotalnum=0
            comments_data = []
            cmspagenum = 1
            while True:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
                }
                if not topicid:
                    comment_url = 'https://apiv2.sohu.com/api/topic/load?page_size=10&topic_source_id=' + \
                              str(data['cmsid'])+'&page_no=1'
                else:
                    comment_url='https://apiv2.sohu.com/api/comment/list?page_size=10&topic_id='+str(topicid)+'&page_no='+str(cmspagenum)
                response1=get_response_and_text(url=comment_url,headers=headers)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                try:
                    data_json = json.loads(response_in_function_text)
                except Exception as e:
                    print e

                if cmspagenum==1:
                    try:
                        cmspage_taotalnum=data_json['jsonObject']['cmt_sum']
                        data['reply_count'] = cmspage_taotalnum
                    except:
                        try:
                            cmspage_taotalnum=data_json['jsonObject']['outer_cmt_sum']
                        except:
                            cmspage_taotalnum=0#因为这里边没有返回这个值
                            return
                for one_comment in data_json['jsonObject']['comments']:
                    id=one_comment['comment_id']
                    content=one_comment['content']
                    url=response_in_function.url
                    publish_time=one_comment['create_time']
                    publish_time = int(publish_time) / 1000
                    time_format = '%Y-%m-%d %H:%M:%S'
                    publish_time_stamp_9 = time.localtime(float(publish_time))
                    publish_time = time.strftime(time_format, publish_time_stamp_9)
                    publish_user_id=one_comment['user_id']
                    like_count=one_comment['support_count']
                    reply_count=one_comment['reply_count']
                    try:
                        publish_user=one_comment['passport']['nickname']
                    except Exception as e:
                        # publish_user='没有抓到这个人的昵称，也没有调试出来为什么'
                        publish_user=''
                    publish_user_photo=one_comment['passport']['img_url']
                    ancestor_id=data['id']
                    # print ancestor_id,'---------',data['id']
                    # print '---------------------',id,'----------------------'
                    # if ancestor_id!=data['id']:
                    #     print ancestor_id,'---------',data['id']
                    parent_id=data['id']
                    if one_comment['comments']:
                        parent_id=one_comment['comments'][0]['comment_id']


                    thisnode={
                        'id':id,
                        'content':content,
                        'url':url,
                        'publish_time':publish_time,
                        'publish_user_id':publish_user_id,
                        'like_count':like_count,
                        'reply_count':reply_count,
                        'publish_user':publish_user,
                        'publish_user_photo':publish_user_photo,
                        'ancestor_id':ancestor_id,
                        'parent_id':parent_id
                    }


                    comments_data.append(thisnode)
                cmspagenum+=1
                if cmspagenum<=int(cmspage_taotalnum/10)+1:#既然每次10条结果，那么
                    if not topicid:
                        topicid=data_json['jsonObject']['topic_id']
                    # get_comment_inside(data,cmspagenum,comments_data,topicid,cmspage_taotalnum)
                else:

                    count_result={}
                    for parent_to_count_parentid in comments_data:
                        if str(parent_to_count_parentid['parent_id']) not in count_result.keys():
                            count_result[str(parent_to_count_parentid['parent_id'])]=0
                        else:
                            count_result[str(parent_to_count_parentid['parent_id'])]+=1

                    comments_data2=[]
                    for parent_to_count_parentid2 in comments_data:
                        if str(parent_to_count_parentid2['parent_id']) in count_result.keys():
                            parent_to_count_parentid2['reply_count']=count_result[str(parent_to_count_parentid2['parent_id'])]
                        comments_data2.append(parent_to_count_parentid2)



                    data['reply_nodes']=comments_data2
                    del data['cmsid']#删除为获取评论而生成的id

                    #统计relpy_count这个值,统计parent_id的出现次数，那么8-23日
                    # parent_id_list=[]
                    # for comment_to_count_parent_id in data['reply_nodes']:
                    #     parent_id_list.append(comment_to_count_parent_id['parent_id'])


                    self.result_list.append(data)
                    break






        threadlist = []
        while self.global_status_num_content > 0 or self.comments_url_list:  # content没有完，就别想完，
            while self.comments_url_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.comments_url_list:
                    data_in_while = self.comments_url_list.pop()
                    thread_in_while = threading.Thread(target=get_comment_inside, args=(data_in_while,))
                    # thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    # thread_in_while.join(timeout=600)
                    threadlist.append(thread_in_while)
                for childthread in threadlist:
                    childthread.join(600)
        while True:
            self.global_status_num_comments = 0
            time.sleep(5)
            if self.global_status_num_comments==0:
                break

    def save_result(self):
        def save_result(data):


            result_file = get_result_name(plantform_e='sohu',plantform_c='搜狐新闻', date_time=data['publish_time'], urlOruid=data['url'],
                                          newsidOrtid=data['id'],
                                          datatype='news', full_data=data)
            print datetime.datetime.now(),'--------',result_file

            save_data_to_mongodb(data={'data':data},item_id=result_file,platform_e='sohu',platform_c='搜狐新闻',cache_data_list=self.cache_data_list)


        threadlist = []
        while self.global_status_num_comments > 0 or self.result_list:
            while self.result_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.result_list:
                    data_in_while = self.result_list.pop()
                    thread_in_while = threading.Thread(target=save_result, args=(data_in_while,))
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
                for childthread in threadlist:
                    childthread.join(600)

        # self.global_status_num_comments = 0
        while True:
            self.global_status_finish=0
            self.global_status_num_result=0
            time.sleep(5)
            if self.global_status_finish==0:
                break





    def run(self):
        thread1=threading.Thread(target=self.get_Index,args=())
        thread1.start()
        time.sleep(5)
        thread2=threading.Thread(target=self.get_content,args=())
        thread2.start()
        # time.sleep(3)
        thread3=threading.Thread(target=self.get_comments,args=())
        thread3.start()
        thread4=threading.Thread(target=self.save_result,args=())
        thread4.start()
        pass

        thread1.join(2*60*60)
        thread2.join(2*60*60)
        thread3.join(2*60*60)
        thread4.join(2*60*60)

        self.global_status_finish=0

        while self.global_status_num_content!=0:
            print 'index没有获取完'
            print '--------the global status num content--',self.global_status_num_content
            print '------the global status num comment--',self.global_status_num_comments
            print '----the global status num result--',self.global_status_num_result
            print '--the global status finish--',self.global_status_finish
            print '========len of content========',len(self.content_data_list)
            time.sleep(2)

        while self.global_status_num_comments!=0:
            print 'content没有获取完'
            print '--------the global status num content--',self.global_status_num_content
            print '------the global status num comment--',self.global_status_num_comments
            print '----the global status num result--',self.global_status_num_result
            print '--the global status finish--',self.global_status_finish
            print '=======len of comment========',len(self.comments_url_list)
            time.sleep(2)





        self.global_status_finish=0

        save_data_to_mongodb_without_full(cache_data_list=self.cache_data_list)

        print '执行完了'

if __name__ == '__main__':
    # thisclass=sohu()
    # thisclass.run()

    while True:
        runthrod=10
        thisclass=sohu()
        thisclass.run()
        while runthrod>1:
            while runthrod and thisclass.global_status_finish==5:
                runthrod=10
                time.sleep(6) # 因为在类里边实在是不好写定时启动任务了，所以写在这里。。。。。
            runthrod-=1
        print '正在等待着600秒'
        #后来增加的防时间等待模块
        time.sleep(600)