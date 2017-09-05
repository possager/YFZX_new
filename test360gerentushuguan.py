#_*_coding:utf-8_*_
import requests
import time
from visit_page import get_response_and_text
import json
from bs4 import BeautifulSoup
import requests
import json
import re




urls2=[
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=7&subClassId=0&nType=10&iIscream=0&iSort=1&nPage=%s&nType=11'%(str(i) for i in range(0,500)),
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=6&subClassId=0&iIscream=0&iSort=1&nPage={}&nType=11'.format(str(i) for i in range(0,500)),
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=10&subClassId=0&iIscream=0&iSort=1&nPage=1&nType=11',#
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=10&subClassId=0&iIscream=0&iSort=1&nPage=300&nType=11',#健康
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=3&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11',#职场
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=440&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11',#财经
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=5&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11',#娱乐
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=1&subClassId=0&iIscream=0&iSort=1&nPage=1&nType=11',#艺术
            'http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=12&subClassId=0&iIscream=0&iSort=1&nPage=2&nType=11',#上网

        ]

url1=urls2[0]
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

# response=requests.request(method='get',url=url1,headers=headers)
# session1=requests.session()
# response=session1.request(method='get',url='http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=6&subClassId=0&iIscream=0&iSort=1&nPage=3&nType=11',headers=headers)
# response.close()


# print response.text

# data_response= get_response_and_text(url=url1,headers=headers)['response_in_function_text']
# print data_response

# datajson=json.loads(response.text)
#
# for i in datajson[0]['data']:
#     print i['StrArtidetitle']#title
#     print i['StrDescription']#简述
#     print i['StrSaveDate']+' 00:00:00'#publish_time
#     print i['StrSaverUserId']#publish_user_id
#     print i['StrSource']#publish_user
#     print i['StrUrl']#url
#     print i['StrUserName']#publish_user
#     print i['StrSaverNum']#转载数量
#     print i['StrArtideid']
#     print '--------------------------------------------------------------'
# for i in urls2:
#     print i

# urls3=['http://www.360doc.com/ajax/ReadingRoom/getZCData.json?artNum=20&classId=7&subClassId=0&nType=10&iIscream=0&iSort=1&nPage=%s&nType=11'%str(i) for i in range(100)]
#
# url4=[i for i in range(10)]
# print url4
# for i in urls3:
#     print i

urls1111='http://www.360doc.com/content/17/0827/08/1302411_682432381.shtml'
# urls1111='http://www.360doc.com/content/17/0902/06/40167318_684060643.shtml'
# resposne1=get_response_and_text(urls1111)
# response_in_function_text= resposne1['response_in_function_text']
session1=requests.session()
response2=session1.request(method='get',url=urls1111,headers=headers)
# session1.close()
response_in_function_text=response2.text
datasoup=BeautifulSoup(response_in_function_text,'lxml')
# print datasoup
print datasoup.select('#titiletext')[0].text#title

Re_find_img_url = re.compile(r'src="(.*?)"')
test1=str(datasoup.select('#artContent')[0])

img_list=Re_find_img_url.findall(test1)
for i in img_list:
    print i

print datasoup.select('#artContent')[0].text.strip()#content
# print datasoup.select('#360doc_Readnum')[0].text#read_num
response_read_num=session1.request(method='get',url='http://webservice.360doc.com/GetArtInfo20130912NewV.ashx?UID=-100,40167318,GetBookTwo,684060643,0,0@cg@0&jsoncallback=jsonp')

json_raw= response_read_num.text.split('Resp(')[1].split(",'jsonp'")[0].split('@c@g@tl@c@g@t')[1].split('l@c@g@t')[0]
# for i in datasoup.select('div > div > p'):
#     print i.text.strip()

print json_raw
# datajsona=json.loads(json_raw)