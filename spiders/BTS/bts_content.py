#_*_coding:utf-8_*_
from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup
import re
from w3lib.url import urljoin




def get_content(data,result_queue):
    url=data['url']
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    basic_url='http://bts.gov.cn/'
    Re_sub_javascript2 = re.compile(r'<script[\S|\s]*?>[\s|\S]*?<\/script\>')
    Re_find_time = re.compile(r'(\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2})')
    Re_find_img = re.compile(r'src\=\"(.*?)\"')
    Re_find_cource = re.compile(ur'来源：(.*?) ')

    try:
        response1=get_response_and_text(url=url,headers=headers,charset='utf-8')
        response_in_function=response1['response_in_function']
        if not response_in_function:
            return
        response_in_function_text=response1['response_in_function_text']
        response_in_function_text_dealed=Re_sub_javascript2.sub('',response_in_function_text)
        datasoup=BeautifulSoup(response_in_function_text_dealed,'lxml')
        title= datasoup.select('body > div > div.detailMain.pageWidth > div.pargraph > h1')[0].text
        content = ''
        for i in datasoup.select('body > div > div.detailMain.pageWidth > div.pargraph  div.detailPar  p'):
            content += i.text
        # print content
        source=Re_find_cource.findall(response_in_function_text_dealed)
        if source:
            source=source[0]
        else:
            source=''
        content_str = datasoup.select('body > div.mainBg > div.detailMain.pageWidth > div.pargraph > div.detailPar')[0]
        content_str2 = str(content_str)
        img_urls = Re_find_img.findall(content_str2)
        img_urls2 = []
        for one_img_url in img_urls:
            img_url_dealed = urljoin(basic_url, one_img_url)
            img_urls2.append(img_url_dealed)


        publish_div = datasoup.select('body > div > div.detailMain.pageWidth > div.pargraph > h6')[0].text
        publish_time= Re_find_time.findall(publish_div)[0]

        data['content']=content
        data['publish_time']=publish_time
        data['img_urls']=img_urls2
        data['source']=source

        pass
        result_queue.put(data)
    except Exception as e:
        print e


if __name__ == '__main__':
    # get_content(data={
    #     'url':'http://bts.gov.cn/c/2017-11-22/2101226.shtml'
    # },result_queue=None)
    pass