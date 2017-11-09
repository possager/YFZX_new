#_*_coding:utf-8_*_
from visit_page4 import get_response_and_text
from bs4 import BeautifulSoup
import json
import re


from visit_page_post import visit_page_in_class_post


def get_index(content_queue):
    def replace_str(match):
        str_target = match.group(1)
        str_original = match.group(0)
        data = str_original.replace(str_target, 'frontDetail')
        return data

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }




    index_list2=[
        'http://www.xjbtssbtszhdj.com/courier.frontAllList.in?pageNum=',#党情速递
        'http://www.xjbtssbtszhdj.com/toxnori.frontAllList.in?pageNum=',#远教天地
        'http://www.xjbtssbtszhdj.com/study.frontAllList.in?pageNum=',#在线学习
        'http://www.xjbtssbtszhdj.com/activity.frontAllList.in?pageNum=',#组织结构
        'http://www.xjbtssbtszhdj.com/announce.frontList.in?pageNum=',#公告通知
        # '',
        # 'experience.frontAllPage.in'
    ]

    for index_url1 in index_list2:
        status_code=1
        pageNum=1
        while status_code<400:
            index_url1=index_url1+str(pageNum)
            post_data={
                'pageSize':'15'
            }
            response1=visit_page_in_class_post(url=index_url1,data=post_data)
            status_code=response1.status_code
            pageNum+=1
            try:
                datajson=json.loads(response1.text)
            except:
                break
            for i in datajson['rows']:
                content=i['content2']
                try:
                    read_count=i['clickRate']
                except:
                    read_count=0
                publish_time=i['createTime']
                id=i['id']
                title=i['title']
                publish_user=i['staff']['staffName']
                url_raw=index_url1.split('pageNum=')[0] + 'id=' + id
                url=re.sub(r'http\:\/\/www\.xjbtssbtszhdj\.com\/\w*?\.(.*?)\.in\?',replace_str,url_raw)
                one_article={
                    'content':content,
                    'read_count':read_count,
                    'publish_time':publish_time,
                    'id':id,
                    'title':title,
                    'publish_user':publish_user,
                    'url':url
                }
                # print one_article
                content_queue.put(one_article)





# if __name__ == '__main__':
#     get_index(url='http://www.baidu.com',content_queue=None)