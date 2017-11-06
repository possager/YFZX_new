#_*_coding:utf-8_*_
from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup
import traceback


def get_content(data,result_queue):
    try:
        url=data['url']
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'connection': 'close',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        }
        if 'nssbt' not in url:
            return
        response1=get_response_and_text(url=url,headers=headers)
        response_in_function=response1['response_in_function']
        response_in_function_text=response1['response_in_function_text']
        if not response_in_function:
            return
        datasoup=BeautifulSoup(response_in_function_text,'lxml')

        # title= datasoup.select('body > div.content > div.shishiimportantnews > div.left > div.bingtuan > div.title')[0].text

        try:
            publish_user=datasoup.select('body > div.content > div.shishiimportantnews > div.left > div.bingtuan > div.bingtuanxinxi')[
                0].text
        except Exception as e:
            print url
        try:
            publish_user.split(u'作者：')[1].split(' ')[0]
        except Exception as e:
            print e
            try:
                print publish_user
            except:
                pass
        source=datasoup.select('body > div.content > div.shishiimportantnews > div.left > div.bingtuan > div.bingtuanxinxi > a')[
            0].text
        content = ''
        for content_p in datasoup.select(
                'body > div.content > div.shishiimportantnews > div.left > div.bingtuan > div.networkinformation > p'):
            content += content_p.text


        data['publish_user']=publish_user
        data['source']=source
        data['content']=content

        result_queue.put(data)
        # print data
        # print 'send to result_queue one!!!!!!!'
    except Exception as e:
        # traceback.extract_stack()
        print e