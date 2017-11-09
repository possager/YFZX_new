#_*_coding:utf-8_*_
from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup
import traceback



def get_content(data,result_queue):

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }

    url=data['url']
    response1=get_response_and_text(url=url,headers=headers)
    response_in_function=response1['response_in_function']
    response_in_function_text=response1['response_in_function_text']
    datasoup=BeautifulSoup(response_in_function_text,'lxml')
    # print str(datasoup)
    try:
        title= datasoup.select('div.main div.infobox h2.bt1')[0].text#title
        publish_time= datasoup.select('div.main div.infobox div.infoDate')[0].text.split('\n')[0].split(u'：')[1].strip()#publish_time
        read_count= datasoup.select('div.main div.infobox div.infoDate')[0].text.split('\n')[1].split(u'：')[1].strip()#read_count

        content= datasoup.select('#infobox > div.infoLeft > div.infoContent div.textwrap')[0].text
        img_urls=[]
        for picurl in datasoup.select('#infobox > div.infoLeft > div.infoContent div.picwrap a'):
            img_urls.append('http://www.ibeitun.net'+picurl.get('href'))


        # news_content={
        #     'title':title,
        #     'publish_time':publish_time,
        #     'read_count':read_count,
        #     'content':content,
        #     'img_urls':img_urls
        # }
        data['content']=content
        data['title']=title
        data['read_count']=read_count
        data['img_urls']=img_urls
        data['publish_time']=str(publish_time)+' 00:00:00'
        result_queue.put(data)
    except Exception as e:
        # print 'the error pages url is ------>',url
        # traceback.print_exc()
        return



if __name__ == '__main__':
    get_content({
        'url':'http://www.ibeitun.net/2066.html'
    })