import requests
from bs4 import BeautifulSoup


session1=requests.session()
response1=session1.request(method='get',url='http://m.thepaper.cn/newsDetail_forward_1775459')
response1.encoding='utf-8'
# print response1.text


datasoup=BeautifulSoup(response1.text,'lxml')
for i in datasoup.select('source'):
    print i.get('src')