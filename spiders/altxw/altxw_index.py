#_*_coding:utf-8_*_

from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup
import datetime


def get_index(queue):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }

    urls1=['http://www.altxw.com/news/system/count//0012002/000000000000/000/001/c0012002000000000000_0000012{}.shtml'.format(str(i)) for i in range(55,58)]#
    urls2=['http://www.altxw.com/news/node_2031.htm']
    urls3=urls1+urls2
    urls3.append('http://www.altxw.com/gblw/index.shtml')

    for url in urls3:
        print url
        response1=get_response_and_text(url=url,headers=headers,charset='utf-8')
        if not response1['response_in_function']:
            continue
        response_in_function_text=response1['response_in_function_text']
        datasoup=BeautifulSoup(response_in_function_text,'lxml')
        for one_url_div in datasoup.select('div.bd > ul  li'):
            url= one_url_div.select('a')[0].get('href')
            if 'com' not in url:
                url='http://www.altxw.com/news/'+url
            if 'altxw.com/news/' not in url:
                continue
            title= one_url_div.select('a')[0].text.strip()
            # publish_time= '20'+one_url_div.select('span')[0].text.strip()+':00'
            publish_time=one_url_div.select('span')[0].text.strip()
            if len(publish_time.split('-')[0])<4:
                publish_time='20'+publish_time
            if len(publish_time)<11:
                publish_time+=' 00:00:00'
            elif 4<len(publish_time.split(u' ')[1])<8:
                publish_time=publish_time+':00'
            if len(publish_time)<18:
                print publish_time
            spider_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            id=url.split('/')[-1].split('.')[0]

            index_data_dict={
                'url':url,
                'title':title,
                'publish_time':publish_time,
                'spider_time':spider_time,
                'id':id,
                'parent_id':id,
                'publish_user':''
            }
            queue.put(index_data_dict)





if __name__ == '__main__':
    # get_index(url='http://www.altxw.com/news/system/count//0012002/000000000000/000/001/c0012002000000000000_000001255.shtml',queue=None)
    get_index(url='http://www.altxw.com/news/system/count//0012004/000000000000/000/000/c0012004000000000000_000000198.shtml',queue=None)

    #http://www.altxw.com/gblw/system/count//0003000/000000000000/000/000/c0003000000000000000_000000065.shtml干部论文2
    #http://www.altxw.com/gblw/index.shtml干部论文1
    #http://www.altxw.com/jsrw/index.shtml金山任务
    #http://www.altxw.com/news/node_2031_10.htm要问