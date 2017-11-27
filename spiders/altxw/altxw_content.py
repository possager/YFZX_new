#_*_coding:utf-8_*_

from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup
import datetime
import re
from w3lib.url import urljoin




def get_content(data,comment_queue):

    Re_find_img=re.compile(r'src\=\"(.*?)\"')


    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    basic_url='http://www.altxw.com/news/content/'


    url=data['url']
    response1=get_response_and_text(url=url,headers=headers,charset='utf-8')
    response_in_function=response1['response_in_function']
    if not response_in_function:
        return
    try:
        response_in_function_text= response1['response_in_function_text']
        datasoup=BeautifulSoup(response_in_function_text,'lxml')
        # title=datasoup.select('body > div.body > div > div.main.l > div > div > h1')[0].text()
        source=datasoup.select('body > div.body > div > div.main.l > div > div > div > li:nth-of-type(2)')[0].text.split(u'：')[1]
        content=''
        for i in datasoup.select('body > div.body > div > div.main.l > div > div > ul > p'):
            content += i.text
        content_div=datasoup.select('div > div.main.l > div > div > ul')[0]
        img_urls=Re_find_img.findall(str(content_div))
        img_urls2=[]
        for one_img_url in img_urls:
            one_img_url=urljoin(basic_url,one_img_url.strip('../'))
            img_urls2.append(one_img_url)
        print img_urls2
        data['source']=source
        data['content']=content
        data['img_urls']=img_urls2

        comment_queue.put(data)
    except Exception as e:
        print e



if __name__ == '__main__':
    get_content(data={'url':'http://www.altxw.com/news/content/2017-10/17/content_9496372.htm'},comment_queue=None)