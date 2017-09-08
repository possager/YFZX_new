# _*_coding:utf-8_*_
import requests
import copy
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
from datetime import datetime,timedelta
from visit_page2 import get_response_and_text
from KafkaConnector import RemoteProducer,Consumer
from saveresult import get_result_name




class thepaper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        }
        self.urls = [
            'http://m.thepaper.cn/channel_26916',#视频，单独搞，因为视频模块的网页码不一样
            # 'http://m.thepaper.cn/channel_25950',  # 时事
            'http://m.thepaper.cn/channel_25951',#财经
            'http://m.thepaper.cn/channel_25952',#思想
            'http://m.thepaper.cn/channel_25953',#生活
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
            try:
                url_in_content = datare[0].split('"')[1]
            except Exception as e:
                print e
                continue
            if 'http://m.thepaper.cn/channel_26916' in url:
                nexturl = 'http://www.thepaper.cn/load_index.jsp?' + url_in_content#发现手机端的数据获得地更多一些,电脑端http://m.thepaper.cn/load_channel.jsp?
            else:
                nexturl='http://m.thepaper.cn/load_channel.jsp?'+url_in_content

            thisurls_list.append(nexturl)
        for url_to_visit in thisurls_list:
            for i in range(10):
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
                video_urls=[]
                try:
                    video_urls1=datasoup.select('video source')
                    for i in video_urls1:
                        video_urls.append(i.get('src'))
                except Exception as e:
                    print e

                data_index={
                    'url':'http://m.thepaper.cn/'+thisurl,
                    'publish_user':publish_user,
                    'title':title,
                    'publish_time':publish_time,
                    'id':id,
                    'reply_count':reply_count,
                    'is_movie':True,
                    'spider_time':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'video_urls':video_urls
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
                    try:
                        reply_count=div_content.select('span.reply')[0].text
                    except Exception as e:
                        print e
                        reply_count=0#因为有些新闻index请求中看不到评论消息。
                    url= 'http://m.thepaper.cn/' + div_content.select('div > a')[0].get('href')  # url
                    publish_time = div_content.select('p > span')[0].text  # publish_time
                    #这里需要对publish_time做处理吗？

                    title= div_content.select('div > p > a')[1].text  # title
                    publish_user= div_content.select('div > p > a')[0].text  # publish_user
                    # print div_content
                    if u'分钟' in publish_time:
                        minulate = publish_time.replace(u'分钟前', '')
                        time_b = datetime.now() - timedelta(minutes=int(minulate))
                        print time_b
                        time_c = time_b.strftime('%Y-%m-%d %H:%M:%S')
                        publish_time= time_c
                    elif u'小时前' in publish_time:
                        hourse = publish_time.replace(u'小时前', '')
                        time_b = datetime.now() - timedelta(hours=int(hourse))
                        time_c = time_b.strftime('%Y-%m-%d %H:%M:%S')
                        publish_time= time_c
                    elif u'天前' in publish_time:
                        days = publish_time.replace(u'天前', '')
                        time_b = datetime.now() - timedelta(days=int(days))
                        time_c = time_b.strftime('%Y-%m-%d %H:%M:%S')
                        publish_time= time_c

                    print '\n\n\n'
                except Exception as e:
                    print e
                id=url.split('_')[-1]
                this_dict={
                    'id':id,
                    'url':url,
                    'publish_time':publish_time,
                    'title':title,
                    'publish_user':publish_user,
                    'is_movie':False,
                    'reply_count':reply_count,
                    'spider_time':datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                self.content_data_list.append(this_dict)



        threadlist=[]
        # self.index_url_list=self.index_url_list.reverse()
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
                #8-30
                like_count=datasoup.select('#news_praise')
                if like_count:
                    like_count_value=int(like_count[0].text.strip())
                else:
                    like_count_value=0

                vedio=datasoup.select('video > source')
                if vedio:
                    vedio_urls=[]
                    for vedio1 in vedio:
                        vedio_urls.append(vedio1.get('src'))
                else:
                    vedio_urls=[]
                #8-30


                try:
                    content= content_data[0]
                except Exception as e:
                    print e#这里有时候会报错说这里的content没有内容

                try:
                    source=datasoup.select('#v3cont_id > div.news_content > div > br')[0].text.split(u'来源：')[1]
                except:
                    source=''

                # publish_time= datasoup.select('#v3cont_id > div.news_content > div:nth-of-type(3)')[0][0:16]
                data['content']=content
                data['like_count']=like_count_value
                data['video_urls']=vedio_urls
                data['source']=source
                # read_count=datasoup.select('body > div.video_main.pad60.nav_container > div.video_bo > div > div.video_txt_l > div > div.video_info > span.reply')
                # data['read_count']=read_count[0].text
                self.comments_url_list.append(data)

            def get_content_inside_no_movie(data):
                url_for_debug=data['url']
                vedio_list=[]
                respons1=get_response_and_text(url=url_for_debug)
                response_in_function=respons1['response_in_function']
                response_in_function_text=respons1['response_in_function_text']
                Re_find_img=re.compile(r'src=".*?"')
                datasoup=BeautifulSoup(response_in_function_text,'lxml')
                content=''
                img_urls=[]
                for content_in_soup in datasoup.select('#v3cont_id > div.news_content > div.news_part'):
                    content+=content_in_soup.text
                try:
                    title=datasoup.select('#v3cont_id > div.news_content > h1')[0].text
                except:
                    print response_in_function.url
                    # title=''
                    return #这里偶尔会转到莫名其妙的网页
                try:
                    publish_user= datasoup.select('#v3cont_id > div.news_content > p.about_news')[0].text
                except Exception as e:
                    print e
                try:
                    source=datasoup.select('#v3cont_id > div.news_content > p.about_news')[1].text.split(u'来源：')[1]
                except:
                    source=''
                try:
                    publish_time=datasoup.select('.news_content .about_news')[1].text.split(u'\xa0')[0]+':00'
                    data['publish_time']=publish_time
                except Exception as e:
                    print e

                for i in datasoup.select('source'):
                    url_vedio= i.get('src')
                    vedio_list.append(url_vedio)

                # publish_time= datasoup.select('#v3cont_id > div.news_content > p.about_news')[1].text.strip()#还是有一个莫名奇妙的空格
                datasoup_content=datasoup.select('#v3cont_id > div.news_content > div.news_part')[0]
                img_urls_original=Re_find_img.findall(str(datasoup_content))
                img_urls_selected_by_doup=datasoup_content.select('img')
                for url in img_urls_selected_by_doup:
                    print url.get('src')
                for url in img_urls_original:
                    url_split=url.split('"')[1]
                    img_urls.append(url_split)
                # if len(publish_time)> 17:
                #     publish_time=publish_time.split('\n')[0]

                #8-30
                like_count = datasoup.select('#news_praise')
                if like_count:
                    like_count_value = int(like_count[0].text.strip())
                else:
                    like_count_value = 0
                #8-30

                data['like_count']=like_count_value
                data['publish_user']=publish_user
                data['img_urls']=img_urls
                data['content']=content
                data['publish_user']=publish_user
                # data['publish_time']=publish_time
                data['title']=title
                data['source']=source
                data['video_urls'] = vedio_list
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
        def get_comment_inside(data):#这种写法可能有问题
            data['source']=data['source'].strip()
            isFirst_req = True
            start_id = 0
            comments_list = []
            while True:
                if isFirst_req==True:
                    comment_req='http://www.thepaper.cn/load_moreFloorComment.jsp?contid='+data['id']
                else:
                    comment_req='http://www.thepaper.cn/load_moreFloorComment.jsp?contid='+data['id']+'&startId='+start_id
                headers={
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
                }
                response1=get_response_and_text(url=comment_req,headers=headers)
                response_in_function=response1['response_in_function']
                response_in_function_text=response1['response_in_function_text']
                Re_find_startid = re.compile(r'startId="(.*?)"')
                data_re = Re_find_startid.findall(response_in_function_text)

                start_id=0#8-24日添加
                try:
                    start_id=data_re[0]
                except Exception as e:
                    print e
                datasoup=BeautifulSoup(response_in_function_text,'lxml')
                for one_div in datasoup.select('div.comment_que'):
                    #手机端和电脑端的显示页面不一样，需要分别处理。
                    try:
                        publish_user_photo=one_div.select('div.aqwleft > div > a > img')[0].get('src')
                    except Exception as e:
                        print e
                        publish_user_photo='http://www.thepaper.cn/img/headerimg_bg50.png'#可能没有，先舍弃了，后边有问题再回来检擦 mark1
                    publish_user=one_div.select('div.aqwright > h3 > a')[0].text
                    try:
                        id_1=str(one_div.select('div.aqwright > h3 > a')[0]).split('commentId=')
                        # id=one_div.select('div.aqwright > h3 > a')[0].split('commentId=')[1]
                        id=id_1[1].split('"')[0]
                    except Exception as e:
                        print e
                    publish_user_id=str(one_div.select('div.aqwright > h3 > a')[0]).split('userId=')[1].split('&')[0]
                    publish_time=one_div.select('div.aqwright > h3 > span')[0].text
                    content=''
                    for content_in_for in one_div.select('div > a[href^="javascript:replyFloor"]'):#有问题
                        if u'回复' not in content_in_for:
                            content+=content_in_for.text
                    # content=content.replace(u'回复',u'')
                    try:
                        like_count=int(one_div.select('div.aqwright > div.ansright_time > a[href^="javascript:priseCommtFloor"]')[0].text)
                    except:
                        like_count=0


                    if u'小时前' in publish_time:
                        publish_time_num=int(publish_time.replace(u'小时前',''))
                        publish_time=(datetime.now()-timedelta(hours=publish_time_num)).strftime('%Y-%m-%d %H:%M:%S')
                    elif u'天前' in publish_time:
                        publish_time_num=int(publish_time.replace(u'天前',''))
                        publish_time=(datetime.now()-timedelta(days=publish_time_num)).strftime('%Y-%m-%d %H:%M:%S')
                    elif u'分钟前' in publish_time:
                        publish_time_num=int(publish_time.replace(u'分钟前',''))
                        publish_time=(datetime.now()-timedelta(minutes=publish_time_num)).strftime('%Y-%m-%d %H:%M:%S')
                    else:
                        publish_time=publish_time

                    #8-25日添加parentid处理模块
                    Re_find_publish_user = re.compile(ur'回复@(.*)\:')
                    has_at_re=Re_find_publish_user.match(content)
                    has_at=''
                    if has_at_re:
                        has_at=has_at_re.group(1)
                    thisdata={
                        'publish_user_photo':publish_user_photo,
                        'publish_user':publish_user,
                        'id':id,
                        'publish_user_id':publish_user_id,
                        'publish_time':publish_time,
                        'content':content,
                        'like_count':like_count,
                        'ancestor_id':data['id'],
                        'parent_id':data['id'],#这一个暂且这么设计，之后统计content里边有没有@到的人，之后再做统计
                        # 'reply_nodes':[],
                        # 'has_at':has_at
                    }
                    comments_list.append(thisdata)

                if int(start_id)==0:
                    #8-25添加parent_id处理功能
                    # comments_list2=comments_list[:]
                    # for comment_one_data in comments_list2:
                    #     if comment_one_data['has_at']:
                    #         def merge_comment(comment_one_data):
                    #             #有@，就根据@后的人名来统计parent_id
                    #             for num in range(len(comments_list2)):
                    #                 if comments_list2[num]['publish_user']==comment_one_data['publish_user']:
                    #                     _=copy.deepcopy(comment_one_data)
                    #                     del(comment_one_data['has_at'])
                    #                     comments_list2[num]['reply_nodes'].append(comment_one_data)
                    #                     comments_list2.remove(_)#这样结构依然不完整
                    #                     if comments_list2[num]['has_at']:#这里注意顺序！！！！python语法就是list都是调用不是开辟新的空间
                    #                         new_child_comment=copy.deepcopy(comments_list2[num])


                    data['reply_nodes']=comments_list
                    data['reply_count']=len(comments_list)
                    try:
                        data['publish_time']=data['publish_time'].replace(u' ',u'').encode('utf-8')
                        data['publish_time']=data['publish_time'].split(' ')[0]+' '+data['publish_time'].split(' ')[1]
                    except Exception as e:
                        print e
                    self.result_list.append(data)
                    break
                else:
                    get_comment_inside(data)




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

    def save_result(self):
        def save_result(data):
            # print 'deal result'
            try:
                del data['is_movie']
            except Exception as e:
                print e
            host = '182.150.63.40'
            port = '12308'
            username = 'silence'
            password = 'silence'

            # producer = Producer(hosts=host)
            producer = RemoteProducer(host=host, port=port, username=username, password=password)
            result_file = get_result_name(plantform_e='PengPai', plantform_c='澎湃新闻', date_time=data['publish_time'],
                                          urlOruid=data['url'],
                                          newsidOrtid=data['id'],
                                          datatype='news', full_data=data)

            producer.send(topic='1101_STREAM_SPIDER', value={'data': data}, key=result_file,
                          updatetime=data['spider_time'])

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
        thread1 = threading.Thread(target=self.get_Index, args=())
        thread1.start()
        # time.sleep(10)
        thread2 = threading.Thread(target=self.get_content, args=())
        thread2.start()
        # time.sleep(3)
        thread3 = threading.Thread(target=self.get_comments, args=())
        thread3.start()
        thread4 = threading.Thread(target=self.save_result, args=())
        thread4.start()
        # pass

if __name__ == '__main__':
    thisclass=thepaper()
    # thisclass.get_Index()
    thisclass.run()