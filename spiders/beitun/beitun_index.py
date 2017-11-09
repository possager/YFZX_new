from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup


def get_index(url,content_queue):
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    response1=get_response_and_text(url=url,headers=headers)
    response_in_function=response1['response_in_function']
    response_in_function_text=response1['response_in_function_text']
    try:
        datasoup=BeautifulSoup(response_in_function_text,'lxml')
    except Exception as e:
        return 
    for i in datasoup.select('body > div.content > div.shishiimportantnews > div.left > ul > li'):
        publish_time= i.select('span')[0].text
        url= i.select('a')[0].get('href')
        title= i.select('a')[0].get('title')
        datadict={
            'publish_time':publish_time,
            'url':url,
            'title':title,
            'id':url.split('id=')[0],
        }
        content_queue.put(datadict)