#_*_coding:utf-8_*_
import urllib2
import requests
import cookielib
from visit_page import get_response_and_text
from setting import *
import threading
from bs4 import BeautifulSoup




class xcar:
    #因为论坛类地网站结构，设计和新闻类的有区别，这里index里获得论坛的板块；content里获得论坛的论贴的列表，comments里获得这个论贴的所有评论数据之类的,相应的数据获取方法也有所改变
    def __init__(self):
        self.timeoutdefault = 20
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
        }

        self.urls=[
                    #地方分舵
                    'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1811',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=702',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=688',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=148',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=192',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=456',
                   #华中地区
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=102',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=120',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=176',
                    #西北地区
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=162',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=307',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=305',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=306',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=161',
                   # 东北地区
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=53',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=275',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=274',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=480',
                    #华北论坛
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=91',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=47',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=42',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=271',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=300',
                    #华东地区
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=44',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=43',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=80',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=154',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=301',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=52',
                    #华南地区
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=45',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=114',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=97',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=172',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=1880',
                   #西南论坛
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=46',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=150',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=303',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=149',
                   'http://www.xcar.com.cn/bbs/forumdisplay.php?fid=304',

                   ]

        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        # -------------------------8-9改动
        self.openner = None
        self.request = None
        self.proxy = None

        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_url_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_list = []  # 这个存储的是已经跑完了的内容

    def get_Index(self):
        self.content_data_list=self.urls

        #更改一些东西


    def get_content(self):
        def get_content_inside(url_with_page):
            response1=get_response_and_text(url=url_with_page)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text'].decode('gb2312').encode('utf-8')
            datasoup=BeautifulSoup(response_in_function_text,'lxml')



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
