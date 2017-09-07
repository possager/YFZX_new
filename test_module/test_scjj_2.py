#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'close',
        }

session1=requests.session()
response1=session1.request(method='get',url='http://www.scjjrb.com/html/xwpd/jjlw/45821.html',headers=headers)
response1.encoding='gb2312'
datasoup=BeautifulSoup(response1.text,'lxml')

print datasoup.select('div.articlecontent .info span')[0].text.split(u'：')[1]#publish_user
print datasoup.select('#MyContent')[0].text.strip()