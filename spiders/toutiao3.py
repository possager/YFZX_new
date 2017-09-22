#_*_coding:utf-8_*_

import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


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
# import logging
from saveresult import BASIC_FILE
# from visit_page import get_response_and_text
# from visit_page2 import get_response_and_text
import datetime
from KafkaConnector1 import Producer,Consumer
from saveresult import get_result_name
from KafkaConnector import RemoteProducer,Consumer


from visit_page3 import get_response_and_text
from sava_data_to_MongoDB import save_data_to_mongodb





# logger_toutiao=logging.getLogger()
# logger_toutiao.setLevel(logging.WARNING)
# filehandler=logging.FileHandler(BASIC_FILE+'/toutiao/debug.text')
# logger_toutiao.addHandler(filehandler)
# formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# filehandler.setFormatter(formatter)


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
                for i in range(1):
                    try:
                        response1=get_response_and_text(url=url_to_get_index)
                        response_in_function=response1['response_in_function']
                        response_in_function_text=response1['response_in_function_text']
                        response_text=response_in_function_text.decode('utf-8')
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
                                if 'http' not in publish_user_photo:
                                    publish_user_photo='http:'+publish_user_photo
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

                            dict1={
                                    'id':id,
                                    'url':url,
                                    'reply_count':reply_count,
                                    'title':title,
                                    'publish_user':publish_user,
                                    'publish_user_photo':publish_user_photo,
                                    'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                                          }

                            self.content_data_list.append(dict1)
                    except Exception as e:
                        pass
            print '歇一会，现在在等待那600秒'
            time.sleep(600)


    def get_content(self):
        def get_content_inside(data):
            url = data['url']
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            response1=get_response_and_text(url=url,headers=headers)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            real_url = response_in_function.url
            if 'toutiao' not in real_url:
                # logger_toutiao.log(level=logging.WARNING, msg='toutiao was not in thisurl---------' + real_url)
                return
            elif 'http://www.toutiao.com/api/pc/subject/' in real_url:
                # logger_toutiao.log(level=logging.WARNING,msg='http://www.toutiao.com/api/pc/subject/ was in thisurl----------'+real_url)
                return
            else:
                url = real_url

            Re_find_chineseTag = re.compile(r"chineseTag: '.*?'")


            #######################################################


            chineseTag = Re_find_chineseTag.findall(response_in_function_text)
            if chineseTag:
                try:
                    # print 'the lenth of response-------',len(response_in_function_text)
                    chineseTag = chineseTag[0].split("'")[1]
                    if chineseTag == u'图片' or chineseTag=='图片':
                        content_time_img = get_content_picture({'response_in_function': response_in_function,
                                                                'response_in_function_text': response_in_function_text})
                    elif chineseTag == u'问答' or chineseTag=='问答':
                        content_time_img = get_content_wenda(htmldata={'response_in_function': response_in_function,'response_in_function_text': response_in_function_text,'data':data},
                                                             data=data)
                        return
                    else:
                        print chineseTag,'is gonging to get_content_news'
                        content_time_img = get_content_news({'response_in_function': response_in_function,
                                                             'response_in_function_text': response_in_function_text})
                except Exception as e:
                    # print e, '在区分是属于图片、问答等模块时出错'
                    pass
            else:

                # print chineseTag
                return
            #如果不是问答，那么就进入到这里边
            Re_find_itmeId = re.compile(r'itemId: \'.*?\'')  # 普通头条
            Re_find_itme_Id = re.compile(r'item_id:\'.*?\'')  # 图片
            if Re_find_itmeId.findall(response_in_function_text):
                try:
                    item_id = Re_find_itmeId.findall(response_in_function_text)[0].split("'")[1]
                except Exception as e:
                    # logger_toutiao.log(level=logging.WARNING, msg={'where': 'itemid来split失败了', 'contetn':
                    #     Re_find_itmeId.findall(response_in_function_text)[0]})
                    # print e, 'itemid在re中找到了，但是split失败了'
                    pass
            else:
                try:
                    item_id = Re_find_itme_Id.findall(response_in_function_text)[0].split("'")[1]
                except Exception as e:
                    pass
                    # print e, '在item——id中没找到值,图片的item_id'
                    # msg = {'errormsg': e.message + '在item——id中没找到值,图片的item_id',
                    #        'htmldata': response_in_function_text,
                    #        'url': response_in_function.url,
                    #        'code': response_in_function.code,
                    #        'msg': response_in_function.msg}
                    # logger_toutiao.log(level=logging.WARNING, msg=msg)
                    return

            try:
                data['img_urls'] = content_time_img['img_urls']
                data['content'] = content_time_img['content']
                if len(content_time_img['publish_time'])<12:
                    data['publish_time'] = content_time_img['publish_time']+' 00:00:00'
                else:
                    data['publish_time']=content_time_img['publish_time']
                data['item_id'] = item_id
                data['reply_nodes'] = []
            except Exception as e:
                # print e, 'data合成的时候除了问题'
                pass

            self.comments_url_list.append(data)

        def get_content_news(htmldata, data=None):
            content_nochange = ''
            img_urls = []
            try:
                # text_content = htmldata.text.split('artilceInfo:')[1].split('commentInfo')[0]
                print '9-21--------------------------0'
                try:
                    text_content = htmldata['response_in_function_text'].split('articleInfo:')[1].split('commentInfo')[0]
                    print '9-21---------------------------1'
                except Exception as e:
                    print e
                    print htmldata['response_in_function'].url
                Re_find_content = re.compile(r"content: '(.*?)'\.replace")
                Re_find_time2 = re.compile(r"time: '(.*?)'")
                content = Re_find_content.findall(text_content)[0]

                # content = content.split("'")[1]
                try:
                    content=content.decode('utf-8')
                except:
                    # try:
                    #     # content=content.encode('utf-8')
                    # except:
                    #     pass
                    pass
                htmlparse = HTMLParser()
                contenthtml = htmlparse.unescape(content)
                content_soup = BeautifulSoup(contenthtml, 'lxml')
                content = content_soup.text
                Re_find_img = re.compile(r'src="(.*?")')
                img_urls_find_by_re = Re_find_img.findall(contenthtml)
                for img_url in img_urls_find_by_re:
                    if '"' in img_url:
                        img_url_split = img_url.split('"')[1]
                    img_urls.append(img_url_split)

                publish_time = Re_find_time2.findall(htmldata['response_in_function_text'])[0] + ':00'
                print publish_time
                return {'content': content, 'img_urls': img_urls, 'publish_time': publish_time}
            except Exception as e:
                # logger_toutiao.log(msg={'msg':e.message+'在get_content_news中出了问题','content':htmldata['response_in_function_text']},level=logging.WARNING)
                print e, '在get_content_news中出了问题'

            pass

        def get_content_picture(htmldata, data=None):
            img_urls = []
            content = ''
            Re_find_pattern1 = re.compile(r'gallery:.*?\]\}\,\n    siblingList')
            # data_find_by_re = Re_find_pattern1.findall(htmldata.text)
            data_find_by_re = Re_find_pattern1.findall(htmldata['response_in_function_text'])

            if data_find_by_re:  # 这里边是处理图片新闻
                picture_data = data_find_by_re[0]
                picture_data_json_original = picture_data.replace('gallery:','').replace(',\n    siblingList','')
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
                                                                                                                    '-').strip()
                return {'content': content, 'img_urls': img_urls, 'publish_time': publish_time}#mark，是不是时间戳





        def get_content_wenda(htmldata,
                              data=None):
            Re_find_question = re.compile(r"__question = .*?\|\| \[\]\;")
            Re_find_answer = re.compile(r"__answer = .*?\|\| \[\]\;")
            Re_find_qid = re.compile(r'qid: \'.*?\'')


            question_result = Re_find_question.findall(str(htmldata['response_in_function_text']))
            answer_result = Re_find_answer.findall(str(htmldata['response_in_function_text']))
            qid = Re_find_qid.findall(str(htmldata['response_in_function_text']))

            question_detail = question_result[0].replace(' || [];', '').replace('__question = ', '')
            answer_detail = answer_result[0].replace(' || [];', '').replace('__answer = ', '')

            question_json = json.loads(question_detail)
            answer_json = json.loads(answer_detail)

            title = question_json[0]['title']
            content = question_json[0]['content']['text']
            publish_time = question_json[0]['create_time']
            publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(publish_time)))
            publish_user_id = question_json[0]['user']['user_id']
            publish_user = question_json[0]['user']['uname']
            publish_user_photo = question_json[0]['user']['avatar_url']
            if 'http' not in publish_user_photo:
                publish_user_photo='http:'+publish_user_photo
            id = question_json[0]['qid']
            reply_nodes = []

            for comment_content_all in answer_json:  # 这里边的时间格式有问题
                comment_content = comment_content_all['content']
                comment_content=BeautifulSoup(comment_content,'lxml')
                comment_content=comment_content.text
                comment_parend_id=data['id']#可以调用父函数的变量
                # comment_publish_time = '2017-'+comment_content_all['show_time']+':00'#时间有问题u'07-31 20:26'
                comment_publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(comment_content_all['create_time']))
                comment_publish_user = comment_content_all['user']['uname']
                comment_publish_user_id = comment_content_all['user']['user_id']
                comment_publish_user_photo = comment_content_all['user']['avatar_url']
                comment_like_count = comment_content_all['digg_count']
                comment_reply_count = comment_content_all['comment_count']
                comment_id = comment_content_all['ansid']
                comment_ancestor_id=data['id']
                comment_url = 'https://www.wukong.com/wenda/web/question/loadmorev1/?qid=' + id + '&count=10&req_type=1&offset=3&enter_ansid=' + comment_id  # 每次请求下一次链接的时候offset+10就可以
                comment_reply_nodes = get_content_in_wenda_comments_comments(
                    {'id': comment_id, 'reply_nodes': [], 'next_comment_url': None,'ancestor_id':data['id']})



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
                    'url': comment_url,
                    'parent_id':comment_parend_id,
                    'ancestor_id':comment_ancestor_id,
                    # 'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                reply_nodes.append(one_node)

            try:
                get_content_in_wenda_comments_more(
                    {'id': qid[0].split("'")[1], 'reply_nodes': reply_nodes, 'next_comment_url': None})#mark 8-22
            except Exception as e:
                print e, 'get_conten_in_wenda_comments_more中出了问题'#mark


            data['title'] = title#在问答中不会返回到get_contont模块中，所以
            data['content'] = content
            data['publish_time'] = publish_time
            data['publish_user_id'] = publish_user_id
            data['publish_user'] = publish_user
            data['publish_user_photo'] = publish_user_photo
            data['id'] = id
            data['reply_nodes'] = reply_nodes
            data['url']=htmldata['response_in_function'].url

            self.result_list.append(data)

        def get_content_in_wenda_comments_comments(id_replynodes,
                                                   data=None):

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            try:
                if not id_replynodes['next_comment_url']:
                    url_comments_more = 'https://www.wukong.com/wenda/web/comment/brow/?ansid=' + \
                                        id_replynodes['id'] + '&count=10&offset=0'
                    response1=get_response_and_text(url=url_comments_more)
                    response_in_function=response1['response_in_function']
                    response_in_function_text=response1['response_in_function_text']

                else:
                    response1=get_response_and_text(url=id_replynodes['next_comment_url'],headers=headers)
                    response_in_function=response1['response_in_function']
                    response_in_function_text=response1['response_in_function_text']

                # break
            except Exception as e:

                print e


            datajson_comment2 = json.loads(response_in_function_text)
            try:
                datajson_comment2['comments']
            except Exception as e:
                print e
            for comment2 in datajson_comment2['comments']:
                id = comment2['comment_id']
                like_count = comment2['digg_count']
                content = comment2['content']
                publish_user_id = comment2['user_info']['user_id']
                publish_user = comment2['user_info']['uname']
                publish_user_photo = comment2['user_info']['avatar_url']
                publish_time = comment2['create_time']
                publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(publish_time)))
                try:
                    ancestor_id=id_replynodes['ancestor_id']
                except Exception as e:
                    print e
                parent_id=id_replynodes['id']

                thisnode = {
                    'id': id,
                    'like_count': like_count,
                    'content': content,
                    'publish_user_id': publish_user_id,
                    'publish_user': publish_user,
                    'publish_user_photo': publish_user_photo,
                    'publish_time': publish_time,#发布时间
                    'parent_id':parent_id,
                    'ancestor_id':ancestor_id,
                    # 'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                id_replynodes['reply_nodes'].append(thisnode)
            if datajson_comment2['has_more']:
                url_offset = response_in_function.url.split('&offset=')
                offset = int(url_offset[1].split('&')[0]) + 10
                url = url_offset[0] + '&offset=' + str(offset)
                id_replynodes['next_comment_url'] = url
                reply_nodes2 = get_content_in_wenda_comments_comments(id_replynodes)
                return reply_nodes2
            else:
                return id_replynodes['reply_nodes']

        def get_content_in_wenda_comments_more(id_replynodes, data=None):
            error_time=5


            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
            }
            try:
                if not id_replynodes['next_comment_url']:
                    url_comments_more = 'https://www.wukong.com/wenda/web/question/loadmorev1/?count=10&qid=' + \
                                        id_replynodes['id'] + '&offset=10&req_type=1'
                    response1=get_response_and_text(url=url_comments_more,headers=headers)
                    response_in_function=response1['response_in_function']
                    response_in_function_text=response1['response_in_function_text']

                else:
                    response1=get_response_and_text(url=id_replynodes['next_comment_url'],headers=headers)
                    response_in_function=response1['response_in_function']
                    response_in_function_text=response1['response_in_function_text']

            except Exception as e:
                    print e
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
                id = one_comment['ansid']
                publish_time = one_comment['create_time']  # 时间戳mark
                publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(publish_time)))
                reply_count = one_comment['comment_count']
                publish_user_photo = one_comment['user']['avatar_url']
                publish_user = one_comment['user']['uname']
                publish_user_id = one_comment['user']['user_id']
                try:
                    reply_nodes = get_content_in_wenda_comments_comments({'id':id,'reply_nodes': [], 'next_comment_url':None})
                except Exception as e:
                    # print e
                    reply_nodes=[]
                parent_id=id_replynodes['id']
                ancestor_id=data['id']


                try:
                    this_node = {
                        'publish_time': publish_time,
                        'content': content,
                        'like_count': like_count,
                        'id': id,
                        'reply_count': reply_count,
                        'publish_user_photo': publish_user_photo,
                        'publish_user': publish_user,
                        'publish_user_id': publish_user_id,
                        'reply_nodes': reply_nodes,
                        'ancestor_id':ancestor_id,
                        'parent_id':parent_id,
                        # 'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                    id_replynodes['reply_nodes'].append(this_node)
                except Exception as e:
                    print e
            if datajson['data']['has_more']:
                url_offset = response_in_function.url.split('&offset=')
                offset = int(url_offset[1].split('&')[0]) + 10
                url = url_offset[0] + '&offset=' + str(offset)
                id_replynodes['next_comment_url'] = url
                reply_nodes2 = get_content_in_wenda_comments_more(id_replynodes)
                return reply_nodes2
            else:
                return id_replynodes['reply_nodes']

        threadlist = []
        while self.global_status_num_index > 0 or self.content_data_list:
        # while self.global_status_num_index > 0 or redis1.llen('toutiao_index')>0:
            while self.content_data_list or threadlist:
            # while self.content_data_list or redis1.llen('toutiao_index')>0:
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
                    # print data
                    comment_url = 'http://www.toutiao.com/api/comment/list/?group_id=' + str(
                        data['id']) + '&item_id=' + str(data['item_id']) + '&offset=0&count=20'
                    response1=get_response_and_text(url=comment_url)
                    response_in_function=response1['response_in_function']
                    response_in_function_text=response1['response_in_function_text']

                    break
                except Exception as e:
                    # print e,'mark1'
                    if 'item_id' in e:
                        messege = {'msg': e.message}
                        # logger_toutiao.log(msg=messege, level=logging.WARNING)
            comments_data = []
            try:
                data_json = json.loads(response_in_function_text)
                data_json['data']['comments']
            except Exception as e:
                # print e,'mark1'#这里本来是应该返回正常的json数据，但是会返回一抹莫名奇妙的location跳转的网站。因此直接把它结束了，宁愿没抓，也不要误抓。
                return
            for one_comment in data_json['data']['comments']:
                content = one_comment['text']
                like_count = one_comment['digg_count']
                publish_time = one_comment['create_time']
                publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(publish_time)))
                publish_user_photo = one_comment['user']['avatar_url']
                publish_user_id = one_comment['user']['user_id']
                publish_user = one_comment['user']['name']#8-17日改
                id = one_comment['id']
                reply_count = one_comment['reply_count']
                parent_id=data['id']
                ancestor_id=data['id']

                if reply_count > 0:
                    reply_nodes = get_comment_comment({'id': id,'ancestor_id':data['id']})
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
                    'reply_nodes': reply_nodes,
                    'parent_id':parent_id,
                    'ancestor_id':ancestor_id,
                    # 'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                }
                # data['reply_nodes'].append(thisnode)
                comments_data.append(thisnode)

            # 这里的评论能获取的就20个,所以不设计下一页,评论中的评论也是不设计下一页

            data['reply_nodes'] = comments_data
            while len(self.result_list) > 600:
                time.sleep(1)
                print 'result_list 的长度低于300了，等待输入存储中。。。'

            self.result_list.append(data)

        def get_comment_comment(data1):  # 评论中有评论,起名data1是为了防止覆盖data变量
            id = data1['id']
            error_time=3
            while True:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
                    # 'Upgrade-Insecure-Requests':'1',
                    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    # 'Accept-Encoding':'gzip, deflate',
                    'Accept-Language':'zh-CN,zh;q=0.8',
                    # 'Cache-Control':'max-age=0',
                    'Connection':'close'

                }
                while True:
                    try:
                        comment_url = 'http://www.toutiao.com/api/comment/get_reply/?comment_id=' + str(
                            id) + '&item_id=' + str(id) + '&offset=0&count=20'


                        response1=get_response_and_text(url=comment_url,headers=headers)
                        response_in_function=response1['response_in_function']
                        response_in_function_text=response1['response_in_function_text']
                        datajson = json.loads(response_in_function_text)
                        break

                    except Exception as e:
                        # print e,'mark2'
                        error_time-=1
                        if error_time <1:
                            return

                reply_nodes = []
                # datajson=json.loads(response_in_function.text)
                try:
                    datajson = json.loads(response_in_function_text)#报错  ValueError: No JSON object could be decoded  8-28日错误很多
                except Exception as e:
                    # print e
                    pass
                try:
                    datajson['data']['data']#sometimes this will be wrong! the response returned is not what you need!9-7
                except Exception as e:
                    # print e
                    error_time-=1
                    if error_time<1:
                        # print 'wrong time too much'
                        break
                    continue
                for one_comment in datajson['data']['data']:
                    content = one_comment['text']
                    like_count = one_comment['digg_count']
                    publish_time = one_comment['create_time']
                    publish_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(publish_time)))
                    publish_user_id = one_comment['user']['user_id']
                    publish_user = one_comment['user']['screen_name']
                    publish_user_photo = one_comment['user']['avatar_url']
                    id = one_comment['id']
                    try:
                        ancestor_id=data1['ancestor_id']
                    except Exception as e:
                        # print e,'mark3'
                        ancestor_id='wrong'
                    parent_id=data1['id']
                    thisnode = {
                        'publish_user': publish_user,
                        'content': content,
                        'like_count': like_count,
                        'publish_time': publish_time,
                        'publish_user_id': publish_user_id,
                        'publish_user_photo': publish_user_photo,
                        'id': id,
                        'ancestor_id':ancestor_id,
                        'parent_id':parent_id,
                        # 'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
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
            try:
                del data['item_id']
            except Exception as e:
                # print e
                pass
            try:

                # host = '182.150.63.40'
                # port = '12308'
                # username = 'silence'
                # password = 'silence'
                #
                # # producer = Producer(hosts=host)
                # producer = RemoteProducer(host=host, port=port, username=username, password=password)
                result_file = get_result_name(plantform_e='toutiao', plantform_c='今日头条', date_time=data['publish_time'],
                                              urlOruid=data['url'],
                                              newsidOrtid=data['id'],
                                              datatype='news', full_data=data)
                print datetime.datetime.now(),'--------',result_file

                save_data_to_mongodb(data={'data':data},item_id=result_file,platform_e='toutiao',platform_c='今日头条')

                # producer.send(topic='1101_STREAM_SPIDER', value={'data': data}, key=result_file, updatetime=data['spider_time'])
                pass



                # host = '192.168.6.187:9092,192.168.6.188:9092,192.168.6.229:9092,192.168.6.230:9092'
                # producer = Producer(hosts=host)
                # result_file = get_result_name(plantform_c='今日头条',plantform_e='JinRiTouTiao', date_time=data['publish_time'], urlOruid=data['url'],
                #                               newsidOrtid=data['id'],
                #                               datatype='news', full_data=data)
                #
                # producer.send(topic='topic', value={'data': data}, key=result_file, updatetime=data['spider_time'])

                # comsumer = Consumer('topic', host, 'll')
                # what = comsumer.poll()
                # # for i in comsumer.poll():
                # #     print i.topic
                # for i in what:
                #     topic = i.topic
                #     partition = i.partition
                #     offset = i.offset
                #     key = i.key
                #     value = i.value

                # Save_result(plantform='toutiao', date_time=data['publish_time'], urlOruid=data['url'],
                #                 newsidOrtid=data['id'], datatype='news', full_data=data)
            except Exception as e:
                # print e
                pass

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
        # time.sleep(3)
        thread3=threading.Thread(target=self.get_comments,args=())
        thread3.start()
        time.sleep(3)
        thread4=threading.Thread(target=self.save_result,args=())
        thread4.start()

if __name__ == '__main__':
    thisclass=toutiao()
    thisclass.run()
    # thisclass.get_content()
    # thisclass.get_Index()