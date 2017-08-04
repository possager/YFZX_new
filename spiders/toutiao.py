#_*_coding:utf-8_*_
import cookielib
import threading
import requests
from proxy_to_redis import *
from multiprocessing import process
from setting import *
from bs4 import BeautifulSoup
import re
import json
from HTMLParser import HTMLParser
from saveresult import Save_result


class toutiao:
    #这个爬虫的策略是一直跑下去，因为这个没有上下页请求之类的东西，所以可以延时一些
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }
        self.urls = [
            # 'http://www.toutiao.com/api/pc/feed/?category=%E7%BB%84%E5%9B%BE&utm_source=toutiao&as=A15579D7AFA0EB3&cp=597FF0BECBF3EE1',
            'https://www.toutiao.com/api/pc/feed/?max_behot_time=1499133489&category=__all__&utm_source=toutiao&widen=1&tadrequire=false',
            'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time_tmp=1499131781&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=%E7%BB%84%E5%9B%BE&utm_source=toutiao&as=A1F5F9655ABFB36&cp=595A5F6BB3262E1',#这个是照片的链接

            # 'https://www.toutiao.com/api/pc/feed/?category=news_society&utm_source=toutiao&widen=1&max_behot_time_tmp=1499130277&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_entertainment&utm_source=toutiao&widen=1&max_behot_time_tmp=1499127310&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=1&mmax_behot_time_tmp=1499126716&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time_tmp=1499129717&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_car&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128582&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_finance&utm_source=toutiao&widen=1&max_behot_time_tmp=1499127720&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=funny&utm_source=toutiao&widen=1&max_behot_time_tmp=1499121867&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time_tmp=1499130314&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_fashion&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128255&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_discovery&utm_source=toutiao&widen=1&mmax_behot_time_tmp=1499128281&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_regimen&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128301&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_essay&utm_source=toutiao&widen=1&max_behot_time_tmp=1499125173&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_history&utm_source=toutiao&widen=1&max_behot_time_tmp=1499125194&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_world&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128221&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_travel&utm_source=toutiao&widen=1&max_behot_time_tmp=1499125233&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_baby&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128468&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_story&utm_source=toutiao&widen=1&max_behot_time_tmp=1499125336&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_game&utm_source=toutiao&widen=1&max_behot_time_tmp=1499131054&tadrequire=true',
            # 'https://www.toutiao.com/api/pc/feed/?category=news_food&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128522&tadrequire=true'
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
        for url_to_get_index in self.urls:
            for i in range(2):
                try:#SyntaxError: unexpected EOF while parsing
                    self.session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
                    timea=time.time()
                    while True:
                        try:
                            response_in_function=self.session1.request(method='get',url=url_to_get_index,headers=self.headers)
                            break
                        except:
                            self.session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
                            timea=time.time()
                    timeb=time.time()
                    proxy_here = self.session1.proxies.values()[0].split('//')[1]
                    if timeb - timea < 3:
                        proxy_sendback(proxy_here)
                        
                    response_text= response_in_function.text.encode('utf-8')
                    datajson=json.loads(response_text)
                    datajson_index_data = datajson['data']
                    for one_index in datajson_index_data:
                        try:
                            title = one_index['title']
                        except:
                            title = ''
                        try:
                            reply_count = int(one_index['comments_count'])
                        except:
                            reply_count = 0
                        url = 'http://www.toutiao.com' + one_index['source_url']
                        try:
                            publish_user = one_index['source']  # publisher
                        except:
                            publish_user = ''
                        try:
                            publish_user_photo = one_index['media_avatar_url']
                        except:
                            publish_user_photo = ''
                        try:
                            vedio_id = one_index['video_id']
                        except:
                            vedio_id = None
                        try:
                            is_ad = one_index['label']
                        except:
                            is_ad = False

                        if vedio_id:
                            continue  # 如果是视频，直接舍弃
                        if is_ad == u'广告':
                            continue

                        id = one_index['group_id']

                        self.content_data_list.append({ 'id':id,
                                'url':url,
                                'reply_count':reply_count,
                                'title':title,
                                'publish_user':publish_user,
                                'publish_user_photo':publish_user_photo,
                                })

                except Exception as e:
                    print e
                print '\n\n'
                # time.sleep(10)

        self.global_status_num_index=0

    def get_content(self):
        def get_content_inside(data):#这个函数用来获得html文件，并在判断它是那种类型的网页，之后调用相应的函数就可以。
            img_urls=[]
            content=''
            url = data['url']
            session1 = requests.session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            timea = time.time()
            session1.cookies = cookielib.MozillaCookieJar()
            session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:
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
            if response_in_function.history:#用来判断是否跳转到其它网页去了，跳转了的话就不继续跟进
                if response_in_function.history[0].status_code in [301,302,303]:
                    real_url= response_in_function.history[0].headers._store['location'][1]
                    if 'toutiao' not in real_url:
                        return
                    else:
                        url=real_url#这是跳转过后的url

            Re_find_chineseTag = re.compile(r"chineseTag: '.*?'")
            chineseTag=Re_find_chineseTag.findall(response_in_function.text)
            if chineseTag:
                chineseTag=chineseTag[0].split("'")[1]
                if chineseTag==u'图片':
                    content_time_img=get_content_picture(response_in_function)
                elif chineseTag==u'问答':
                    content_time_img=get_content_wenda(response_in_function)
                else:
                    content_time_img=get_content_news(response_in_function)
            else:
                print chineseTag
                return








            # datasoup = BeautifulSoup(response_in_function.text, 'lxml')
            # Re_find_pattern1 = re.compile(r'\bvar gallery =.*?\]\}')
            # data_find_by_re=Re_find_pattern1.findall(response_in_function.text)
            # if data_find_by_re:#这里边是处理图片新闻
            #     picture_data = data_find_by_re[0]
            #     picture_data_json_original = picture_data.split('=')[1]
            #     datajson = json.loads(picture_data_json_original)
            #     for picture_info in datajson['sub_images']:
            #         img_url_in_for = picture_info['url']
            #         img_urls.append(img_url_in_for)
            #     for content_info in datajson['sub_abstracts']:
            #         content += content_info
            #     title = datajson['sub_titles'][0]
            #     # Re_find_publish_time=re.compile(r'')
            #     Re_find_time = re.compile(r'publish_time:.*?\,')
            #     publish_time = Re_find_time.findall(response_in_function.text)[0].split("'")[1].replace('/', '-')
            # else:
            #     text_content = response_in_function.text.split('artilceInfo:')[1].split('commentInfo')[0]
            #     Re_find_content = re.compile(r"content: '.*?\;'")
            #     Re_find_time2=re.compile(r"time: '.*?'")
            #     content= Re_find_content.findall(text_content)[0]
            #     publish_time=Re_find_time2.findall(text_content)[0]

            # Re_content_item_id = re.compile(r'item_id: \'.*?\'')
            # Re_content_qid = re.compile(r'qid : \".*?\"')
            # item_id_re = Re_content_item_id.findall(response_in_function.text)
            # if not item_id_re:
            #     print Re_content_item_id.findall(response_in_function.text)
            #     qid_re =Re_content_qid.findall(response_in_function.text)
            #     print qid_re[0].split('"')[1]#这里的作用是找出文中对应的id部分.
            #     # yield scrapy.Request()
            # else:
            #     print item_id_re[0].split("'")[1]
            #     thisurl=response_in_function.url.split('com/a')
            #     nexturl='http://www.toutiao.com/api/comment/list/?group_id='+thisurl[1].replace('/','')+'&item_id='+str(item_id_re[0].split("'")[1])+'&offset=0&count=20'
            #     print nexturl




            # data['url']=url#已跳转
            try:
                data['img_urls']=content_time_img['img_urls']
                data['content']=content_time_img['content']
                data['publish_time']=content_time_img['publish_time']
            except Exception as e:
                print e

            self.comments_url_list.append(data)
            print data
        #这里每个htmldata都是一个beautifulsoup对象
        def get_content_news(htmldata,data=None):
            content_nochange=''
            img_urls=[]
            try:
                text_content = htmldata.text.split('artilceInfo:')[1].split('commentInfo')[0]
                Re_find_content = re.compile(r"content: '.*?\;'")
                Re_find_time2 = re.compile(r"time: '.*?'")
                content = Re_find_content.findall(text_content)[0]
                content=content.split("'")[1]
                htmlparse=HTMLParser()
                contenthtml=htmlparse.unescape(content)
                content_soup=BeautifulSoup(contenthtml,'lxml')
                content=content_soup.text
                Re_find_img=re.compile(r'src=".*?"')
                img_urls_find_by_re=Re_find_img.findall(contenthtml)
                for img_url in img_urls_find_by_re:
                    img_url_split= img_url.split('"')[1]
                    img_urls.append(img_url_split)


                publish_time = Re_find_time2.findall(text_content)[0].split("'")[1]+':00'

                # content_nochange=content
                return {'content':content,'img_urls':img_urls,'publish_time':publish_time}
            except Exception as e:
                print e



            pass
        def get_content_picture(htmldata,data=None):
            img_urls = []
            content = ''
            Re_find_pattern1 = re.compile(r'\bvar gallery =.*?\]\}')
            data_find_by_re = Re_find_pattern1.findall(htmldata.text)
            if data_find_by_re:  # 这里边是处理图片新闻
                picture_data = data_find_by_re[0]
                picture_data_json_original = picture_data.split('=')[1]
                datajson = json.loads(picture_data_json_original)
                for picture_info in datajson['sub_images']:
                    img_url_in_for = picture_info['url']
                    img_urls.append(img_url_in_for)
                for content_info in datajson['sub_abstracts']:
                    content += content_info
                title = datajson['sub_titles'][0]
                Re_find_time = re.compile(r'publish_time:.*?\,')
                publish_time = Re_find_time.findall(htmldata.text)[0].split("'")[1].replace('/', '-')
            return {'content': content, 'img_urls': img_urls, 'publish_time': publish_time}
        def get_content_wenda(htmldata,data=None):#评论里边有评论，评论的评论里边还有评论，所以后边要有两个评论replynode获取函数，第一层评论可以根据has_more字段来判断遍历完了没有
            #这个函数获取评论是从首页来的，因为首页里边有提问的问题，所以要抓，但是后边调用的话，就调用另外一个函数来启动后续的评论获取。
            #问答里边的title和index中获得的title不一样。
            Re_find_question = re.compile(r"__question = .*?\|\| \[\]\;")
            Re_find_answer = re.compile(r"__answer = .*?\|\| \[\]\;")
            question_result=Re_find_question.findall(str(htmldata))
            answer_result=Re_find_answer.findall(str(htmldata))

            question_detail=question_result[0].replace(' || [];','').replace('__question = ','')
            answer_detail=answer_result[0].replace(' || [];','').replace('__question = ','')

            question_json=json.loads(question_detail)
            answer_json=json.loads(answer_detail)

            title=question_json[0]['title']
            content=question_json[0]['content']['text']
            publish_time=question_json[0]['create_time']
            publish_user_id=question_json[0]['user']['user_id']
            publish_user=question_json[0]['user']['uname']
            publish_user_photo=question_json[0]['user']['avatar_url']
            id=question_json[0]['qid']
            reply_nodes=[]


            for comment_content_all in answer_result:#这里边的时间格式有问题
                comment_content=comment_content_all['content']
                comment_publish_time=comment_content_all['show_time']
                comment_publish_user=comment_content_all['user']['uname']
                comment_publish_user_id=comment_content_all['user']['user_id']
                comment_publish_user_photo=comment_content_all['user']['avatar_url']
                comment_like_count=comment_content_all['digg_count']
                comment_reply_count=comment_content_all['comment_count']
                comment_id=comment_content_all['ansid']
                comment_url='https://www.wukong.com/wenda/web/question/loadmorev1/?qid='+id+'&count=10&req_type=1&offset=3&enter_ansid='+comment_id#每次请求下一次链接的时候offset+10就可以
                comment_reply_nodes=[]
                one_node={
                    'content':comment_content,
                    'publish_time':comment_publish_time,
                    'publish_user':comment_publish_user,
                    'publish_user_id':comment_publish_user_id,
                    'publish_user_photo':comment_publish_user_photo,
                    'like_count':comment_like_count,
                    'reply_nodes':comment_reply_nodes,
                    'reply_count':comment_reply_count,
                    #缺少url
                }
                reply_nodes.append(one_node)

            #开始判断评论是否还有下一页：
            get_content_in_wenda_comments_more({'id':id,})
            #---------------------------上边这部分的代码是前边没爬完的评论的延续

            data['title']=title
            data['content']=content
            data['publish_time']=publish_time
            data['publish_user_id']=publish_user_id
            data['publish_user']=publish_user
            data['publish_user_photo']=publish_user_photo
            data['id']=id
            data['reply_nodes']=reply_nodes


            self.result_list.append(data)#这里的评论获取也在content里边获取了，因为评论就是问答里边的内容，





        def get_content_in_wenda_comments_comments(htmldata,data=None):#获取评论中的评论
            pass
        def get_content_in_wenda_comments_more(comments_data,data=None):
            #https://www.wukong.com/wenda/web/question/loadmorev1/?count=10&qid=6370458749798187265&offset=10&t=1501814522809&req_type=1

            session1 = requests.session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            timea = time.time()
            session1.cookies = cookielib.MozillaCookieJar()
            session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:
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


            
            







        threadlist = []
        while self.global_status_num_index > 0 or self.content_data_list:
            while self.content_data_list or threadlist:
                for threadi in threadlist:
                    if not threadi.is_alive():
                        threadlist.remove(threadi)
                while len(threadlist) < LEN_COMMENT_LIST and self.content_data_list:
                    data_in_while = self.content_data_list.pop()
                    thread_in_while = threading.Thread(target=get_content_inside, args=(data_in_while,))
                    thread_in_while.setDaemon(True)
                    thread_in_while.start()
                    threadlist.append(thread_in_while)
                    print 'len of threadlist in content---', len(threadlist)
                    print 'len of content_data_list in content is ---', len(self.content_data_list)

        self.global_status_num_content = 0

    def get_comments(self):
        def get_comment_inside(data):
            session1 = requests.session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }

            timea = time.time()
            session1.cookies = cookielib.MozillaCookieJar()
            session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:
                    comment_url = ''
                    response_in_function = session1.request(method='get', url=comment_url, headers=headers,
                                                            timeout=5)  # 这里的headers会因为其它的线程使用而有所改变，因为线程安全的原因，这里不好控制，控制的意义不大。
                    break
                except Exception as e:
                    print e
            timeb = time.time()
            proxy_here = session1.proxies.values()[0].split('//')[1]
            if timeb - timea < 3:
                proxy_sendback(proxy_here)
            comments_data = []
            data_json = json.loads(response_in_function.text.encode('utf-8'))








            data['reply_nodes'] = comments_data
            while len(self.result_list) > 600:
                time.sleep(1)
                print 'is waiting the lenth of the result_list to decrease to 300'
            self.result_list.append(data)

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



    def run(self):
        thread1=threading.Thread(target=self.get_Index,args=())
        thread1.start()
        time.sleep(5)
        thread2=threading.Thread(target=self.get_content,args=())
        thread2.start()
        # # time.sleep(3)
        # thread3=threading.Thread(target=self.get_comments,args=())
        # thread3.start()
        # thread4=threading.Thread(target=self.save_result,args=())
        # thread4.start()
        pass


if __name__ == '__main__':
    thisclass=toutiao()
    thisclass.run()