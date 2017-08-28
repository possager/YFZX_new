#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import re

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
}

url5='http://www.thepaper.cn/load_moreFloorComment.jsp?contid=1774002&hotIds=12433548,12433083,12433687,12433684,12433670&pageidx=5&startId=12434342'
url3='http://www.thepaper.cn/load_moreFloorComment.jsp?contid=1774002&hotIds=12433548,12433083,12433687,12433684,12433670&pageidx=3&startId=12434373'
url4='http://www.thepaper.cn/load_moreFloorComment.jsp?contid=1774002&hotIds=12433548,12433083,12433687,12433684,12433670&pageidx=4&startId=12434357'


# response1=requests.get(url=url4,headers=headers)
# # print response1.text
# datasoup=BeautifulSoup(response1.text,'lxml')
# Re_find_publish_user=re.compile(ur'回复@(.*)\:')
# for i in  datasoup.select('div.comment_que > div > div.aqwright > div > a[href^=javascript:replyFloo]'):
#     # print i.text
#     result_re=Re_find_publish_user.match(i.text)
#     if result_re:
#         print result_re.group(1)

a=[1,2,3,4]
b=a[:]
for i in range(len(a)):
    a[i]+=1
print a