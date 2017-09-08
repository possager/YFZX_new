#_*_coding:utf-8_*_
from bs4 import BeautifulSoup
import requests
import re

# html_raw=requests.get(url='http://m.xilu.com/v/1000030000012866.html')
html_raw=requests.get(url='http://m.xilu.com/v/1000010001006753.html')


Re_find_time=re.compile(r'((201\d)[\/-](\d{2})(\d{2}))')
Re_find_time2=re.compile(r'(20\d{2}\-\d{1,2}-\d{1,2})')
datasoup=BeautifulSoup(html_raw.text,'lxml')



this_div=datasoup.select('.art_txt')[0]
this_div_str=str(this_div)
print Re_find_time2.findall(this_div_str)



# pic_div=datasoup.select('.hdp-box')[0]
# pic_div_str= str(pic_div)
# Re_sub=re.compile(r'(201\d[\/-]\d{2}\d{2})')
#
# one_split= Re_find_time.findall(pic_div_str)[0]
# print one_split[1]+'-'+one_split[2]+'-'+one_split[2]