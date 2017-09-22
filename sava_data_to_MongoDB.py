import pymongo
import json
import datetime
import time
from KafkaConnector import RemoteProducer,Consumer
import threading
# from multiprocessing import Pool



Client=pymongo.MongoClient('localhost',27017)
Col=Client['1101_all_data']
Doc=Col['data_all']


List_outside=[]

host = '182.150.63.40'
port = '12308'
username = 'silence'
password = 'silence'
producer = RemoteProducer(host=host, port=port, username=username, password=password)


class data_to_mongo:
    def __init__(self):
        self.clent=pymongo.MongoClient('localhost',27017)
        self.Col=self.clent['1101_all_data']
        self.Doc=self.Col['data_all']



# Doc.create_index('item_id')


def save_data_to_mongodb(data,item_id,platform_e,platform_c):
    data_insert={
        'item_id':item_id,
        'data':data,
        'been_pushed':0,
        'platform_e':platform_e,
        'platform_c':platform_c
    }
    while True:
        try:
            Doc.insert(data_insert)
            break
        except Exception as e:
            print e




def send_data_from_list_kafka(i):

    while True:
        try:
            content = i['data']
            item_id = i['item_id']
            print item_id
            producer.send(topic='1101_STREAM_SPIDER', value=content, key=item_id, updatetime=content['data']['spider_time'])
            Doc.delete_one({'item_id': item_id})
            break
        except Exception as e:
            print e


def send_data_from_mongo_to_list():
    while True:
        try:
            for i in Doc.find({'been_pushed':0}).limit(30):
                if len(List_outside)<50:
                    print len(List_outside)
                    Doc.update({'item_id': i['item_id']}, {'$set': {'been_pushed': 1}})
                    List_outside.append(i)
                else:
                    time.sleep(1)

        except:
            pass





if __name__ == '__main__':
    # send_data_from_mongo_kafka()
    threading1=threading.Thread(target=send_data_from_mongo_to_list,args=())
    # threading1.setDaemon(True)
    threading1.start()
    # threading1.join()





    threadlist = []
    while True:
        while List_outside or threadlist:
            for threadi in threadlist:
                if not threadi.is_alive():
                    threadlist.remove(threadi)
            while len(threadlist) < 30 and List_outside:
                print len(List_outside)
                data_in_while = List_outside.pop()
                thread_in_while = threading.Thread(target=send_data_from_list_kafka, args=(data_in_while,))
                thread_in_while.setDaemon(True)
                thread_in_while.start()
                threadlist.append(thread_in_while)


    # print 'hello'
