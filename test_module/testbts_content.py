#_*_coding:utf-8_*_

import requests
from bs4 import BeautifulSoup
from w3lib.url import urljoin




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
urls = ['http://bts.gov.cn/xw/gjgn/index_{}.shtml'.format(str(i)) for i in range(2, 13)]  # 国内
url2 = ['http://bts.gov.cn/xw/zdxw/index_{}.shtml'.format(str(i)) for i in range(2, 15)]  # 师事
url3 = ['http://www.bts.gov.cn/zcms/catalog/36384/pc/index_{}.shtml'.format(str(i)) for i in range(2, 200)]  # 部门动态
url4 = ['http://bts.gov.cn/xw/zsjg/index_{}.shtml'.format(str(i)) for i in range(2, 3)]  # 直属单位
url5 = ['http://bts.gov.cn/xw/gjgn/tcdt/index_{}.shtml'.format(str(i)) for i in range(2, 100)]
url6 = ['http://bts.gov.cn/xw/qt/']  # 其它
url7 = ['http://www.bts.gov.cn/gk/tzgg/index_{}.shtml'.format(str(i)) for i in range(2, 3)]  # 通知公告
url9 = ['http://www.bts.gov.cn/gk/rsxx/index_{}.shtml'.format(str(i)) for i in range(2, 3)]  # 人事信息
url10 = ['http://www.bts.gov.cn/gk/ywgz/index_{}.shtml'.format(str(i)) for i in range(2, 34)]  # 业务工作
url11 = ['http://www.bts.gov.cn/gk/wjzc/index_{}.shtml'.format(str(i)) for i in range(2, 13)]  # 文件政策
url12 = ['http://www.bts.gov.cn/gk/zcjd1/index_{}.shtml'.format(str(i)) for i in range(2, 9)]  # 政策解读
url13 = ['http://www.bts.gov.cn/gk/tjxx/']  # 统计信息

urls_all = urls + url2 + url3 + url4 + url5 + url6 + url7 + url9 + url10 + url11 + url12 + url13

basic_url='http://bts.gov.cn/'
for oneurl in url7:


    response=requests.get(url=oneurl,headers=headers)
    response.encoding='utf-8'
    datasoup=BeautifulSoup(response.text,'lxml')
    # try:
    #     print datasoup.select('body > div.mainBg > div.detailMain.pageWidth > div.pargraph > h1')
    # except Exception as e:
    #     print oneurl
    try:
        for one_li in datasoup.select('body > div.mainBg > div.listMain.pageWidth.clearself > div.ListRightContent.clearself > div.docuContent.listul > ul > li'):
            # print one_li.text
            url_raw= one_li.select('a')[0].get('href')
            title=one_li.select('a')[0].text
            url_end= urljoin(basic_url,url_raw)


            if 'bts.gov.cn' in url_end:
                print url_end

            print title
            print one_li.select('a')[1].text
    except Exception as e:
        print e
        print oneurl