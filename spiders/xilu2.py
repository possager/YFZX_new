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
import datetime
from datetime import timedelta

class xilu:
    # 没有图片处理模块，对应的图片处理模块导致信息读取不完全。
    # http://wap.chengdu.cn/1700213这是一个典型的图片新闻网页
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
            'X-Requested-With': 'XMLHttpRequest',  # 重要
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'm.xilu.com',
            'Upgrade-Insecure-Requests': '1'

        }
        self.urls = [
            'http://m.xilu.com/index.html',
            # 'http://m.xilu.com/list_1353.html',
            # 'http://m.xilu.com/list_1283.html',
            # 'http://m.xilu.com/list_1311.html',
            # 'http://m.xilu.com/list_1142.html',
            # 'http://m.xilu.com/list_1412.html'#这个是解析图片，估计会出现解析不准确的情况。
            # 'http://m.xilu.com/list_1469.html'
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
            for i in range(300):
                try:  # SyntaxError: unexpected EOF while parsing
                    # self.session1.proxies = {'http': 'http://' + get_proxy_from_redis()}
                    response1 = self.session1.post(url=url_to_get_index, headers=self.headers, data={'page': i})
                    # response1=get_response_and_text(url=url_to_get_index,headers=self.headers,)
                    self.session1.close()
                    response_text = response1.text.encode('utf-8')
                    self.session1.close()
                    eval(response_text)
                    json_charge = json.loads(json.dumps(eval(response_text)))
                    if not json_charge:
                        break
                    if response1.cookies:
                        self.session1.cookies = response1.cookies
                    if 'Set-Cookie' in response1.headers:
                        for headers_key in response1.headers.keys():
                            if 'Set-Cookie' in headers_key:
                                set_cookie = response1.headers[headers_key]
                                cookies_name = set_cookie.split(';')[0].split('=')
                                self.session1.cookies[cookies_name[0]] = cookies_name[1]
                            else:
                                self.session1.headers[headers_key] = response1.headers[headers_key]
                    for news_index in json_charge:
                        data_in_index = {}
                        data_in_index['publish_time'] = news_index['sdate']  # publish_time
                        data_in_index['id'] = news_index['rfilename']  # id
                        data_in_index['title'] = news_index['title']  # title
                        data_in_index['read_count'] = news_index['onclick']  # view_num
                        data_in_index['url'] = 'http://m.xilu.com/v/' + news_index['rfilename'] + '.html'
                        data_in_index['spider_time']=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        self.content_data_list.append(data_in_index)
                        return
                except Exception as e:
                    print e
                print '\n\n'
                time.sleep(10)
        self.global_status_num_index = 0

    def get_content(self):
        print 'hello in get_content'
        threadlist = []

        def get_content_inside(data):  # 在线程函数中这里使用心得session算了，线程安全，这里是获取的一页的信息，另一个名字相似的函数是获得下一页的content信息
            url = data['url']
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }
            response1=get_response_and_text(url=url,headers=headers)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']
            datasoup = BeautifulSoup(response_in_function_text, 'lxml')

            Re_find_isimgpage = re.compile(r'\<ul class\=\"piclist\"\>')
            to_charge_is_picture = Re_find_isimgpage.findall(response_in_function_text)
            if to_charge_is_picture:  # 是图片模块，进入图片处理模块
                print to_charge_is_picture, 'and is in deal_pucture and the url is ---', data['url']
                content_and_img_urls = get_content_inside_picture(datasoup)
                img_urls = content_and_img_urls['img_urls']
                contentall = content_and_img_urls['content']

            else:
                content = ''
                img_urls = []
                for i in datasoup.select('body > div.scrollBox.mt10 > div.article > div.art_co.sau > p'):
                    content += i.text
                # 8-3添加图片抓取功能
                Re_find_img_url = re.compile(r'src=".*?"/\>')
                content_part_data = datasoup.select('div.article')
                if content_part_data:
                    data_find_by_re = Re_find_img_url.findall(str(content_part_data[0]))
                    for url_img_re in data_find_by_re:
                        img_urls.append(url_img_re.split('"')[1])
                next_page_selector = datasoup.select(
                    'body > div.scrollBox.mt10 > div.article > div.mb10.mt5.fs14 > a.page-next.ml5')
                contentall = ''
                if next_page_selector:
                    next_page_html = next_page_selector[0].get('href')
                    if next_page_html and len(next_page_html) > 3:
                        next_page_url = next_page_html
                        next_url = 'http://m.xilu.com' + next_page_url
                        data['url'] = next_url
                        content_and_img_urls2 = get_content_inside_next_page(
                            {'content': content, 'nexturl': next_url, 'img_urls': img_urls})
                        contentall += content_and_img_urls2['content']
                        img_urls3 = []
                        for i in content_and_img_urls2['img_urls']:
                            img_urls3.append(i)
                        for i in img_urls3:
                            img_urls.append(i)

                else:
                    contentall = content

            publish_time = data['publish_time']
            if publish_time == u'刚刚':
                publish_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            elif u'小时前' in publish_time:
                time_pass = int(publish_time.replace(u'小时前', ''))
                publish_time=(datetime.datetime.now()-timedelta(hours=time_pass)).strftime('%Y-%m-%d %H:%M:%S')
            elif u'分钟前' in publish_time:
                time_pass = int(publish_time.replace(u'分钟前', ''))
                publish_time=(datetime.datetime.now()-timedelta(minutes=time_pass)).strftime('%Y-%m-%d %H:%M:%S')
            elif '-' in publish_time and len(publish_time) == 5:
                publish_time = '2017-' + publish_time+' 00:00:00'
            data['content'] = contentall
            data['img_urls'] = img_urls
            data['publish_time'] = publish_time
            data['url'] = url

            while len(self.comments_url_list) > 600:  # 防止一个列表中的东西太多，太多了就等等
                time.sleep(1)
                print 'is waiting the lenth of comments_urls_list to decrease to 300'
            self.comments_url_list.append(data)

        def get_content_inside_next_page(data):
            url = data['nexturl']
            content = data['content']
            img_urls = data['img_urls']
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }
            response1=get_response_and_text(url=url,headers=headers)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']

            datasoup = BeautifulSoup(response_in_function_text, 'lxml')
            content1 = ''
            for i in datasoup.select('body > div.scrollBox.mt10 > div.article > div.art_co.sau > p'):
                content1 += i.text
            content += content1
            # 8-3
            Re_find_img_url = re.compile(r'src=".*?"/\>')
            content_part_data = datasoup.select('div.article')
            if content_part_data:
                data_find_by_re = Re_find_img_url.findall(str(content_part_data[0]))
                img_urls2=[]
                for url_img_re in data_find_by_re:
                    imgurl=url_img_re.split('"')[1]
                    img_urls2.append(imgurl)
                for url_without_http in img_urls2:
                    if 'http' not in url_without_http:
                        url_without_http='http'+url_without_http
                        img_urls.append(url_without_http)
                        pass
            # 8-3


            next_page_selector = datasoup.select(
                'body > div.scrollBox.mt10 > div.article > div.mb10.mt5.fs14 > a.page-next.ml5')
            if next_page_selector:
                next_page_html = next_page_selector[0].get('href')
                if next_page_html and len(next_page_html) > 3:
                    next_page_url = next_page_html
                    next_url = 'http://m.xilu.com' + next_page_url
                    content_result = get_content_inside_next_page(
                        {'content': content, 'nexturl': next_url, 'img_urls': img_urls})
                    return content_result
                else:
                    return {'content': content, 'img_urls': img_urls}

        def get_content_inside_picture(datasoup):
            img_urls = []
            content = ''
            for imgurl in datasoup.select('#slider > ul > li > img'):
                # img_urls.append(imgurl.get('src'))
                imgurl=imgurl.get('src')
                if 'http' not in imgurl:
                    imgurl='http'+imgurl
                img_urls.append(imgurl)
            for contenti in datasoup.select('#slider > ul > li > p'):
                content += contenti.text
            return {'img_urls': img_urls, 'content': content}

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
        def get_comment_inside(data):
            headers = {
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }
            comment_url = 'http://changyan.sohu.com/api/3/topic/liteload?&client_id=cysYw3AKM&page_size=30&hot_size=10&topic_source_id=' + \
                          data['id']

            response1=get_response_and_text(url=comment_url,headers=headers)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']


            comments_data = []
            data_json = json.loads(response_in_function_text)
            reply_count_outside=data_json['cmt_sum']

            if data_json['comments']:
                data_json_comments = data_json['comments']

                for someone_comment in data_json_comments:
                    content = someone_comment['content']  # content
                    id = someone_comment['comment_id']  # id
                    publish_user_photo = someone_comment['passport']['img_url']  # publish_user_photo
                    publish_user = someone_comment['passport']['nickname']  # publish_user
                    publish_user_id = someone_comment['passport']['user_id']  # publish_user_id
                    create_time = someone_comment['create_time']  # publish_time
                    spider_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    parent_id=data['id']
                    ancestor_id=data['id']
                    comments=someone_comment['comments']
                    reply_count=someone_comment['reply_count']
                    like_count=someone_comment['support_count']
                    dislike_count=someone_comment['oppose_count']
                    if comments:
                        parent_id=comments['comment_id']

                    thiscomments = {
                        'content': content,
                        'id': id,
                        'publish_user_photo': publish_user_photo,
                        'publish_user': publish_user,
                        'publish_user_id': publish_user_id,
                        'create_time': create_time,
                        'spider_time': spider_time,
                        'parent_id':parent_id,
                        'ancestor_id':ancestor_id,
                        'reply_count':reply_count,
                        'like_count':like_count,
                        'dislike_count':dislike_count

                    }
                    comments_data.append(thiscomments)

            data['reply_nodes'] = comments_data
            data['reply_count']=reply_count_outside
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





    def save_result(self):
        def save_result(data):
            print 'deal result'
            Save_result(plantform='xilu', date_time=data['publish_time'], urlOruid=data['url'], newsidOrtid=data['id'],
                        datatype='news', full_data=data)

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
        # time.sleep(5)
        thread2 = threading.Thread(target=self.get_content, args=())
        thread2.start()
        # time.sleep(3)
        thread3 = threading.Thread(target=self.get_comments, args=())
        thread3.start()
        thread4 = threading.Thread(target=self.save_result, args=())
        thread4.start()
        pass


if __name__ == '__main__':
    thisclass = xilu()
    # thisclass.get_Index()
    thisclass.run()