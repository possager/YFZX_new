import urllib2
import time
import cookielib


import requests




class requests:
    def __init__(self):
        self.headers={}
        self.cookie={}
        self.proxies={}
        self.elapsed=-1
        self.openner=None
    def session(self):
        elapsed=-1
        headers=self.headers
        proxies=self.proxies
        cookie=self.cookie
        def request(url,headers=None,cookies=None,proxies=None,timeout=None):
            request1=urllib2.Request(url=url)
            self.openner=urllib2.build_opener()
            if headers:
                request1.headers=headers
            if proxies:
                proxies1={'http':'http://'+proxies}
                proxyhandler=urllib2.ProxyHandler(proxies1)
                self.openner.add_handler(proxyhandler)
            time1 = time.time()
            if timeout:
                response1=self.openner.open(request1,timeout=timeout)
            else:
                request1=self.openner.open(request1)
            time2=time.time()
            elapsed=time2-time1



        def close():
            self.openner.close()