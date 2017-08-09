#_*_coding:utf-8_*_
import cookielib
from proxy_to_redis import *
from setting import *
from bs4 import BeautifulSoup
import re
import json
from HTMLParser import HTMLParser
from saveresult import Save_result
from proxy_to_redis import redis1
import urllib2
import logging
from saveresult import BASIC_FILE


logger_toutiao=logging.getLogger()
logger_toutiao.setLevel(logging.WARNING)
filehandler=logging.FileHandler(BASIC_FILE+'/toutiao/debug.text')
logger_toutiao.addHandler(filehandler)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
filehandler.setFormatter(formatter)


timeoutdefault=20

class toutiao:
    #这个爬虫的策略是一直跑下去，因为这个没有上下页请求之类的东西，所以可以延时一些
    def __init__(self):
        self.timeoutdefault=20
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }
        self.urls = [
            'http://www.toutiao.com/api/pc/feed/?category=%E7%BB%84%E5%9B%BE&utm_source=toutiao&as=A15579D7AFA0EB3&cp=597FF0BECBF3EE1',
            'https://www.toutiao.com/api/pc/feed/?max_behot_time=1499133489&category=__all__&utm_source=toutiao&widen=1&tadrequire=false',
            'https://www.toutiao.com/api/pc/feed/?category=news_hot&utm_source=toutiao&widen=1&max_behot_time_tmp=1499131781&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=%E7%BB%84%E5%9B%BE&utm_source=toutiao&as=A1F5F9655ABFB36&cp=595A5F6BB3262E1',#这个是照片的链接

            'https://www.toutiao.com/api/pc/feed/?category=news_society&utm_source=toutiao&widen=1&max_behot_time_tmp=1499130277&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_entertainment&utm_source=toutiao&widen=1&max_behot_time_tmp=1499127310&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=1&mmax_behot_time_tmp=1499126716&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_sports&utm_source=toutiao&widen=1&max_behot_time_tmp=1499129717&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_car&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128582&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_finance&utm_source=toutiao&widen=1&max_behot_time_tmp=1499127720&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=funny&utm_source=toutiao&widen=1&max_behot_time_tmp=1499121867&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time_tmp=1499130314&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_fashion&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128255&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_discovery&utm_source=toutiao&widen=1&mmax_behot_time_tmp=1499128281&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_regimen&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128301&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_essay&utm_source=toutiao&widen=1&max_behot_time_tmp=1499125173&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_history&utm_source=toutiao&widen=1&max_behot_time_tmp=1499125194&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_world&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128221&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_travel&utm_source=toutiao&widen=1&max_behot_time_tmp=1499125233&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_baby&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128468&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_story&utm_source=toutiao&widen=1&max_behot_time_tmp=1499125336&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_game&utm_source=toutiao&widen=1&max_behot_time_tmp=1499131054&tadrequire=true',
            'https://www.toutiao.com/api/pc/feed/?category=news_food&utm_source=toutiao&widen=1&max_behot_time_tmp=1499128522&tadrequire=true'
        ]
        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()


        #-------------------------8-9改动
        self.openner=None
        self.request=None
        self.proxy=None


        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容

    def get_Index(self):
        while True:
            for url_to_get_index in self.urls:
                for i in range(2):
                    try:
                        self.proxy={'http':'http://'+get_proxy_from_redis()}
                        timea=time.time()
                        while True:
                            try:
                                proxyhandler=urllib2.ProxyHandler(self.proxy)
                                openner=urllib2.build_opener(proxyhandler)
                                request1=urllib2.Request(url=url_to_get_index,headers=self.headers)
                                response_in_function=openner.open(request1,timeout=timeoutdefault)
                                response_in_function_text=response_in_function.read()

                                break
                            except:
                                self.proxy={'http':'http://'+get_proxy_from_redis()}
                                timea=time.time()
                        timeb=time.time()
                        proxy_here=self.proxy.values()[0].split('//')[1]
                        openner.close()
                        if timeb - timea < 3:
                            proxy_sendback(proxy_here)
                        response_text=response_in_function_text.encode('utf-8')
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
                            redis1.lpush('urltest',url)
                    except Exception as e:
                        pass
            time.sleep(10)
        self.global_status_num_index=0

    def get_content(self):
        def get_content_inside(data):
            url = data['url']
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            timea = time.time()
            cookies = cookielib.MozillaCookieJar()
            proxies1 = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:
                    request1 = urllib2.Request(url=url, headers=headers)
                    cookiehandler1 = urllib2.HTTPCookieProcessor(cookies)
                    proxyhandler = urllib2.ProxyHandler(proxies1)
                    openner1 = urllib2.build_opener(cookiehandler1, proxyhandler)
                    response_in_function = openner1.open(request1, timeout=timeoutdefault)
                    response_in_function_text = response_in_function.read()
                    break
                except Exception as e:
                    proxies1 = {'http': 'http://' + get_proxy_from_redis()}
                    timea = time.time()
                    print e, '请求indexnews时出错'
            timeb = time.time()
            proxy_here = proxies1.values()[0].split('//')[1]
            openner1.close()
            if timeb - timea < 3:
                proxy_sendback(proxy_here)
            real_url = response_in_function.url
            if 'toutiao' not in real_url:
                logger_toutiao.log(level=logging.WARNING, msg='toutiao was not in thisurl---------' + real_url)
                return
            elif 'http://www.toutiao.com/api/pc/subject/' in real_url:
                logger_toutiao.log(level=logging.WARNING,msg='http://www.toutiao.com/api/pc/subject/ was in thisurl----------'+real_url)
                return
            else:
                url = real_url

            Re_find_chineseTag = re.compile(r"chineseTag: '.*?'")


            #######################################################


            chineseTag = Re_find_chineseTag.findall(response_in_function_text)
            if chineseTag:
                try:
                    print 'the lenth of response-------',len(response_in_function_text)
                    chineseTag = chineseTag[0].split("'")[1]
                    if chineseTag == u'图片':
                        content_time_img = get_content_picture({'response_in_function': response_in_function,
                                                                'response_in_function_text': response_in_function_text})
                    elif chineseTag == u'问答':
                        content_time_img = get_content_wenda(htmldata={'response_in_function': response_in_function,
                                                                       'response_in_function_text': response_in_function_text},
                                                             data={})
                        return
                    else:
                        content_time_img = get_content_news({'response_in_function': response_in_function,
                                                             'response_in_function_text': response_in_function_text})
                except Exception as e:
                    print e, '在找图片，问答等分类模块的时候出了问题'
                    logger_toutiao.log(level=logging.WARNING, msg={'where': '在找板块分类定位的时候除了问题', 'content': e.message})
            else:
                logger_toutiao.log(level=logging.WARNING, msg=chineseTag)
                print chineseTag
                return
            #如果不是问答，那么就进入到这里边
            Re_find_itmeId = re.compile(r'itemId: \'.*?\'')  # 普通头条
            Re_find_itme_Id = re.compile(r'item_id:\'.*?\'')  # 图片
            if Re_find_itmeId.findall(response_in_function_text):
                try:
                    item_id = Re_find_itmeId.findall(response_in_function_text)[0].split("'")[1]
                except Exception as e:
                    logger_toutiao.log(level=logging.WARNING, msg={'where': 'itemid来split失败了', 'contetn':
                        Re_find_itmeId.findall(response_in_function_text)[0]})
                    print e, 'itemid在re中找到了，但是split失败了'
            else:
                try:
                    item_id = Re_find_itme_Id.findall(response_in_function_text)[0].split("'")[1]
                except Exception as e:
                    print e, '在item——id中没找到值,图片的item_id'
                    msg = {'errormsg': e.message + '在item——id中没找到值,图片的item_id',
                           'htmldata': response_in_function_text,
                           'url': response_in_function.url,
                           'code': response_in_function.code,
                           'msg': response_in_function.msg}
                    logger_toutiao.log(level=logging.WARNING, msg=msg)
                    return

            try:
                data['img_urls'] = content_time_img['img_urls']
                data['content'] = content_time_img['content']
                data['publish_time'] = content_time_img['publish_time']
                data['item_id'] = item_id
                data['reply_nodes'] = []
            except Exception as e:
                print e, 'data合成的时候除了问题'

            self.comments_url_list.append(data)

        def get_content_news(htmldata, data=None):
            content_nochange = ''
            img_urls = []
            try:
                # text_content = htmldata.text.split('artilceInfo:')[1].split('commentInfo')[0]
                text_content = htmldata['response_in_function_text'].split('artilceInfo:')[1].split('commentInfo')[0]
                Re_find_content = re.compile(r"content: '.*?\;'")
                Re_find_time2 = re.compile(r"time: '.*?'")
                content = Re_find_content.findall(text_content)[0]
                content = content.split("'")[1]
                htmlparse = HTMLParser()
                contenthtml = htmlparse.unescape(content)
                content_soup = BeautifulSoup(contenthtml, 'lxml')
                content = content_soup.text
                Re_find_img = re.compile(r'src=".*?"')
                img_urls_find_by_re = Re_find_img.findall(contenthtml)
                for img_url in img_urls_find_by_re:
                    img_url_split = img_url.split('"')[1]
                    img_urls.append(img_url_split)

                publish_time = Re_find_time2.findall(text_content)[0].split("'")[1] + ':00'
                return {'content': content, 'img_urls': img_urls, 'publish_time': publish_time}
            except Exception as e:
                logger_toutiao.log(msg={'msg':e.message+'在get_content_news中出了问题','content':htmldata['response_in_fucntion_text']},level=logging.WARNING)
                print e, '在get_content_news中出了问题'

            pass

        def get_content_picture(htmldata, data=None):
            img_urls = []
            content = ''
            Re_find_pattern1 = re.compile(r'\bvar gallery =.*?\]\}')
            # data_find_by_re = Re_find_pattern1.findall(htmldata.text)
            data_find_by_re = Re_find_pattern1.findall(htmldata['response_in_function_text'])
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
                # publish_time = Re_find_time.findall(htmldata.text)[0].split("'")[1].replace('/', '-')
                publish_time = Re_find_time.findall(htmldata['response_in_function_text'])[0].split("'")[1].replace('/',
                                                                                                                    '-')
                return {'content': content, 'img_urls': img_urls, 'publish_time': publish_time}

        def get_content_wenda(htmldata,
                              data=None):
            Re_find_question = re.compile(r"__question = .*?\|\| \[\]\;")
            Re_find_answer = re.compile(r"__answer = .*?\|\| \[\]\;")
            Re_find_qid = re.compile(r'qid: \'.*?\'')


            question_result = Re_find_question.findall(str(htmldata['response_in_function_text']))
            answer_result = Re_find_answer.findall(str(htmldata['response_in_function_text']))
            qid = Re_find_qid.findall(str(htmldata['response_in_function_text']))

            question_detail = question_result[0].replace(' || [];', '').replace('__question = ', '')
            answer_detail = answer_result[0].replace(' || [];', '').replace('__question = ', '')

            question_json = json.loads(question_detail)
            answer_json = json.loads(answer_detail)

            title = question_json[0]['title']
            content = question_json[0]['content']['text']
            publish_time = question_json[0]['create_time']
            publish_user_id = question_json[0]['user']['user_id']
            publish_user = question_json[0]['user']['uname']
            publish_user_photo = question_json[0]['user']['avatar_url']
            id = question_json[0]['qid']
            reply_nodes = []

            for comment_content_all in answer_json:  # 这里边的时间格式有问题
                comment_content = comment_content_all['content']
                comment_publish_time = comment_content_all['show_time']
                comment_publish_user = comment_content_all['user']['uname']
                comment_publish_user_id = comment_content_all['user']['user_id']
                comment_publish_user_photo = comment_content_all['user']['avatar_url']
                comment_like_count = comment_content_all['digg_count']
                comment_reply_count = comment_content_all['comment_count']
                comment_id = comment_content_all['ansid']
                comment_url = 'https://www.wukong.com/wenda/web/question/loadmorev1/?qid=' + id + '&count=10&req_type=1&offset=3&enter_ansid=' + comment_id  # 每次请求下一次链接的时候offset+10就可以
                comment_reply_nodes = get_content_in_wenda_comments_comments(
                    {'id': comment_id, 'reply_nodes': [], 'next_comment_url': None})



                ######################################



                one_node = {
                    'content': comment_content,
                    'publish_time': comment_publish_time,
                    'publish_user': comment_publish_user,
                    'publish_user_id': comment_publish_user_id,
                    'publish_user_photo': comment_publish_user_photo,
                    'like_count': comment_like_count,
                    'reply_nodes': comment_reply_nodes,
                    'reply_count': comment_reply_count,
                    'url': comment_url
                }
                reply_nodes.append(one_node)

            try:
                get_content_in_wenda_comments_more(
                    {'id': qid[0].split("'")[1], 'reply_nodes': reply_nodes, 'next_comment_url': None})
            except Exception as e:
                print e, 'get_conten_in_wenda_comments_more中出了问题'


            data['title'] = title
            data['content'] = content
            data['publish_time'] = publish_time
            data['publish_user_id'] = publish_user_id
            data['publish_user'] = publish_user
            data['publish_user_photo'] = publish_user_photo
            data['id'] = id
            data['reply_nodes'] = reply_nodes

            self.result_list.append(data)

        def get_content_in_wenda_comments_comments(id_replynodes,
                                                   data=None):

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            timea = time.time()
            cookies1 = cookielib.MozillaCookieJar()
            proxies1 = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:
                    proxyhandler = urllib2.ProxyHandler(proxies1)
                    cookiehandler = urllib2.HTTPCookieProcessor(cookies1)
                    openner1 = urllib2.build_opener(proxyhandler, cookiehandler)
                    if not id_replynodes['next_comment_url']:
                        url_comments_more = 'https://www.wukong.com/wenda/web/comment/brow/?ansid=' + \
                                            id_replynodes['id'] + '&count=10&offset=0'
                        request1 = urllib2.Request(url=url_comments_more, headers=headers)
                        response_in_function = openner1.open(request1, timeout=timeoutdefault)
                        response_in_function_text = response_in_function.read()  # mark2

                    else:
                        request1 = urllib2.Request(url=id_replynodes['next_comment_url'], headers=headers)
                        response_in_function = openner1.open(request1, timeout=timeoutdefault)
                        response_in_function_text = response_in_function.read()

                    break
                except Exception as e:
                    proxies1 = {'http': 'http://' + get_proxy_from_redis()}
                    timea = time.time()
                    print e
            timeb = time.time()
            proxy_here = proxies1.values()[0].split('//')[1]
            openner1.close()
            if timeb - timea < 3:
                proxy_sendback(proxy_here)
            datajson_comment2 = json.loads(response_in_function_text)
            for comment2 in datajson_comment2['comments']:
                id = comment2['comment_id']
                like_count = comment2['digg_count']
                content = comment2['content']
                publish_user_id = comment2['user_info']['user_id']
                publish_user = comment2['user_info']['uname']
                publish_user_photo = comment2['user_info']['avatar_url']
                publish_time = comment2['create_time']

                thisnode = {
                    'id': id,
                    'like_count': like_count,
                    'content': content,
                    'publish_user_id': publish_user_id,
                    'publish_user': publish_user,
                    'publish_user_photo': publish_user_photo,
                    'publish_time': publish_time
                }
                id_replynodes['reply_nodes'].append(thisnode)
            if datajson_comment2['has_more']:
                url_offset = response_in_function.url.split('&offset=')
                offset = int(url_offset[1].split('&')[0]) + 10
                url = url_offset + '&offset=' + str(offset)
                id_replynodes['next_comment_url'] = url
                reply_nodes2 = get_content_in_wenda_comments_comments(id_replynodes)
                return reply_nodes2
            else:
                return id_replynodes['reply_nodes']

        def get_content_in_wenda_comments_more(id_replynodes, data=None):
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            timea = time.time()
            cookies1 = cookielib.MozillaCookieJar()
            proxies1 = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:
                    proxyhandler = urllib2.ProxyHandler(proxies1)
                    cookiehandler = urllib2.HTTPCookieProcessor(cookies1)
                    openner1 = urllib2.build_opener(proxyhandler, cookiehandler)
                    if not id_replynodes['next_comment_url']:
                        url_comments_more = 'https://www.wukong.com/wenda/web/question/loadmorev1/?count=10&qid=' + \
                                            id_replynodes['id'] + '&offset=10&req_type=1'
                        request1 = urllib2.Request(url=url_comments_more, headers=headers)
                        response_in_function = openner1.open(request1, timeout=timeoutdefault)
                        response_in_function_text = response_in_function.read()

                    else:
                        request1 = urllib2.Request(url=id_replynodes['next_comment_url'], headers=headers)
                        response_in_function = openner1.open(request1, timeout=timeoutdefault)
                        response_in_function_text = response_in_function.read()

                    break
                except Exception as e:
                    proxies1 = {'http': 'http://' + get_proxy_from_redis()}
                    timea = time.time()
                    print e
            timeb = time.time()
            proxy_here = proxies1.values()[0].split('//')[1]
            # session1.close()
            openner1.close()
            if timeb - timea < 3:
                proxy_sendback(proxy_here)
            datajson = json.loads(response_in_function_text)
            for one_comment in datajson['data']['ans_list']:
                datasoup_content = BeautifulSoup(one_comment['content'], 'lxml')
                content = datasoup_content.text
                img_urls = []
                Re_find_img = re.compile(r'src=".*?"')
                img_urls_find_by_re = Re_find_img.findall(one_comment['content'])
                for img_url in img_urls_find_by_re:
                    img_url_split = img_url.split('"')[1]
                    img_urls.append(img_url_split)
                like_count = one_comment['digg_count']
                id = one_comment['id']
                publish_time = one_comment['create_time']  # 时间戳
                reply_count = one_comment['comment_count']
                publish_user_photo = one_comment['user']['avatar_url']
                publish_user = one_comment['user']['uname']
                publish_user_id = one_comment['user']['user_id']
                reply_nodes = []

                this_node = {
                    'publish_time': publish_time,
                    'content': content,
                    'like_count': like_count,
                    'id': id,
                    'reply_count': reply_count,
                    'publish_user_photo': publish_user_photo,
                    'publish_user': publish_user,
                    'publish_user_id': publish_user_id,
                    'reply_nodes': reply_nodes
                }
                id_replynodes['reply_nodes'].append(this_node)

            if datajson['data']['has_more']:
                url_offset = response_in_function.url.split('&offset=')
                offset = int(url_offset[1].split('&')[0]) + 10
                url = url_offset + '&offset=' + str(offset)
                id_replynodes['next_comment_url'] = url
                reply_nodes2 = get_content_in_wenda_comments_comments(id_replynodes)
                return reply_nodes2
            else:
                return id_replynodes['reply_nodes']

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

        self.global_status_num_content = 0

    def get_comments(self):
        def get_comment_inside(data):
            # session1 = requests.session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }

            while True:  # 强制请求
                try:
                    timea = time.time()

                    cookies1 = cookielib.MozillaCookieJar()
                    proxies1 = {'http': 'http://' + get_proxy_from_redis()}
                    proxyhandler = urllib2.ProxyHandler(proxies1)
                    cookiehandler = urllib2.HTTPCookieProcessor(cookies1)
                    comment_url = 'http://www.toutiao.com/api/comment/list/?group_id=' + str(
                        data['id']) + '&item_id=' + str(data['item_id']) + '&offset=5&count=10'
                    request1 = urllib2.Request(url=comment_url, headers=headers)
                    opener1 = urllib2.build_opener(proxyhandler, cookiehandler)
                    response_in_function = opener1.open(request1)
                    response_in_function_text = response_in_function.read()

                    break
                except Exception as e:
                    print e
                    if 'item_id' in e:
                        messege = {'msg': e.message}
                        logger_toutiao.log(msg=messege, level=logging.WARNING)
            timeb = time.time()
            # proxy_here = session1.proxies.values()[0].split('//')[1]
            proxy_here = proxies1.values()[0].split('//')[1]
            # session1.close()
            opener1.close()
            if timeb - timea < 3:
                proxy_sendback(proxy_here)
            comments_data = []
            try:
                # data_json = json.loads(response_in_function.text.encode('utf-8'))
                data_json = json.loads(response_in_function_text)
            except Exception as e:
                print e
            for one_comment in data_json['data']['comments']:
                content = one_comment['text']
                like_count = one_comment['digg_count']
                publish_time = one_comment['create_time']
                publish_user_photo = one_comment['user']['avatar_url']
                publish_user_id = one_comment['user']['user_id']
                publish_user = one_comment['user']['user_id']
                id = one_comment['id']
                reply_count = one_comment['reply_count']
                if reply_count > 0:
                    reply_nodes = get_comment_comment({'id': id})
                else:
                    reply_nodes = []

                thisnode = {
                    'content': content,
                    'like_count': like_count,
                    'publish_time': publish_time,
                    'publish_user_photo': publish_user_photo,
                    'publish_user_id': publish_user_id,
                    'publish_user': publish_user,
                    'id': id,
                    'reply_count': reply_count,
                    'reply_nodes': reply_nodes
                }
                # data['reply_nodes'].append(thisnode)
                comments_data.append(thisnode)

            # 这里的评论能获取的就20个,所以不设计下一页,评论中的评论也是不设计下一页




            data['reply_nodes'] = comments_data
            while len(self.result_list) > 600:
                time.sleep(1)
                print 'is waiting the lenth of the result_list to decrease to 300'
            self.result_list.append(data)

        def get_comment_comment(data):  # 评论中有评论
            id = data['id']
            # session1 = requests.session()
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }

            timea = time.time()
            # session1.cookies = cookielib.MozillaCookieJar()
            # session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
            cookies1 = cookielib.MozillaCookieJar()
            proxies1 = {'http': 'http://' + get_proxy_from_redis()}
            while True:  # 强制请求
                try:

                    # session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
                    # http://www.toutiao.com/api/comment/get_reply/?comment_id=1574954012827661&dongtai_id=1574954012827661&offset=0&count=20
                    comment_url = 'http://www.toutiao.com/api/comment/get_reply/?comment_id=' + str(
                        id) + '&item_id=' + str(id) + '&offset=5&count=10'

                    proxyhandler = urllib2.ProxyHandler(proxies1)
                    cookiehandler = urllib2.HTTPCookieProcessor(cookies1)
                    request1 = urllib2.Request(url=comment_url, headers=headers)
                    openner1 = urllib2.build_opener(proxyhandler, cookiehandler)
                    response_in_function = openner1.open(request1)
                    response_in_function_text = response_in_function.read()

                    # response_in_function = session1.request(method='get', url=comment_url, headers=headers,
                    #                                         timeout=self.timeoutdefault)  # 这里的headers会因为其它的线程使用而有所改变，因为线程安全的原因，这里不好控制，控制的意义不大。
                    # datajson = json.loads(response_in_function.text)
                    datajson = json.loads(response_in_function_text)

                    break
                except Exception as e:
                    print e
            timeb = time.time()
            # proxy_here = session1.proxies.values()[0].split('//')[1]
            proxy_here = proxies1.values()[0].split('//')[1]
            # session1.close()
            openner1.close()
            if timeb - timea < 3:
                proxy_sendback(proxy_here)

            reply_nodes = []
            # datajson=json.loads(response_in_function.text)
            datajson = json.loads(response_in_function_text)
            for one_comment in datajson['data']['data']:
                content = one_comment['text']
                like_count = one_comment['digg_count']
                publish_time = one_comment['create_time']
                publish_user_id = one_comment['user']['user_id']
                publish_user = one_comment['user']['screen_name']
                publish_user_photo = one_comment['user']['avatar_url']
                id = one_comment['id']
                thisnode = {
                    'publish_user': publish_user,
                    'content': content,
                    'like_count': like_count,
                    'publish_time': publish_time,
                    'publish_user_id': publish_user_id,
                    'publish_user_photo': publish_user_photo,
                    'id': id
                }
                reply_nodes.append(thisnode)

            return reply_nodes

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
        self.global_status_num_comments = 0

    def save_result(self):
        def save_result(data):
            Save_result(plantform='toutiao', date_time=data['publish_time'], urlOruid=data['url'],
                        newsidOrtid=data['id'], datatype='news', full_data=data)

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


    def run(self):
        thread1=threading.Thread(target=self.get_Index,args=())
        thread1.start()
        # time.sleep(20)
        thread2=threading.Thread(target=self.get_content,args=())
        thread2.start()
        # # time.sleep(3)
        # thread3=threading.Thread(target=self.get_comments,args=())
        # thread3.start()
        # thread4=threading.Thread(target=self.save_result,args=())
        # thread4.start()

if __name__ == '__main__':
    thisclass=toutiao()
    thisclass.run()