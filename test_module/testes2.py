#_*_coding:utf-8_*_
import requests
import re
import json
from bs4 import BeautifulSoup
# from lxml import html
#
#
# response1=requests.get(url='http://bbs.csdn.net/topics/320264923')
#
# doc=html.fromstring(response1.text)
#
# print doc.xpath('head::text()')


thisdiv='''
<div class="li">
	<span class="money">中国</span>
	<!--<i></i>-->
	学习
</div>

'''

datasoup=BeautifulSoup(thisdiv,'lxml')
print datasoup.select('div')[0].text