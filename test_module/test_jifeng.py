#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import json
import re


url_test='http://bbs.gfan.com/android-8483949-1-1.html'

Re_find_url_bankuai=re.compile(r'(http://bbs\.gfan\.com/forum-\d{2,4}-1\.html)')

# data_response=requests.get(url=url_test)
# data_response_text=data_response.text
# url_bankuai= Re_find_url_bankuai.findall(data_response_text)
# print len(url_bankuai)
# print len(set(url_bankuai))
#
# for i in list(set(url_bankuai)):
#     print i
# print list(set(url_bankuai))

response1=requests.get(url=url_test)
# print response1.text

Re_sub_publish_time=re.compile(r'')





datasoup=BeautifulSoup(response1.text,'lxml')
# print datasoup.select('.nxt')

# for i in  datasoup.select('#moderate  tbody')[1:]:
#     print '\n\n'
#     print i.select('th > a')[0].text #title
#     print i.select('td.by a')[0].text #publish_user
#     print i.select('td.by a')[0].get('href') #publish_user_url
#     print i.select('td.by em span')[0].text+':00' #publish_time
#     print i.select('td.num a')[0].text #reply_count
#     print i.select('td.num em')[0].text #view_num
#     print i.select('th > a')[0].get('href') #url
#
# print datasoup.select('.nxt')[0].get('href')


for one_div in  datasoup.select('#postlist > div[id]')[:-1]:
    print '\n\n\n'
    print one_div.select('div.authi a')[0].text
    # print one_div.select()
    # print one_div.select('div.authi')[0]
    # print one_div.select('')
    try:
        print one_div.select('.t_fsz')[0].text
    except Exception as e:
        print e,'这里楼层数据被删除了'



