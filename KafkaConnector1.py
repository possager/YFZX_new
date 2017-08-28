#!/usr/bin/python
# -*- coding: utf-8 -*-  
'''
    @File        KafkaConnector.py
    @Author      pengsen cheng
    @Company     silence
    @CreatedDate 2017-07-21
'''

import kafka, json, traceback

class Producer(object):
    def __init__(self, hosts):
        self.__packer   = json.JSONEncoder()
        self.__producer = kafka.KafkaProducer(bootstrap_servers = hosts, 
                                              value_serializer = self.__packer.encode, 
                                              max_request_size = 67108864)
    
    def __del__(self):
        if self.__dict__.has_key('_Producer__producer') and self.__producer:
            self.__producer.close()    
    
    def  send(self, topic, value, key, updatetime):
        fdata = {'content': value, 'update_time': updatetime}
        try:
            self.__producer.send(topic, value = fdata, key = key)
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
    # host = ['192.168.6.187:9092', '192.168.6.188:9092', '192.168.6.229:9092', '192.168.6.230:9092']
    host = '192.168.6.187:9092,192.168.6.188:9092,192.168.6.229:9092,192.168.6.230:9092'
    p = Producer(host)
    i=0
    while(i<1000):
         p.send('topic',{ 'cps': 44443}, "key1","updatetime")
         i=i+1
   # p.send('origin', {'cps': 3333})

    c = Consumer('topic', host, '111')#第一个参数是topic的名字，最后一个是你的用户名，你可以随便取，但最好取特别一点
    for message in c.poll():
        print message.topic, message.partition, message.offset, message.key, message.value