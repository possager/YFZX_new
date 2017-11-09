import requests
from bs4 import BeautifulSoup
from visit_page4 import get_response_and_text
import datetime
import re



def get_index(index_queue):
    index_urls=['http://www.ibeitun.net/{}.html'.format(str(i)) for i in range(1,2070)]
    for url in index_urls:
        index_queue.put(
            {
                'url':url,
                'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'id':url.split('/')[-1].split('.')[0]
            }
        )


def get_index2(index_queue):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    index_page_1_url='http://www.ibeitun.net/xinxi/s0_a0_m0_p1.html'
    response1=get_response_and_text(url=index_page_1_url,headers=headers)
    response_in_function=response1['response_in_function']
    response_in_function_text=response1['response_in_function_text']
    if not response_in_function:
        return
    datasoup=BeautifulSoup(response_in_function_text,'lxml')
    url_list_div= datasoup.select('div.indexMessBox')
    Re_find_all_url=re.compile(r'\<a href\=\"(\/\d{4,5}.html)"')
    url_list=Re_find_all_url.findall(str(url_list_div))
    for i in url_list:
        url='http://www.ibeitun.net'+str(i)
        index_queue.put(
            {
                'url': url,
                'spider_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'id': url.split('/')[-1].split('.')[0]
            }
        )
    # print url_list

if __name__ == '__main__':
    get_index2(index_queue=None)