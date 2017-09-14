import requests
from  bs4 import  BeautifulSoup

headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

session1=requests.session()
response1=session1.request(method='get',url='http://wap.chengdu.cn/?action=category&catid=583',headers=headers)

response1.encoding='utf-8'
datasoup=BeautifulSoup(response1.text,'lxml')


url_id_set=set()
for i in  datasoup.select('div.content.more ul li a'):
    url_id_set.add(int(i.get('href').split('contentid=')[1]))

print max(list(url_id_set))