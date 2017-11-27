#_*_coding:utf-8_*_
from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup
from w3lib.url import urljoin
import datetime




basic_url='http://bts.gov.cn/'

def get_index(contentqueue):

    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    }
    urls=['http://bts.gov.cn/xw/gjgn/']#国内
    url2=['http://bts.gov.cn/xw/zdxw/']#师事
    url3=['http://www.bts.gov.cn/zcms/']#部门动态
    url4=['http://bts.gov.cn/xw/zsjg/']#直属单位
    url5=['http://bts.gov.cn/xw/gjgn/']
    url6=['http://bts.gov.cn/xw/qt/']#其它
    url7=['http://www.bts.gov.cn/gk/tzgg/']#通知公告
    url9=['http://www.bts.gov.cn/gk/rsxx/']#人事信息
    url10=['http://www.bts.gov.cn/gk/ywgz/']#业务工作
    url11=['http://www.bts.gov.cn/gk/wjzc/']#文件政策
    url12=['http://www.bts.gov.cn/gk/zcjd1/']#政策解读
    url13=['http://www.bts.gov.cn/gk/tjxx/']#统计信息


    urls_all=urls+url2+url3+url4+url5+url6+url7+url9+url10+url11+url12+url13

    for one_url in urls_all:
        response1=get_response_and_text(url=one_url,headers=headers,charset='utf-8')
        response_in_fucntion=response1['response_in_function']
        if not response_in_fucntion:
            continue
        response_in_fucntion_text=response1['response_in_function_text']
        datasoup=BeautifulSoup(response_in_fucntion_text,'lxml')
        try:
            for one_li in datasoup.select(
                    'body > div.mainBg > div.listMain.pageWidth.clearself > div.ListRightContent.clearself > div.docuContent.listul > ul > li'):
                # print one_li.text
                url_raw = one_li.select('a')[0].get('href')
                title = one_li.select('a')[0].text.strip()
                url_end = urljoin(basic_url, url_raw)
                id=url_end.split('/')[-1].split('.')[0]

                if 'bts.gov.cn' in url_end:
                    print url_end

                print title
                # print one_li.select('a')[1].text#publish_time//2017-04-04
                index_dict={
                    'title':title,
                    'url':url_end,
                    'id':id,
                    'spider_time':datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'parent_id':id,
                }
                contentqueue.put(index_dict)
        except Exception as e:
            print e
            print one_url
