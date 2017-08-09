import urllib2
import cookielib
import time
from proxy_to_redis import get_proxy_from_redis
from proxy_to_redis import proxy_sendback


def get_response_and_text(url,headers=None):
    if headers:
        this_headers=headers
    else:
        this_headers={
                'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
            }
    while True:  # 强制请求
        try:
            timea = time.time()
            cookies1 = cookielib.MozillaCookieJar()
            proxies1 = {'http': 'http://' + get_proxy_from_redis()}
            proxyhandler = urllib2.ProxyHandler(proxies1)
            cookiehandler = urllib2.HTTPCookieProcessor(cookies1)
            request1 = urllib2.Request(url=url, headers=this_headers)
            opener1 = urllib2.build_opener(proxyhandler, cookiehandler)
            response_in_function = opener1.open(request1)
            response_in_function_text = response_in_function.read()
            break
        except Exception as e:
            print e
    timeb = time.time()
    proxy_here = proxies1.values()[0].split('//')[1]
    opener1.close()
    if timeb - timea < 3:
        proxy_sendback(proxy_here)
    return {'response_in_function':response_in_function,'response_in_function_text':response_in_function_text}