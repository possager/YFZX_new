#_*_coding:utf-8_*_
import requests
import re
import json
from bs4 import BeautifulSoup

sessopm1=requests.session()
url='http://www.toutiao.com/a6452518585087558158/'

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}
response=sessopm1.request(method='get',headers=headers,url=url)

print response.text

Re_find_content=re.compile(r'content: \'.*?\'')
data_find_by_re=Re_find_content.findall(response.text)[0]
print data_find_by_re[0]