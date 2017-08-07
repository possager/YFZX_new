#_*_coding:utf-8_*_
import requests
import re
import json
from bs4 import BeautifulSoup

sessopm1=requests.session()
url='http://www.toutiao.com/a6434708385005830402/'

headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

response=sessopm1.request(method='get',headers=headers,url=url)
# print response.text

Re_find_qid=re.compile(r'qid: \'.*?\'')
result_re=Re_find_qid.findall(response.text)
qid= result_re[0].split("'")[1]
commenturl='https://www.wukong.com/wenda/web/question/loadmorev1/?count=10&qid='+qid+'&offset=10&req_type=1'

print commenturl

response2=sessopm1.request(method='get',url=commenturl,headers=headers)
# print response2.text
datajson=json.loads(response2.text)
for i in  datajson['data']['ans_list']:
    print i
#请求comment的url里边有一个是有html的，一个是只有评论数据的
#https://www.wukong.com/wenda/web/comment/brow/?ansid=6420334226893177090&count=10&offset=0&t=1502039743713#json格式的评论数据
#https://www.wukong.com/answer/6420334226893177090/?showComment=6420334226893177090#有评论的url
#https://www.wukong.com/wenda/web/question/loadmorev1/?count=10&qid=6407060007531053314&offset=10&t=1502038242559&req_type=1



#普通内容的评论链接：http://www.toutiao.com/api/comment/list/?group_id=6451171041971962125&item_id=6450423345560158734&offset=5&count=10   这里边的groupid和item_id都是一样的
response3=sessopm1.request(method='get',url='http://www.toutiao.com/a6450982841744408845/',headers=headers)
response3.encoding='utf-8'
Re_find_itmeId = re.compile(r'item_id:\'.*?\'')

# datajson3=json.loads(response3.text)
# print datajson3
# print datajson3['data']['has_more']
# if datajson3['data']['has_more']:
#     print 'yes'
# else:
#     print 'no'
datasoup=BeautifulSoup(response3.text,'lxml')

print Re_find_itmeId.findall(response3.text)