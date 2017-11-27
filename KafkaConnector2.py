#!/usr/bin/python
# -*- coding: utf-8 -*-  
'''
    @File        KafkaConnector.py
    @Author      pengsen cheng
    @Company     silence
    @CreatedDate 2017-07-21
'''

import kafka, json, traceback, time, requests

class RemoteProducer(object):
    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self.__packer   = json.JSONEncoder()


    def __del__(self):
        pass

    def send(self, topic, value, key, updatetime):
         fdata = {'content': value, 'update_time': updatetime}
         url = 'https://%s:%s/tasks?id=%s&topic=%s' % (self._host, self._port, key, topic)
         try:
             parmas_message = json.dumps(fdata)
             response = requests.post(url,data=parmas_message, auth=(self._username, self._password), verify=False)
             print response.status_code
         except Exception, e:
            traceback.print_exc()

class Consumer(object):
    def __init__(self, topic, hosts, group_id):
        self.__unpacker = json.JSONDecoder()
        self.__consumer = kafka.KafkaConsumer(topic, 
                                              bootstrap_servers = hosts, 
                                              auto_offset_reset = 'earliest',
                                              value_deserializer = self.__unpacker.decode,  
                                              group_id = group_id,
                                              consumer_timeout_ms = 5000,
                                              fetch_max_bytes = 67108864)
        
    def __del__(self):
        if self.__dict__.has_key('_Consumer__consumer') and self.__consumer:
            self.__consumer.close()    
    
    def poll(self):
        try:
            for msg in self.__consumer:
                yield msg
        except:
            pass


if __name__ == '__main__':
    host = '118.112.17.8'
    port='18080'
    username='silence'
    password='silence'
    p = RemoteProducer(host,port,username, password)
    #p.send('test_aika', {"cps": "s大发大时代1111"},'1',2017)
   # p.send('test_aika', {"cps": 2222},'2',2017)
   #  ss={'data': {'spider_time': '2017-08-18 12:46:52', 'publish_time': '2017-08-16 07:03:41', 'img_urls': [],
   #            'read_count': 587, 'reply_nodes': [{'publish_time': '2017-08-16 09:00', 'img_urls': [], 'reply_nodes': [
   #          {'content': u'\\uff1a\\u724c\\u5b50\\uff0c\\u578b\\u53f7\\uff0c\\u4ef7\\u683c',
   #           'publish_time': '2017-08-16 09:00', 'url': u'https://www.cqsq.com/user/111599', 'img_urls': [],
   #           'publish_user_id': u'111599', 'parent_id': '54379894', 'publish_user': u'maim'}], 'like_count': 0,
   #                                                'publish_user': u'\\u6ce2\\u5a03\\u54e5\\u54e5', 'id': '54379894',
   #                                                'ancestor_id': u'7149488',
   #                                                'content': '\\n\\t\\t\\t\\t\\t\\xe6\\x88\\x91\\xe6\\x9c\\x89\\t\\t\\t\\t',
   #                                                'url': 'https://www.cqsq.com/read/7149488#54379894',
   #                                                'publish_user_id': u'1022917', 'reply_count': 1,
   #                                                'publish_user_photo': u'http://i.cq.cm/avatar/1022917?x-oss-process=style/avatar-middle'},
   #                                               {'publish_time': '2017-08-16 09:12', 'img_urls': [], 'reply_nodes': [],
   #                                                'like_count': 0, 'publish_user': u'maim', 'id': '54379954',
   #                                                'ancestor_id': u'7149488',
   #                                                'content': '\\n\\xe6\\xb3\\xa2\\xe5\\xa8\\x83\\xe5\\x93\\xa5\\xe5\\x93\\xa5\\xef\\xbc\\x9a\\xe6\\x88\\x91\\xe6\\x9c\\x89\\xe5\\x9b\\x9e\\xe5\\x88\\xb0\\xe5\\x8e\\x9f\\xe5\\xb8\\x96\\xe7\\x89\\x8c\\xe5\\xad\\x90\\xef\\xbc\\x8c\\xe5\\x9e\\x8b\\xe5\\x8f\\xb7\\xef\\xbc\\x8c\\xe4\\xbb\\xb7\\xe6\\xa0\\xbc\\t\\t\\t\\t',
   #                                                'url': 'https://www.cqsq.com/read/7149488#54379954',
   #                                                'publish_user_id': u'111599', 'reply_count': 0,
   #                                                'publish_user_photo': u'http://i.cq.cm/avatar/111599?x-oss-process=style/avatar-middle'}],
   #            'reply_count': 2, 'publish_user': u'maim', 'id': u'7149488',
   #            'content': u'\\u6536\\u4e2a\\u7535\\u5b50\\u79e4\\uff0c\\u54ea\\u4e2a\\u6709\\u95f2\\u7f6e\\u7684',
   #            'title': u'\\u6536\\u4e2a\\u7535\\u5b50\\u79e4\\uff0c\\u54ea\\u4e2a\\u6709\\u95f2\\u7f6e\\u7684',
   #            'url': 'https://www.cqsq.com/read/7149488', 'publish_user_id': '111599',
   #            'publish_user_photo': u'https://i.cq.cm/avatar/111599?x-oss-process=style/avatar-middle&r=20581'}}
    for i in range(5):
        p.send('test-topic', 'ss', '2', 2017)

    # p.send('test', {'cps': 3333},'3',2017)
    # hosts = '192.168.6.187:9092,192.168.6.188:9092,192.168.6.229:9092,192.168.6.230:9092'
    # c = Consumer('test-topic', hosts, '111')
    # for message in c.poll():
    #     print message.topic, message.partition, message.offset, message.key, message.value


