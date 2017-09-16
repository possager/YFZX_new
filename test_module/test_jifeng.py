#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import json
import re


url_test='http://bbs.gfan.com/android-8483949-1-1.html'

Re_find_url_bankuai=re.compile(r'(http://bbs\.gfan\.com/forum-\d{2,4}-1\.html)')

# data_response=requests.get(url=url_test)
# data_response_text=data_response.text
# url_bankuai= Re_find_url_bankuai.findall(data_response_text)
# print len(url_bankuai)
# print len(set(url_bankuai))
#
# for i in list(set(url_bankuai)):
#     print i
# print list(set(url_bankuai))

response1=requests.get(url=url_test)
# print response1.text

# Re_sub_publish_time=re.compile(r'<i class="pstatus">.*?<\/i>')

# content_no_publish_info=Re_sub_publish_time.sub('',response1.text,0)

def deal_content(content):
    Re_sub_publish_time = re.compile(r'<i class="pstatus">.*?<\/i>')
    content = Re_sub_publish_time.sub('', content)

    Re_sub_style=re.compile(r'<style.*?>[\s|\S]*?<\/style>')
    content=Re_sub_style.sub('',content)

    Re_sub_script=re.compile(r'<script[\s|\S]*?\>?[\S|\s]<\/script>')
    content=Re_sub_script.sub('',content)



    return content



content_dealed=deal_content(response1.text)

# print content_dealed



datasoup=BeautifulSoup(content_dealed,'lxml')
# print datasoup.select('.nxt')
#
# for i in  datasoup.select('#moderate  tbody')[1:]:
#     print '\n\n'
#     print i.select('th > a')[0].text #title
#     print i.select('td.by a')[0].text #publish_user
#     print i.select('td.by a')[0].get('href') #publish_user_url
#     print i.select('td.by em span')[0].text+':00' #publish_time
#     print i.select('td.num a')[0].text #reply_count
#     print i.select('td.num em')[0].text #view_num
#     print i.select('th > a')[0].get('href') #url
#
# print datasoup.select('.nxt')[0].get('href')

Re_find_img_url = re.compile(r'file="(.*?)"')
img_may_no_user=['http://image.gfan.com/static/image/common/rright.gif', 'http://image.gfan.com/static/image/common/none.gif', 'http://image.gfan.com/static/image/common/rleft.gif']
print list(set(img_may_no_user))

for one_div in  datasoup.select('#postlist > div[id]')[:-1]:
    print '\n\n\n'
    img_list = []
    print one_div.select('div.authi a')[0].text.strip()#publish_user
    # print one_div.text.strip()
    try:
        maybe_url_list= Re_find_img_url.findall(str(one_div.select('.t_fsz')[0]))
        for url_img_one in maybe_url_list:
            if url_img_one not in img_may_no_user:
                img_list.append(url_img_one)
        print img_list # img_list
        print one_div.select('.t_fsz')[0].text.strip() # content
        print one_div.select('.authi em')[0].text.replace(u'发表于 ','')+':00' # publish_time
        print one_div.select('div.avatar a img')[0].get('src') # publish_user_photo
        print one_div.select('.plc .pi strong a')[0].get('href').replace(';','&') #url
        print one_div.select('.plc .pi strong a')[0].get('id')#id
        print one_div.select('.plc .pi strong a')[0].get('id').replace('postnum','')#publish_user_id
        
        # print one_div.select('.plc .pi strong a')
        # print one_div.select('')

    except Exception as e:
        print e,'这里楼层数据被删除了'