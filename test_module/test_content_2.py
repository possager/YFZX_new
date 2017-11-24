#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import re
from w3lib.url import urljoin


Re_sub_javascript2=re.compile(r'<script[\S|\s]*?>[\s|\S]*?<\/script\>')
Re_find_time=re.compile(r'(\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2})')
Re_find_img=re.compile(r'src\=\"(.*?)\"')
Re_find_cource=re.compile(ur'来源：(.*?) ')



# response1=requests.get(url='http://www.bts.gov.cn/c/2017-09-08/2066049.shtml')
# response1=requests.get(url='http://bts.gov.cn/c/2017-11-13/2095430.shtml')
# response1=requests.get(url='http://bts.gov.cn/c/2017-11-22/2101226.shtml')
response1=requests.get(url='http://bts.gov.cn/c/2017-11-08/2094367.shtml')
response1.encoding='utf-8'
response_text=response1.text
basic_url='http://bts.gov.cn/'

content1=Re_sub_javascript2.sub('',response1.text)



datasoup=BeautifulSoup(content1,'lxml')
print datasoup.select('body > div > div.detailMain.pageWidth > div.pargraph > h1')[0].text
content=''
for i in  datasoup.select('body > div > div.detailMain.pageWidth > div.pargraph  div.detailPar  p'):
    content+= i.text

source=Re_find_cource.findall(response_text)
print source[0]



content_str=datasoup.select('body > div.mainBg > div.detailMain.pageWidth > div.pargraph > div.detailPar')[0]
content_str2=str(content_str)
img_urls=Re_find_img.findall(content_str2)
print img_urls
img_urls2=[]
for one_img_url in img_urls:
    img_url_dealed=urljoin(basic_url,one_img_url)
    img_urls2.append(img_url_dealed)
print img_urls2
print content
publish_div= datasoup.select('body > div > div.detailMain.pageWidth > div.pargraph > h6')[0].text
print Re_find_time.findall(publish_div)[0]
