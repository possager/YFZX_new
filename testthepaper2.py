import requests
from bs4 import BeautifulSoup


headers={
    'User-Agent':"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
}

response1=requests.get(url='http://m.thepaper.cn/newsDetail_forward_1765057',headers=headers)
# print response1.text
datasoup=BeautifulSoup(response1.text,'lxml')
for content in  datasoup.select('#v3cont_id > div.news_content > div.news_part'):
    print content.text
print datasoup.select('#v3cont_id > div.news_content > h1')[0].text#title
print datasoup.select('#v3cont_id > div.news_content > p.about_news')[0].text
print datasoup.select('#v3cont_id > div.news_content > p.about_news')[1].text