#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup

urllist=[
    # 'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=650',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=651',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=652',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=670',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=654',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=653',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=665',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=664',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=660',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=656',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=666',
    'http://www.nssbt.com/index.php?m=content&c=index&a=lists&catid=661'
]

# for url in urllist:
# # url=urllist[0]
#     response1=requests.get(url=url)
#     datasoup=BeautifulSoup(response1.text,'lxml')
#     for i in datasoup.select('body > div.content > div.shishiimportantnews > div.left > ul > li'):
#         print i.select('span')[0].text
#         print i.select('a')[0].get('href')
#         print i.select('a')[0].get('title')

url='http://www.nssbt.com/index.php?m=content&c=index&a=show&catid=654&id=58228'
response=requests.get(url=url)
datasoup=BeautifulSoup(response.text,'lxml')


print datasoup.select('body > div.content > div.shishiimportantnews > div.left > div.bingtuan > div.title')[0].text
print datasoup.select('body > div.content > div.shishiimportantnews > div.left > div.bingtuan > div.bingtuanxinxi')[0].text.split(u'作者：')[1].split(' ')[0]
print datasoup.select('body > div.content > div.shishiimportantnews > div.left > div.bingtuan > div.bingtuanxinxi > a')[0].text
content=''
for content_p in datasoup.select('body > div.content > div.shishiimportantnews > div.left > div.bingtuan > div.networkinformation > p'):
    content+= content_p.text
    print content_p.text

print content
