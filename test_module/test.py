import requests



proxy={
    'http':'http://192.168.6.105:8080',
    'https':'http://192.168.6.105:8080'
}

response1=requests.get(url='http://www.baidu.com',proxies=proxy)
print response1.text