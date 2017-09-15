# _*_coding:utf-8_*_
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import json
import time
import urllib
from bs4 import BeautifulSoup
import cookielib
import threading
from proxy_to_redis import *
from multiprocessing import process
from setting import CONTENT_THREADING_NUM
from setting import COMMENTS_THREADING_NUM
import re
import logging
import datetime
from datetime import timedelta
from KafkaConnector import RemoteProducer,Consumer





from visit_page2 import get_response_and_text
# from visit_page2 import get_response_and_text
from KafkaConnector1 import Producer,Consumer
from saveresult import get_result_name
from saveresult import Save_result
import redis


class jifeng:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        }

        self.connectpool = redis.ConnectionPool(host='localhost', port=6379)
        self.redis1 = redis.Redis(connection_pool=connectpool)

        self.global_status_num_index = 1
        self.global_status_num_content = 2
        self.global_status_num_comments = 3
        self.global_status_num_result = 4

        self.session1 = requests.session()
        self.cookies = cookielib.MozillaCookieJar()

        self.urls = [u'http://bbs.gfan.com/forum-1660-1.html', u'http://bbs.gfan.com/forum-1671-1.html', u'http://bbs.gfan.com/forum-920-1.html', u'http://bbs.gfan.com/forum-47-1.html', u'http://bbs.gfan.com/forum-16-1.html', u'http://bbs.gfan.com/forum-1653-1.html', u'http://bbs.gfan.com/forum-1302-1.html', u'http://bbs.gfan.com/forum-1578-1.html', u'http://bbs.gfan.com/forum-970-1.html', u'http://bbs.gfan.com/forum-1683-1.html', u'http://bbs.gfan.com/forum-1678-1.html', u'http://bbs.gfan.com/forum-963-1.html', u'http://bbs.gfan.com/forum-339-1.html', u'http://bbs.gfan.com/forum-1342-1.html', u'http://bbs.gfan.com/forum-164-1.html', u'http://bbs.gfan.com/forum-661-1.html', u'http://bbs.gfan.com/forum-1024-1.html', u'http://bbs.gfan.com/forum-517-1.html', u'http://bbs.gfan.com/forum-1257-1.html', u'http://bbs.gfan.com/forum-649-1.html', u'http://bbs.gfan.com/forum-1679-1.html', u'http://bbs.gfan.com/forum-506-1.html', u'http://bbs.gfan.com/forum-1473-1.html', u'http://bbs.gfan.com/forum-1550-1.html', u'http://bbs.gfan.com/forum-1607-1.html', u'http://bbs.gfan.com/forum-1260-1.html', u'http://bbs.gfan.com/forum-1069-1.html', u'http://bbs.gfan.com/forum-1661-1.html', u'http://bbs.gfan.com/forum-165-1.html', u'http://bbs.gfan.com/forum-1238-1.html', u'http://bbs.gfan.com/forum-1688-1.html', u'http://bbs.gfan.com/forum-1629-1.html', u'http://bbs.gfan.com/forum-1329-1.html', u'http://bbs.gfan.com/forum-1656-1.html', u'http://bbs.gfan.com/forum-967-1.html', u'http://bbs.gfan.com/forum-972-1.html', u'http://bbs.gfan.com/forum-1681-1.html', u'http://bbs.gfan.com/forum-1367-1.html', u'http://bbs.gfan.com/forum-1199-1.html', u'http://bbs.gfan.com/forum-1513-1.html', u'http://bbs.gfan.com/forum-1112-1.html', u'http://bbs.gfan.com/forum-1161-1.html', u'http://bbs.gfan.com/forum-1467-1.html', u'http://bbs.gfan.com/forum-729-1.html', u'http://bbs.gfan.com/forum-502-1.html', u'http://bbs.gfan.com/forum-1580-1.html', u'http://bbs.gfan.com/forum-1530-1.html', u'http://bbs.gfan.com/forum-1617-1.html', u'http://bbs.gfan.com/forum-1686-1.html', u'http://bbs.gfan.com/forum-975-1.html', u'http://bbs.gfan.com/forum-1640-1.html', u'http://bbs.gfan.com/forum-1684-1.html', u'http://bbs.gfan.com/forum-23-1.html', u'http://bbs.gfan.com/forum-1604-1.html', u'http://bbs.gfan.com/forum-109-1.html', u'http://bbs.gfan.com/forum-304-1.html', u'http://bbs.gfan.com/forum-602-1.html', u'http://bbs.gfan.com/forum-1696-1.html', u'http://bbs.gfan.com/forum-1448-1.html', u'http://bbs.gfan.com/forum-1625-1.html', u'http://bbs.gfan.com/forum-1545-1.html', u'http://bbs.gfan.com/forum-1577-1.html', u'http://bbs.gfan.com/forum-1576-1.html', u'http://bbs.gfan.com/forum-1621-1.html', u'http://bbs.gfan.com/forum-749-1.html', u'http://bbs.gfan.com/forum-1443-1.html', u'http://bbs.gfan.com/forum-1675-1.html', u'http://bbs.gfan.com/forum-1571-1.html', u'http://bbs.gfan.com/forum-962-1.html', u'http://bbs.gfan.com/forum-1345-1.html', u'http://bbs.gfan.com/forum-958-1.html', u'http://bbs.gfan.com/forum-11-1.html', u'http://bbs.gfan.com/forum-1548-1.html', u'http://bbs.gfan.com/forum-847-1.html', u'http://bbs.gfan.com/forum-240-1.html', u'http://bbs.gfan.com/forum-1601-1.html', u'http://bbs.gfan.com/forum-1687-1.html', u'http://bbs.gfan.com/forum-1689-1.html', u'http://bbs.gfan.com/forum-986-1.html', u'http://bbs.gfan.com/forum-86-1.html', u'http://bbs.gfan.com/forum-673-1.html', u'http://bbs.gfan.com/forum-1581-1.html', u'http://bbs.gfan.com/forum-216-1.html', u'http://bbs.gfan.com/forum-1235-1.html', u'http://bbs.gfan.com/forum-1552-1.html', u'http://bbs.gfan.com/forum-1121-1.html', u'http://bbs.gfan.com/forum-989-1.html', u'http://bbs.gfan.com/forum-62-1.html', u'http://bbs.gfan.com/forum-279-1.html', u'http://bbs.gfan.com/forum-574-1.html', u'http://bbs.gfan.com/forum-980-1.html', u'http://bbs.gfan.com/forum-676-1.html', u'http://bbs.gfan.com/forum-1676-1.html', u'http://bbs.gfan.com/forum-1508-1.html', u'http://bbs.gfan.com/forum-1356-1.html', u'http://bbs.gfan.com/forum-211-1.html', u'http://bbs.gfan.com/forum-1695-1.html', u'http://bbs.gfan.com/forum-375-1.html', u'http://bbs.gfan.com/forum-351-1.html', u'http://bbs.gfan.com/forum-1630-1.html', u'http://bbs.gfan.com/forum-1340-1.html', u'http://bbs.gfan.com/forum-1619-1.html', u'http://bbs.gfan.com/forum-983-1.html', u'http://bbs.gfan.com/forum-1624-1.html', u'http://bbs.gfan.com/forum-625-1.html', u'http://bbs.gfan.com/forum-888-1.html', u'http://bbs.gfan.com/forum-1382-1.html', u'http://bbs.gfan.com/forum-454-1.html', u'http://bbs.gfan.com/forum-1616-1.html', u'http://bbs.gfan.com/forum-1080-1.html', u'http://bbs.gfan.com/forum-960-1.html', u'http://bbs.gfan.com/forum-1651-1.html', u'http://bbs.gfan.com/forum-1663-1.html', u'http://bbs.gfan.com/forum-1361-1.html', u'http://bbs.gfan.com/forum-1665-1.html', u'http://bbs.gfan.com/forum-22-1.html', u'http://bbs.gfan.com/forum-976-1.html', u'http://bbs.gfan.com/forum-1685-1.html', u'http://bbs.gfan.com/forum-819-1.html', u'http://bbs.gfan.com/forum-1627-1.html', u'http://bbs.gfan.com/forum-1017-1.html', u'http://bbs.gfan.com/forum-306-1.html', u'http://bbs.gfan.com/forum-134-1.html', u'http://bbs.gfan.com/forum-730-1.html', u'http://bbs.gfan.com/forum-1691-1.html', u'http://bbs.gfan.com/forum-308-1.html', u'http://bbs.gfan.com/forum-1558-1.html', u'http://bbs.gfan.com/forum-1570-1.html', u'http://bbs.gfan.com/forum-522-1.html', u'http://bbs.gfan.com/forum-398-1.html', u'http://bbs.gfan.com/forum-1475-1.html', u'http://bbs.gfan.com/forum-1447-1.html', u'http://bbs.gfan.com/forum-1259-1.html', u'http://bbs.gfan.com/forum-1667-1.html', u'http://bbs.gfan.com/forum-1566-1.html', u'http://bbs.gfan.com/forum-1682-1.html', u'http://bbs.gfan.com/forum-1610-1.html', u'http://bbs.gfan.com/forum-1647-1.html', u'http://bbs.gfan.com/forum-1349-1.html', u'http://bbs.gfan.com/forum-961-1.html', u'http://bbs.gfan.com/forum-1648-1.html', u'http://bbs.gfan.com/forum-192-1.html', u'http://bbs.gfan.com/forum-835-1.html', u'http://bbs.gfan.com/forum-1692-1.html', u'http://bbs.gfan.com/forum-1694-1.html', u'http://bbs.gfan.com/forum-96-1.html', u'http://bbs.gfan.com/forum-984-1.html', u'http://bbs.gfan.com/forum-1690-1.html', u'http://bbs.gfan.com/forum-595-1.html', u'http://bbs.gfan.com/forum-919-1.html', u'http://bbs.gfan.com/forum-170-1.html', u'http://bbs.gfan.com/forum-1240-1.html', u'http://bbs.gfan.com/forum-1050-1.html', u'http://bbs.gfan.com/forum-1247-1.html', u'http://bbs.gfan.com/forum-1677-1.html', u'http://bbs.gfan.com/forum-1458-1.html', u'http://bbs.gfan.com/forum-1210-1.html', u'http://bbs.gfan.com/forum-1343-1.html', u'http://bbs.gfan.com/forum-1609-1.html', u'http://bbs.gfan.com/forum-1330-1.html', u'http://bbs.gfan.com/forum-403-1.html', u'http://bbs.gfan.com/forum-527-1.html', u'http://bbs.gfan.com/forum-1505-1.html', u'http://bbs.gfan.com/forum-848-1.html', u'http://bbs.gfan.com/forum-1184-1.html', u'http://bbs.gfan.com/forum-1674-1.html', u'http://bbs.gfan.com/forum-1378-1.html', u'http://bbs.gfan.com/forum-861-1.html', u'http://bbs.gfan.com/forum-978-1.html', u'http://bbs.gfan.com/forum-1594-1.html', u'http://bbs.gfan.com/forum-1321-1.html', u'http://bbs.gfan.com/forum-1272-1.html', u'http://bbs.gfan.com/forum-354-1.html', u'http://bbs.gfan.com/forum-1645-1.html', u'http://bbs.gfan.com/forum-130-1.html', u'http://bbs.gfan.com/forum-990-1.html', u'http://bbs.gfan.com/forum-399-1.html', u'http://bbs.gfan.com/forum-484-1.html']
        self.index_data_list=[]
        self.content_data_list = []  # 下次需要获得的content链接，不是content内容
        self.comments_data_list = []  # 下次需要获得的comment链接，不是comment内容
        self.result_data_list = []  # 这个存储的是已经跑完了的内容
        self.publish_user_url_need_to_visit = []

    def get_Index(self):
        def get_index_inside(url_get_index):
            while True:
                response1=get_response_and_text(url=url_get_index,headers=self.headers)
                respnse_in_function=response1['response_in_function']
                respnse_in_function_text=response1['response_in_function_text']

                datasoup=BeautifulSoup(respnse_in_function_text,'lxml')
                for one_forum in datasoup.select('#moderate  tbody')[1:]:
                    try:
                        title= one_forum.select('th > a')[0].text  # title
                        publish_user= one_forum.select('td.by a')[0].text  # publish_user
                        # print one_forum.select('td.by a')[0].get('href')  # publish_user_url
                        publish_time= one_forum.select('td.by em span')[0].text + ':00'  # publish_time
                        reply_count= one_forum.select('td.num a')[0].text  # reply_count
                        read_count= one_forum.select('td.num em')[0].text  # view_num
                        url= one_forum.select('th > a')[0].get('href')  # url

                        this_reply_node={
                            'title':title,
                            'publish_user':publish_user,
                            'publish_time':publish_time,
                            'reply_count':reply_count,
                            'read_count':read_count,
                            'url':url,
                            # 'publish_user':None,

                        }
                        self.content_data_list.append(this_reply_node)
                    except:
                        pass

                next_page_url=datasoup.select('.nxt')
                if next_page_url:
                    next_url=next_page_url[0].get('href')
                    url_get_index=next_url
                else:
                    break



        threadlist=[]
        while self.urls or threadlist:
            for threadi in threadlist:
                if not threadi.is_alive():
                    threadlist.remove(threadi)
            while len(threadlist) < CONTENT_THREADING_NUM and self.urls:
                data_in_while = self.urls.pop()
                thread_in_while = threading.Thread(target=get_index_inside, args=(data_in_while,))
                thread_in_while.setDaemon(True)
                thread_in_while.start()
                threadlist.append(thread_in_while)

    def get_content(self):
        def get_content_inside(data):
            url_for_debug=data['url']
            response1=get_response_and_text(url=url_for_debug,headers=self.headers)
            response_in_function=response1['response_in_function']
            response_in_function_text=response1['response_in_function_text']


            datasoup=BeautifulSoup(response_in_function_text,'lxml')






    def run(self):
        thread1 = threading.Thread(target=self.get_Index, args=())
        thread1.start()
        # thread2 = threading.Thread(target=self.get_content, args=())
        # thread2.start()
        # thread4 = threading.Thread(target=self.save_result, args=())
        # thread4.start()
        pass


if __name__ == '__main__':
    thisclass=jifeng()
    thisclass.run()