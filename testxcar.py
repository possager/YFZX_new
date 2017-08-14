import requests
import cookielib
from visit_page import get_response_and_text
from bs4 import BeautifulSoup
import html5lib



headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
}
response1=get_response_and_text(url='http://www.xcar.com.cn/bbs/forumdisplay.php?fid=192',headers=headers)
response_in_function_text= response1['response_in_function_text']
datasoup=BeautifulSoup(response_in_function_text,'lxml')
# print response_in_function_text

# print str(datasoup)
for url in  datasoup.select('body > form > div > div > div.table-section > div.plr20 > dl'):
    print url.select('dt > p > a')[0].text
    print url.select('dd.w98 > a')[0].text
    print url.select('dd.w98 > span')[0].text


# for i in datasoup.select('div.post-list > div.table-section > div.plr20 > dl'):
    # print i

# print datasoup



# response1=requests.get(url='http://www.xcar.com.cn/bbs/forumdisplay.php?fid=192')
# print response1.text