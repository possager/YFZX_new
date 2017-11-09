#_*_coding:utf-8_*_
import requests
import random
from get_proxy_from_XMX import get_proxy_couple
import traceback

def visit_page_in_class_post(url, data=None, charset='utf-8', headers=None):
    error_num=0
    while True:
        error_num+=1
        try:
            while True:
                # proxy = getSqliteProxy()

                # proxy_from_xmx = get_proxy_couple(random.randint(0, 50))
                proxy_from_xmx='192.168.6.105:8080'
                proxy = {'http': 'http://' + proxy_from_xmx, 'https': 'http://' + proxy_from_xmx}

                if proxy:
                    break
            while True:
                response1 = requests.post(url=url, headers=headers, proxies=proxy, data=data)
                response1.encoding = charset
                response = response1.text
                response1.close()
                try:
                    response_code = response1.status_code
                except Exception as e:
                    traceback.print_exc()
                    return None
                if response_code < 300:
                    return response1
                elif response_code >300:
                    return response1
                else:
                    return response1
        except:
            pass
        if error_num>5:
            break