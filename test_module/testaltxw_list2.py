#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup


response1=requests.get(url='http://www.altxw.com/news/content/2017-09/30/content_9494597.htm')
response1.encoding='utf-8'
datasoup=BeautifulSoup(response1.text,'lxml')

print datasoup.select('body > div.body > div > div.main.l > div > div > h1')[0].text
print datasoup.select('body > div.body > div > div.main.l > div > div > div > li:nth-of-type(2)')[0].text.split(u'：')[1]
content=''
for i in datasoup.select('body > div.body > div > div.main.l > div > div > ul > p'):
    content+= i.text
print content