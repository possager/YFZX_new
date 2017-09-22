#_*_coding:utf-8_*_
import requests

import random
import cookielib
import time
from saveresult import BASIC_FILE
import sys
from get_proxy_from_XMX import get_proxy_couple
from get_proxy_from_TG import getSqliteProxy
from requests.exceptions import ProxyError,ConnectTimeout,ReadTimeout,ConnectionError



timeout_value=10
proxy_time_threshold=5


def get_response_and_text(url,headers=None,needupdate=False,update_info=None,charset=None):
    if headers:
        this_headers=headers
    else:
        this_headers={
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
                'Connection':'close'
            }
    num_reply=5
    while True:  # 强制请求
        try:
            # timea = time.time()
            # cookies1 = cookielib.MozillaCookieJar()
            # proxies_from_db=get_proxy_couple(random.randint(0,50))
            # proxies1 = {'http': 'http://' + proxies_from_db,
            #             'https':'https://'+proxies_from_db}#反正实在try里边，过限了自然会回去。

            proxies1=getSqliteProxy()
            # print proxies1


            if headers:
                response_in_function=requests.get(url=url,headers=headers,proxies=proxies1,timeout=timeout_value)
            else:
                response_in_function=requests.get(url=url,headers=this_headers,proxies=proxies1,timeout=timeout_value)
            if charset:
                response_in_function.encoding=charset
            response_in_function_text = response_in_function.text
            if response_in_function.status_code ==204:
                num_reply-=1
                if num_reply<0:
                    sys.exit()
                else:
                    raise Exception

            if needupdate:
                file1 = BASIC_FILE + '/chengdu/chengdu_sechdule.text'
                sechdule = 1700000
                sechdule=update_info['page_num']
                with open(file1,'w') as fl:
                    fl.write(sechdule)


            break
        except Exception as e:
            # print e
            # if hasattr(e,'status_code'):
            if isinstance(e,ProxyError):
                continue
            if isinstance(e,ConnectTimeout):
                continue
            if isinstance(e,ReadTimeout):
                continue
            try:
                if e.status_code in [404,400]:


                    sys.exit()
                elif e.status_code==[204,403]:#可能是有数据的，但是被屏蔽了
                    num_reply-=1

                    if num_reply<1:
                        sys.exit()
            except Exception as e:
                print e


    proxy_here = proxies1.values()[0].split('//')[1]
    if response_in_function.status_code==204:
        return {'response_in_function':None,'response_in_function_text':{}}
    return {'response_in_function':response_in_function,'response_in_function_text':response_in_function_text}