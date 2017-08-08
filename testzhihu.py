import requests
import cookielib
import time
from bs4 import BeautifulSoup
import socket


# cookiejar1=cookielib.MozillaCookieJar()
session1=requests.session()
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.57 Safari/534.24',#Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'www.zhihu.com',
    'Origin':'https://www.zhihu.com',
    'Referer':'https://www.zhihu.com/explore/recommendations',
    'X-Requested-With':'XMLHttpRequest',
    # 'X-Xsrftoken':'537c9ca88eb28de88f5582b6415d88a9',
    # 'Cookie':'aliyungf_tc=AQAAAC+avQQTbAgAwbnU3nxmUomJtIiu; l_n_c=1; q_c1=872c85171d95441286e6730b8c5e74c4|1502180994000|1502180994000; _xsrf=b8edcf2172dcaa20f6c46cd68bfa02ab; r_cap_id="NjNlMjA3YmZhZTFiNDg3ZWEzNzcyZDI2NDc4NDA3N2M=|1502180994|80a81b477f141db5e5896d4882f61ad4f89413c2"; cap_id="M2UwN2VhZDNkMGQ0NDU2ZDk1NGY5OWExMzY3YWYyNzc=|1502180994|fe6625ddf00af2b730027fe37e8c2c131c6827e6"; l_cap_id="MTVkMzk5NjcxMTVmNDgwODhhNjdhMGFjZDQ5NjJiZmE=|1502180994|39dce4c9c58a33879ab7f611161fbe6f6efd8682"; d_c0="AIBChmdRMAyPTnIzb2EkJK4JD7e2P7EQRQ8=|1502180995"; _zap=6f048c2f-4eef-4701-b29f-c3685ad5ee14; n_c=1; __utma=51854390.1308714305.1502180983.1502180983.1502180983.1; __utmb=51854390.0.10.1502180983; __utmc=51854390; __utmz=51854390.1502180983.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20170808=1'
}


body={
    'method':'next','params':"{'limit':20,'offset':20}"
      }

response2=session1.post(url='https://www.zhihu.com/node/ExploreRecommendListV2',headers=headers,data=body)
print response2.text
print requests.post(url='https://www.zhihu.com/node/ExploreRecommendListV2',headers=headers,data=body).text



# response2=session1.
# print response2.elapsed
# print response2.text


# socket1=socket.socket()
# socket1.connect(('118.178.213.186',443))
# conn,data= socket1.accept()
# for i in conn.accept():
#     print i