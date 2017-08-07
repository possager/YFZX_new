import requests
from bs4 import BeautifulSoup
import re



session1=requests.session()
headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
response1=session1.request(method='get',url='http://m.sohu.com/n/505757224/',headers=headers)
# print response1.text
datasoup=BeautifulSoup(response1.text,'lxml')
print str(datasoup)
Re_find_img=re.compile(r'img src=".*?"')
for i in Re_find_img.findall(response1.text):
    print i.split('"')[1]