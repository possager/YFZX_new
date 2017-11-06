from visit_page4 import get_response_and_text
import re
from bs4 import BeautifulSoup


def get_content(data,result_queue):#
    Re_find_img=re.compile(r'img .*? src="(.*?)"')
    Re_find_movie=re.compile(r'\<video.*?src="(.*?)"')

    url=data['url']
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'connection': 'close',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    }
    response1=get_response_and_text(url=url,headers=headers)
    response_in_function=response1['response_in_function']
    if not response_in_function:
        return
    response_in_function_text=response1['response_in_function_text']
    try:
        datasoup=BeautifulSoup(response_in_function_text,'lxml')
    except:
        return
    content_str=str(datasoup.select('div.content_main')[0])
    img_urls=Re_find_img.findall(content_str)
    video_url=Re_find_movie.findall(content_str)
    img_urls2=[]
    video_url2=[]
    for one_img_url in img_urls:
        img_urls2.append('http://www.xjbtssbtszhdj.com/'+one_img_url)
    for one_video_url in video_url:
        video_url2.append('http://www.xjbtssbtszhdj.com'+one_video_url)
    print img_urls2
    print video_url2
    data['img_urls']=img_urls2
    data['video_urls']=video_url2
    result_queue.put(data)


if __name__ == '__main__':
    get_content({'url':'http://www.xjbtssbtszhdj.com/toxnori.frontDetail.in?id=402880825f0a31b6015f104ca68a23ac'})