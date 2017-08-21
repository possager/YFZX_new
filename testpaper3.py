import requests
import re
from bs4 import BeautifulSoup


response1=requests.request(method='get',url='http://www.thepaper.cn/load_moreFloorComment.jsp?contid=1768770')
datasoup=BeautifulSoup(response1.text,'lxml')
for i in datasoup.select('#startId'):
    print i.get('startid')
for jj in datasoup.select('div > div.aqwleft > div > a > img'):
    print jj
for jjj in datasoup.select('div.aq_write.clearfix > div.aqwright > h3 > a'):
    print jjj
    print jjj.get('href').split('commentId=')[1]
    print 'http://www.thepaper.cn/'+jjj.get('href')
for jjjj in datasoup.select('div.aq_write.clearfix > div.aqwright > h3 > span'):
    print jjjj
for j5 in datasoup.select(' div.aq_write.clearfix > div.aqwright > div.floor_content > div > h3 > span'):
    print j5.text
for j6 in datasoup.select('div > div.aqwright > div.ansright_cont > a'):
    print j6.text
for j7 in datasoup.select(' div.aq_write.clearfix > div.aqwright > div.ansright_time > a:nth-of-type(1)'):
    print j7.text
# for j8 in datasoup.select('')
