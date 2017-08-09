import requests
from bs4 import BeautifulSoup
import time
import json
from proxy_to_redis import redis1
from proxy_to_redis import *
from multiprocessing import process
from multiprocessing.pool import Pool
from multiprocessing import pool
import UserAgent
import urllib
import urllib3
import urllib2


# proxy1 = get_proxy_from_redis()
# headers = {
#     'User-Agent': UserAgent.getUserAgentRandom(),
# }
# request1=urllib2.Request(url="http://www.toutiao.com/a6421034271468683777/",headers=headers)
# proxyhandler=urllib2.ProxyHandler({'http':'http://'+proxy1})
# openner=urllib2.build_opener(proxyhandler)
# data=openner.open(request1,timeout=5)
# print data.read()
# openner.close()

def run1(j):
    url=redis1.lindex('urltest',j)
    while True:
        try:
            time1=time.time()
            proxy1 = get_proxy_from_redis()
            headers = {
                'User-Agent': UserAgent.getUserAgentRandom(),
            }
            request1=urllib2.Request(url=url,headers=headers)
            proxyhandler=urllib2.ProxyHandler({'http':'http://'+proxy1})
            openner=urllib2.build_opener(proxyhandler)
            data=openner.open(request1,timeout=5)

            print '-----------------------------',j
            openner.close()
            time2=time.time()
            break
        except Exception as e:
            print e
            # print '----------------has wrong   the headers is          ',sessionq.headers
            time.sleep(1)
            # redis1.lpush('proxy_good',proxy1)
    print time2-time1
    time3=time.time()
    print 'data'
    data2=data
    print data.read()

    time4=time.time()
    print time4-time3
    print 'data2-------------data2'
    print data.read()
    time5=time.time()
    print time5-time4
    print 'data3---------------data-'
    print data2.read()
    time6=time.time()
    print time6-time5






    redis1.rpush('urltest',url)


if __name__ == '__main__':
#     # list1=[i for i in range(3000)]
#     # process1=pool.Pool(processes=70)
#     # process1.map(run1,list1)
#     # process1.close()
#     # process1.join()
#
#
#
#     for i in range(100):
#         print i
#         run1(i)
    run1(1)