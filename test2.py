import requests
from bs4 import BeautifulSoup
import re
import json




session1=requests.session()
headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
response1=session1.request(method='get',url='https://apiv2.sohu.com/api/topic/load?page_size=10&topic_source_id=505790957&page_no=10&hot_size=5',headers=headers)
# print response1.text
# datasoup=BeautifulSoup(response1.text,'lxml')
# print str(datasoup)
# Re_find_img=re.compile(r'img src=".*?"')
# for i in Re_find_img.findall(response1.text):
#     print i.split('"')[1]


#https://m.sohu.com/cm/162897783_313745?_f=m-channel_8_feeds_290
#https://m.sohu.com/a/162897783_313745?_f=m-channel_8_feeds_290

datajson=json.loads(response1.text)
print datajson
for one in datajson['jsonObject']['comments']:
    print one
    # print one['authorName']
    # print one['']
# print response1.text
# datasoup=BeautifulSoup(response1.text,'lxml')
# for i in datasoup.select('#articleContent > div.display-content > p'):
#     print i.text
#
# for j in datasoup.select('#articleContent > div.display-content'):
#     print j