import requests
from bs4 import BeautifulSoup
import json




# response1=requests.get(url='http://www.xjbtssbtszhdj.com/courier.frontPage.in?courTypeId=40286c8158a53e550158a548d80f000a')
# print response1.text

url1='http://www.xjbtssbtszhdj.com/courier.frontList.in?pageNum=1'
# url1='http://www.xjbtssbtszhdj.com/courier.frontAllPage.in?pageNum=1'
# url1='http://www.xjbtssbtszhdj.com/courier.frontAllList.in?pageNum=0&pageSize=15'

data={
    # 'courTypeId':'40286c8158a53e550158a548d80f000a',
    'pageSize':'15'
}
response1=requests.post(data=data,url=url1)
print response1.text
print response1.status_code

# datajson=json.loads(response1.text)
# print data