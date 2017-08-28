#!/usr/bin/python
# -*- coding: utf-8 -*-  
'''
    @File        KafkaConnector.py
    @Author      pengsen cheng
    @Company     silence
    @CreatedDate 2017-07-21
'''




#那个是1101_STREAM_SPIDER
#我的1101平台的topic


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
    
    def send(self, topic, value, key,updatetime ):
        try:
            fdata = {'content': value, 'update_time': updatetime}
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
    hosts = ['192.168.6.187:9092', '192.168.6.188:9092', '192.168.6.229:9092']
    
    p = Producer(hosts)

    p.send('test_aika', {'cps': 1111},'1',2017)
    p.send('test_aika', {'cps': 2222},'2',2017)
    p.send('test_aika', {'cps': 3333},'3',2017)
#     
#     c = Consumer('origin', hosts, '111')
    # for message in c.poll():
    #     print message.topic, message.partition, message.offset, message.key, message.value

