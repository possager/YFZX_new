#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import datetime
import datetime
import re


#http://e.chengdu.cn/html/2017-10/10/node_2.htm

headers={
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }
response=requests.get(url='http://e.chengdu.cn/html/2017-10/10/content_607885.htm',headers=headers)
response.encoding='utf-8'
# print response.text
datasoup=BeautifulSoup(response.text,'lxml')
# url_pre='http://e.chengdu.cn/html/'
# datetime= datetime.datetime.now().strftime('%Y-%m/%d')
# for i in datasoup.select('#nowPageArticleList li a'):
#     print url_pre+datetime+'/'+i.get('href')


Re_find_time=re.compile(ur'(\d{4}年\d{1,2}月\d{1,2}日)')
Re_find_publish_user=re.compile(ur'\d{4}年\d{1,2}月\d{1,2}日([\s|\S]*?)')


print datasoup.select('div.content-news div.content-title > h4')[0].text
print '\n'
for i in datasoup.select('td.xilan_content_tt p'):
    print i.text.strip()
div_contain_time= datasoup.select('div.content-info')[0].text

print div_contain_time
print Re_find_time.findall(div_contain_time)[0]
print div_contain_time.split(u'\xa0')[1].strip()


content_div=datasoup.select('div.content-news')[0]
Re_find_img_url = re.compile(r' src="(.*?)"')
img_list= Re_find_img_url.findall(str(content_div))
img_set=set()
for imgurl in img_list:
    img_set.add(imgurl.replace('../../..','http://e.chengdu.cn'))

for url in list(img_set):
    print url