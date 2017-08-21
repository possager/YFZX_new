#_*_coding:utf-8_*_
import urllib
import urllib2
import re
import requests
from bs4 import BeautifulSoup
import chardet

headers = {
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



data1={'page':2}
url2='http://m.xilu.com/index.html'
data=urllib.urlencode(data1)
request1=urllib2.Request(url=url2,data=data,headers=headers)
openner1=urllib2.build_opener()
response=openner1.open(request1)
data2=response.read()
# print data2
# print chardet.detect(data2)

response2=requests.get(url=url2,headers=headers)
print response2.text