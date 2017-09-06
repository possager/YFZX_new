# #_*_coding:utf-8_*_
# import urllib
# import redis
# import requests
#
# connectpool = redis.ConnectionPool(host='localhost', port=6379)
# redis1 = redis.Redis(connection_pool=connectpool)
#
# thisunicode=u'你好'
#
#
# redis1.hset('people',u'你好',0)
#
#
# thisstr=thisunicode.encode('utf-8')
# print urllib.quote('你好')
#
# all_list=redis1.hgetall('people')
# print all_list
# for i in all_list.keys():
#     url1= 'http://bbs1.people.com.cn/userInfo.do?userNick='+i
#
#     response=requests.get(url=url1)
#     print response.text
#
#     print u


dict1={
    'hello':'hello'
}
print dict1.items()