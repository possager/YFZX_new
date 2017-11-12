#_*_coding:utf-8_*_
import requests
from bs4 import BeautifulSoup
import re



def get_content(result_queue,data):
    # url='http://186t.ibeitun.net/shownews.aspx?mid=340'
    url=data['url']


    Re_find_img = re.compile(r'src\=\"(.*?)\"')

    response = requests.get(url=url)
    # print response.text
    datasoup = BeautifulSoup(response.text, 'lxml')
    content_soup = datasoup.select('div.rightBox')[0]
    print '\n---------------------------------------------------------'
    publish_user_time = content_soup.select('div,downLoadTit div.cource')[0].text
    publish_user_time_split = publish_user_time.split(u'编辑：')[1].split(u'时间：')
    publish_user= publish_user_time_split[0].strip()
    publish_time= publish_user_time_split[1].strip() + ' 00:00:00'
    content= content_soup.select('div.content.fixed')[0].text

    img_urls=[]
    img_urls_re = Re_find_img.findall(str(content_soup))
    for i in img_urls_re:
        img_urls.append(i)

    data['img_urls']=img_urls
    data['content']=content
    # data['publish_time']=publish_time
    data['publish_user']=publish_user

    result_queue.put(data)



if __name__ == '__main__':
    get_content(content_queue=None)