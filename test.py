#_*_coding:utf-8_*_
import time
import requests
import json
import re
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup


headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            # 'X-Requested-With':'XMLHttpRequest',#重要
            # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            # 'Accept-Encoding':'gzip, deflate, sdch',
            # 'Accept-Language':'zh-CN,zh;q=0.8',
            # 'Cache-Control':'max-age=0',
            # 'Connection':'keep-alive',
            # 'Host':'m.xilu.com',
            # 'Upgrade-Insecure-Requests':'1'

        }

session1=requests.session()
response_data=session1.request(method='get',url='http://www.toutiao.com/a6373916953177751810/')#http://www.toutiao.com/a6449864567698866445/


print response_data.text


Re_find_atricle=re.compile(r"__question = .*?\|\| \[\]\;")
Re_find_answer=re.compile(r"__answer = .*?\|\| \[\]\;")

response_data.encoding='utf-8'
# print response_data.text
result =  Re_find_atricle.findall(response_data.text)[0]
question_origion= result.replace(' || [];','').replace('__question = ','')
datajson= json.loads(question_origion)

print datajson[0]['content']['text']

answer= Re_find_answer.findall(response_data.text)
datajson2=answer[0]
datajson2= datajson2.replace(' || [];','').replace('__answer = ','')
datajson2=json.loads(datajson2)
print datajson2