#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import re



url='http://186t.ibeitun.net/show.aspx?mid=374'



Re_find_img=re.compile(r'src\=\"(.*?)\"')

response=requests.get(url=url)
# print response.text
datasoup=BeautifulSoup(response.text,'lxml')
content_soup= datasoup.select('div.rightBox')[0]
print content_soup.text
# print datasoup.select('div.downLoadTit > h1')[0].text
print content_soup.select('div.downLoadTit h1')[0].text
print '\n---------------------------------------------------------'
publish_user_time= content_soup.select('div,downLoadTit div.cource')[0].text
publish_user_time_split=publish_user_time.split(u'编辑：')[1].split(u'时间：')
print publish_user_time_split[0].strip()
print publish_user_time_split[1].strip()+' 00:00:00'
print content_soup.select('div.content.fixed')[0].text


img_urls= Re_find_img.findall(str(content_soup))
for i in img_urls:
    print i