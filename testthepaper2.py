#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import re



url1='http://bbs.csdn.net/topics/392208919'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

response1=requests.get(url=url1)
# print response1.text

datasoup=BeautifulSoup(response1.text,'lxml')

# for dl in datasoup.select('.dropdown-menu a[href]'):
#     # for a in dl.:
#     #     print
#     print dl
#     print dl.get('href')

# for i in  datasoup.select('.content > table > tr')[1:-1]:
#
#     print i.select('td.title > a[title]')[0].text.strip()#title
#     print 'http://bbs.csdn.net'+i.select('td.title > a[title]')[0].get('href').strip()#title
#     print i.select('td.tc a[title]')[0].get('title').strip()#publish_user
#     print i.select('td.tc a[title]')[0].get('href')#publish_user_href
#     print i.select('td:nth-of-type(4)')[0].text#read_count
#     print '\n'

#
# nextpage= datasoup.select('a.next')
# if nextpage:
#     print 'http://bbs.csdn.net'+nextpage[0].get('href')
#     print i.select('td')
#     print i.select('')

Re_find_img_url = re.compile(r'src="(.*?)"')

# print response1.text
for i in datasoup.select('div.detailed table.post'):
    # print i.select('tr')
    print '\n'
    j= i.select('div.post_body')
    # print i.select('.user_info .user_head img')[0].get('src')

    print j[0].text.strip()#content
    img_urls=Re_find_img_url.findall(str(j))
    img_urls2=[]
    for img_url_maybe_have_js in img_urls:
        if '.js' not in  img_url_maybe_have_js:
            img_urls2.append(img_url_maybe_have_js)
    print 'this is img_urls---',img_urls2

    print i.select('.user_info .user_head a')[0].get('href')#publish_user_photo
    print i.select('.user_info .nickname span')[0].text#已经有了
    print i.select('.time')[0].text.strip().split('\n')[1].strip()#publish_time
    try:
        print i.select('.data .fr a[href]')[0].get('href')#楼层的

        print i.select(' div.control .fr a.red')[0].text.split('[')[1].split(']')[0]
        print i.select(' div.control .fr a.bury')[0].text.split('[')[1].split(']')[0]
        # print i.select(' div.control .fr a.quote')[0].text.split('[')[1].split(']')[0]
        # print i.select(' div.control .fr a.fancybox')[0].text.split('[')[1].split(']')[0]
        # print i.select('')
    except Exception as e:
        print e


