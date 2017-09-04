import requests
from bs4 import BeautifulSoup

headers={
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}
response1=requests.get(url='http://m.thepaper.cn/newsDetail_forward_1781497',headers=headers)
# response1=requests.get(url='http://bbs1.people.com.cn/posts/Y0/09/AB/68/BD/content_html.txt')
# response1.encoding='utf-8'
# print response1.text

datasoup=BeautifulSoup(response1.text,'lxml')
# print datasoup.select('.replayInfo .float_l.mT10')[0].text.split(u'\xa0')[-1]
# print datasoup.select('.outer h2')[0].text
# print datasoup.select('.outer h2')[1]
print datasoup.select('.news_content .about_news')[1].text.split(u'\xa0')[0]