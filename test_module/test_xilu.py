#_*_coding:utf-8_*_
import requests

headers1 = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'X-Requested-With': 'XMLHttpRequest',  # 重要
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'close',
    'Host': 'm.xilu.com',
    'Upgrade-Insecure-Requests': '1'

}
while True:
    try:
        response1=requests.get(url='http://m.xilu.com/index.html',headers=headers1,data={'page':'5'})
        print response1.text
        break
    except Exception as e:
        print e