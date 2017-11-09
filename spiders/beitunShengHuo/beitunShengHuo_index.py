import requests
from bs4 import BeautifulSoup
from visit_page4 import get_response_and_text
import datetime



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