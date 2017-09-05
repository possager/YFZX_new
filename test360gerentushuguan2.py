#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import json

session1=requests.session()
headers={
    # 'Accept': '*/*',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    # 'cookie': 'BDTUJIAID=22139bce90aad109451d0cbbeb0fed77; _ga=GA1.1.1036367116.1504236827; doctaobaocookie=1; 360docsn=RSP8U3SW94AQ0RK7; Hm_lvt_d86954201130d615136257dde062a503=1502150932,1504236788,1504492977; Hm_lpvt_d86954201130d615136257dde062a503=' + str(int(time.time())),
    'Host': 'www.360doc.com',
    'Cache-Control':'max-age=0',
    'Proxy-Connection': 'close',
    # 'Referer': 'http://www.360doc.com/index.html',
    # 'X-Requested-With': 'XMLHttpRequest',  # 重要
    'Referer':'http://www.360doc.com/content/17/0902/06/40167318_684060643.shtml',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }



response1=session1.request(method='post',url='http://www.360doc.cn/ajax/refmore.ashx',data={'pagenum':'4','artid':'683174651'},headers=headers)

# print response1.text
datasoup=BeautifulSoup(response1.text,'lxml')
for i in  datasoup.select('.pllist1 '):
    print i.text
    print i.select('.plbox')[0].text
    print i.select('img')[0].get('src')
    print i.select('.name1 > a')[0].text
    print i.select('.name1 > a')[0].get('href')
    print i.select('.name1 > a')[0].get('href').split('userid=')[-1]
    print i.select('div.time')[0].text.split(u'\xa0')[-1]+':00'