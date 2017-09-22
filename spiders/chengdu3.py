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
# from KafkaConnector1 import Producer,Consumer
# from visit_page2 import get_response_and_text
from visit_page3 import get_response_and_text
from KafkaConnector import RemoteProducer,Consumer
import sqlite3
from sava_data_to_MongoDB import save_data_to_mongodb


class chengdu:
    #这个模式和xilu有点不一样
    #缺少一个停止条件，当满足停止条件是，应当一些参数设置成？


    def __init__(self):
        self.session1=requests.session()
        self.headers={
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
        # self.page_begain=1699990
        # self.urls=['http://wap.chengdu.cn/'+str(i) for i in range(self.page_begain,3000000)]#1696951
        self.urls=[]

        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4
        self.error_num_to_stop=100



        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容

    def get_Index(self):
        need_continue=True

        while True:
            try:
                response1=requests.get(url='http://wap.chengdu.cn/?action=category&catid=583',headers=self.headers)
                datasoup=BeautifulSoup(response1.text,'lxml')

                url_id_set = set()
                for i in datasoup.select('div.content.more ul li a'):
                    try:
                        url_id_set.add(int(i.get('href').split('contentid=')[1]))
                    except:
                        pass

                max_url_id= max(list(url_id_set))
                self.urls=['http://wap.chengdu.cn/'+str(i) for i in range(max_url_id-1000,max_url_id+1000)]

                while self.urls and need_continue:  # 设置成and为了方便停止
                    while len(self.content_data_list) > LEN_CONTENT_LIST:
                        time.sleep(1)
                    url = self.urls.pop(1)
                    self.content_data_list.append({'url': url, 'id': url.split('/')[-1]})
                    # break
                # self.global_status_num_index = 0
                time.sleep(300)
            except:
                pass



    def get_content(self):
        def get_content_inside(data):
            #这里不设计去重功能就真的没法停下来了
            #这里就写第一次的代码功能就行
            url = data['url']
            page_num=url.split('/')[-1]
            response1=get_response_and_text(url=url,needupdate=True,update_info={'page_num':page_num})
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            Re_find_sid=re.compile(r'sid=".*"')
            try:
                datasoup = BeautifulSoup(response_in_function_text, 'lxml')
            except Exception as e:
                print e
                return

            if ('class="swiper-container"' not in response_in_function_text) and ('class="content"' in response_in_function_text):#这个是文字类的新闻
                sid = Re_find_sid.findall(response_in_function_text)[0].split('"')[1]
                data['sid'] = sid

                datasoup = BeautifulSoup(response_in_function_text, 'lxml')
                for i in datasoup.select('body > div.content > div.neirong > h2'):
                    title= i.text
                for j in datasoup.select('body > div.content > div.neirong > p > span:nth-of-type(4)'):
                    publish_time= j.text
                for k in datasoup.select('body > div.content > div.neirong > p > span:nth-of-type(3)'):
                    publish_user= k.text.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r','').replace(u'来源：','')
                    break
                for publish_user_for in datasoup.select('body > div.content > p.jieshao > span:nth-of-type(3)'):
                    publish_user=publish_user_for.text
                    break
                # for publish_user_for in datasoup.select('body > div.content > p.jieshao > span:nth-child(3) > a')
                content = ''
                for l in datasoup.select('body > div.content > div.neirong > article > p'):
                    content+= l.text
                img_urls=[]
                neirong_content = datasoup.select('body > div.content > div.neirong')
                neirong_content = str(neirong_content)
                Re_find_img_url = re.compile(r'src=".*?"')
                img_find_by_re = Re_find_img_url.findall(neirong_content)
                for i in img_find_by_re:
                    img_urls.append(i.split('"')[1])
                try:
                    publish_time+=':00'
                except Exception as e:
                    print e
                data['title']=title
                data['content']=content
                data['publish_time']=publish_time
                data['publish_user']=publish_user
                data['reply_nodes']=[]
                data['spider_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                data['img_urls']=img_urls
            elif 'class="swiper-container"' in response_in_function_text:#这里可能是图片新闻
                content=''
                img_urls=[]
                for title_for in datasoup.select('body > div.content > h2'):
                    title= title_for.text
                for publish_time_for in datasoup.select('body > div.content > p.jieshao > span:nth-of-type(4)'):
                    publish_time= publish_time_for.text+':00'
                for publish_user_for in datasoup.select('body > div.content > p.jieshao > span:nth-of-type(3) > a'):
                    publish_user= publish_user_for.text.replace(' ', '').replace('\t', '').replace('\n', '').replace('\r','').replace(u'来源：','')
                    break
                for publish_user_for in datasoup.select('body > div.content > p.jieshao > span:nth-of-type(3)'):
                    publish_user=publish_user_for.text
                    break
                for content_for in datasoup.select('body > div.content > p.zongjie'):
                    content+= content_for.text
                for img_url in datasoup.select(
                        'div.swiper-container > div.swiper-wrapper > div.swiper-slide > div.imgdiv > img'):
                    img_urls.append(img_url.get('src'))
                try:
                    data['title'] = title
                    data['content'] = content
                    data['publish_time'] = publish_time
                    data['publish_user'] = publish_user
                    data['reply_nodes'] = []
                    data['spider_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    data['img_urls']=img_urls
                except Exception as e:
                    print e
                    return

            else:
                print url,'-----not in neirong and picture deal module'
                return

            while len(self.comments_url_list) > LEN_COMMENT_LIST:
                time.sleep(1)
            # print data
            self.comments_url_list.append(data)
            pass




        threadlist=[]
        while self.global_status_num_index>0 or self.content_data_list:
            while self.content_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist)<CONTENT_THREADING_NUM and self.content_data_list:
                    data_in_while = self.content_data_list.pop()
                    thread_in_while = threading.Thread(target=get_content_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)

        self.global_status_num_content=0

    def get_comments(self):
        def get_comment_inside(data):#也是分为两段设计，第一次获得contentid
            topicid = None
            cmspage_taotalnum = 1
            comments_data = []
            cmspagenum = 1


            #额外添加
            request_num=1
            error_time=5

            # comments_data=[]
            while True:
                # reply_count=0
                if not topicid:
                    comment_url_without_id='http://changyan.sohu.com/api/3/topic/liteload?&client_id=cyrHnxhFx&page_size=30&hot_size=5&topic_source_id='
                    try:
                        comment_url=comment_url_without_id+data['sid']
                    except Exception as e:
                        print e
                        break#图片类新闻没有评论
                else:
                    comment_url = 'http://changyan.sohu.com/api/2/topic/comments?client_id=cyrHnxhFx&page_size=30&topic_id=' + str(
                        topicid) + '&page_no=' + str(request_num)

                response1=get_response_and_text(url=comment_url)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                try:
                    data_json=json.loads(response_in_function_text)
                except Exception as e:
                    print e
                    # return
                    break
                try:
                    data_json['comments']
                except Exception as e:
                    print e
                    continue
                    error_time-=1
                    if error_time<1:
                        break
                if data_json['comments']:
                    data_json_comments = data_json['comments']
                    cmspage_taotalnum=data_json['cmt_sum']
                    topicid=data_json['topic_id']


                    for someone_comment in data_json_comments:
                        content = someone_comment['content']  # content
                        id = someone_comment['comment_id']  # id
                        publish_user_photo = someone_comment['passport']['img_url']  # publish_user_photo
                        try:
                            publish_user = someone_comment['passport']['nickname']  # publish_user
                        except Exception as e:
                            print e
                            publish_user=''
                        publish_user_id = someone_comment['passport']['user_id']  # publish_user_id
                        create_time = someone_comment['create_time']  # publish_time
                        create_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(int(create_time/1000))))
                        spider_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        like_count=someone_comment['support_count']
                        parent_id=data['id']#mark这两个节点到底应该放什么东西呢？
                        ancestor_id=data['id']
                        this_comments=someone_comment['comments']
                        if this_comments:
                            parent_id=this_comments[0]['comment_id']
                        #用堆来解决这种类型的评论8-16
                        # for this_comments
                        cmspagenum+=1





                        thiscomments = {
                            'content': content,
                            'id': id,
                            'publish_user_photo': publish_user_photo,
                            'publish_user': publish_user,
                            'publish_user_id': publish_user_id,
                            'publish_time': create_time,
                            'spider_time': spider_time,
                            'like_count':like_count,
                            'parent_id':parent_id,
                            'ancestor_id':ancestor_id,
                        }
                        comments_data.append(thiscomments)

                    if cmspagenum>=cmspage_taotalnum-1:
                        break

                request_num+=1
                if cmspagenum>cmspage_taotalnum/30:
                    break

            data['reply_nodes']=comments_data
            if not comments_data:
                data['reply_count']=0
            else:
                data['reply_count']=cmspage_taotalnum
            while len(self.result_list)>600:
                time.sleep(1)
                print 'is waiting the lenth of the result_list to decrease to 300'

            #最后处理，去掉不需要的字段：
            try:
                del data['sid']#图片类的新闻没有sid
            except :
                pass
            self.result_list.append(data)


        threadlist = []
        while self.global_status_num_content > 0 or self.comments_url_list:  # content没有完，就别想完，
            while self.comments_url_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < COMMENTS_THREADING_NUM and self.comments_url_list:
                    data_in_while = self.comments_url_list.pop()
                    thread_in_while = threading.Thread(target=get_comment_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
        self.global_status_num_comments = 0

    def save_result(self):
        def save_result(data):
            # print 'deal result'
            try:#因为有些页面有时候会解析错误，导致没有正确的内容，自然也没有publishtime这个属性，所以直接可以用try模块来过滤掉那些没有抓全的数据。

                # host = '192.168.6.187:9092,192.168.6.188:9092,192.168.6.229:9092,192.168.6.230:9092'
                # host='182.150.63.40'
                # port='12308'
                # username='silence'
                # password='silence'
                #
                # producer=RemoteProducer(host=host,port=port,username=username,password=password)
                result_file=get_result_name(plantform_e='ChengDuQuanSouSuo',plantform_c='成都全搜索',date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
                        datatype='news', full_data=data)

                print datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'--------', result_file


                save_data_to_mongodb(data={'data':data},item_id=result_file,platform_e='ChengDuQuanSouSuo',platform_c='成都全搜索')

                # producer.send(topic='1101_STREAM_SPIDER',value={'data':data},key=result_file,updatetime=data['spider_time'])

                # comsumer=Consumer('topic', host, 'll')
                # what=comsumer.poll()
                # for i in comsumer.poll():
                #     print i.topic
                # for i in what:
                #     # print i.topic,i.partition,i.offset,i.key,i.value
                #     topic=i.topic
                #     partition=i.partition
                #     offset=i.offset
                #     key=i.key
                #     value=i.value
                # datalist=enumerate(what)
                #
                #
                #     Save_result(plantform='chengdu', date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
                #             datatype='news', full_data=value['content'])
            except Exception as e:
                print e

        threadlist = []
        while self.global_status_num_comments > 0 or self.result_list:
            while self.result_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < CONTENT_THREADING_NUM and self.result_list:
                    data_in_while = self.result_list.pop()
                    thread_in_while = threading.Thread(target=save_result, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
        self.global_status_num_comments = 0

    def get_schedule(self,isread=None,iswrite=None,sechdule_new=None):
        file1=BASIC_FILE+'/chengdu/chengdu_sechdule.text'
        sechdule=1696951
        if isread:
            try:
                with open(file1) as fl:
                    sechdule=int(fl.read())
            except:
                pass
            return sechdule
        elif iswrite:
            with open(file1) as fl:
                fl.write(str(sechdule_new))
        else:
            print 'what do you want to do? read or write?'




    def run(self):

        self.page_begain=self.get_schedule(isread=True)

        self.urls=['http://wap.chengdu.cn/'+str(i) for i in range(int(self.page_begain),3000000)]#1696951

        thread1 = threading.Thread(target=self.get_Index, args=())
        thread1.start()
        time.sleep(5)#有必要设置一个延时
        thread2 = threading.Thread(target=self.get_content, args=())
        thread2.start()
        time.sleep(3)
        thread3 = threading.Thread(target=self.get_comments, args=())
        thread3.start()
        thread4 = threading.Thread(target=self.save_result, args=())
        thread4.start()
        pass

if __name__ == '__main__':
    thisclass=chengdu()
    thisclass.run()
