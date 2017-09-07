#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup

headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'close',
        }

session1=requests.session()

response1=session1.request(method='get',url='http://www.scjjrb.com/Item/list.asp?id=674&page=1',headers=headers)
print response1.text.decode('gb2312')
session1.close()



# datasoup=BeautifulSoup(response1.text,'lxml')
# newslist= datasoup.select('div.newslist')[0].select('dl.nl_con1')
# for i in newslist:
#     print i.select('h4.nlc_tit a')[0].get('title')#title
#     print i.select('h4.nlc_tit a')[0].get('href')#href
#     print i.select('p.nlc_time')[0].text.split(u' ')[0]#publish_time
#     # print i.select('p.nlc_info')[0].text
#
# next_a= datasoup.select('a.next')#下一页链接，这里边的链接就是这样
# for one_a in next_a:
#     next_url= one_a.get('href')
#     if next_url not in ['javascript:;']:
#         print next_url