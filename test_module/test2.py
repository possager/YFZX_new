import requests
from bs4 import BeautifulSoup
import re
import json




session1=requests.session()
headers={
    # 'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    # 'Accept-Encoding':'gzip, deflate',
    # 'Accept-Language':'zh-CN,zh;q=0.8',
    # 'Connection':'keep-alive',
    # 'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
response1=session1.request(method='get',url='http://www.toutiao.com/a6451941878181921293/#p=1',headers=headers)
response1.encoding='utf-8'
session1.close()
print response1.text







#https://apiv2.sohu.com/api/comment/list?page_size=10&topic_id=3613216966&page_no=2
# print response1.text
# datasoup=BeautifulSoup(response1.text,'lxml')
# print str(datasoup)
# Re_find_img=re.compile(r'img src=".*?"')
# for i in Re_find_img.findall(response1.text):
#     print i.split('"')[1]


#https://m.sohu.com/cm/162897783_313745?_f=m-channel_8_feeds_290
#https://m.sohu.com/a/162897783_313745?_f=m-channel_8_feeds_290

# datajson=json.loads(response1.text)
# print datajson
# for one in datajson['jsonObject']['comments']:
#     print one['content']
    # print one['authorName']
    # print one['']
# print response1.text
# datasoup=BeautifulSoup(response1.text,'lxml')
# for i in datasoup.select('#articleContent > div.display-content > p'):
#     print i.text
#
# for j in datasoup.select('#articleContent > div.display-content'):
#     print j