from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup
import json
import requests


def get_index(content_queue):
    # url=data['url']
    outside_url=['http://186t.ibeitun.net/news.aspx?s=0&p={}'.format(str(i)) for i in range(1,5)]


    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    for url in outside_url:
        response1=get_response_and_text(url=url,headers=headers)
        response_in_function=response1['response_in_function']
        response_in_function_text=response1['response_in_function_text']
        # response1=requests.get(url=url,headers=headers)
        # response_in_function_text=response1.text
        datasoup=BeautifulSoup(response_in_function_text,'lxml')

        for one_title in datasoup.select('div.main.fixed > div.right.wow.fadeInUp > ul > li'):
            url= 'http://186t.ibeitun.net'+one_title.select('a')[0].get('href')
            publish_time= one_title.select('a span')[0].text.strip()+' 00:00:00'
            title= one_title.select('a div')[0].text.strip()

            one_dict={
                'url':url,
                'publish_time':publish_time,
                'title':title,
                'id':url.split('mid=')[1],
            }
            content_queue.put(one_dict)



if __name__ == '__main__':
    get_index()