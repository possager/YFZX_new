#_*_coding:utf-8_*_
import  requests
from bs4 import BeautifulSoup


url1='http://www.chengshiluntan.com/5931287-1.html'
response1=requests.get(url=url1)

datasoup=BeautifulSoup(response1.text,'lxml')



print datasoup.select('#thread_subject')[0].text

print datasoup.select('#postlist > div.bm_h.comiis_snvbt > span.y.comiis_hfs > strong')[0].text
print datasoup.select('#postlist > div.bm_h.comiis_snvbt > span.y.comiis_cks > strong')[0].text

for one_comment_div in datasoup.select('#postlist > div[id]')[:-1]:
    # print one_comment_div.select('')
    print '\n\n'
    print one_comment_div.select('tr:nth-of-type(1) > td.plc > div.pi > div.pti > div.authi > a.xi2.kmyzz')[0].text#publish_user
    print one_comment_div.select('tr:nth-of-type(1) > td.plc > div.pi > div.pti > div.authi  > em')[0].text.replace(u'发表于','').strip()#pubtlish_time
    print one_comment_div.select(' div.t_fsz > div.t_f')[0].text.strip()#content
    if one_comment_div.select('div.cm')[0].text.strip():
        print 'has comments---------!!!!----------'
        # print one_comment_div.select('div.cm')[0].text
        print '现在在评论里了'
        print one_comment_div.select('div.cm')[0].get('id')#comment_id
        print one_comment_div.select('div.cm div.pstl div.psta a > img')[0].get('src')#publish_photo
        print one_comment_div.select('div.pstl div.psti')[0].text.split(u'详情')[0].strip()#content
        print one_comment_div.select('div.pstl div.psta a.xi2')[0].text#publish_user
        print one_comment_div.select('div.pstl div.psti span.xg1')[0].text.replace(u'发表于','').strip()#publish_time
    try:
        print one_comment_div.select('td.pls > div.pls')[0].get('id')#id
        print one_comment_div.select('td.pls > div.pls div div.avatar a img')[0].get('src')#publish_user_photo
        print one_comment_div.select('td.pls > div.pls div.m.z div[id]')[0].get('id')#publish_user_id


    except Exception as e:
        print e