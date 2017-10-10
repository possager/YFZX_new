import pymongo
import json
import datetime
import time
from KafkaConnector import RemoteProducer,Consumer
import threading
import datetime
# from multiprocessing import Pool






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







def save_data_to_mongodb(data,item_id,platform_e,platform_c,cache_data_list):
    # Client = pymongo.MongoClient('localhost', 27017)
    # Col = Client['1101_all_data']
    # Doc = Col['data_all']


    data_insert={
        'item_id':item_id,
        'data':data,
        'been_pushed':0,
        'platform_e':platform_e,
        'platform_c':platform_c
    }
    cache_data_list.put(data_insert)
    print cache_data_list.qsize()
    # while True:
    #     try:
    #         Doc.insert(data_insert)
    #         Client.close()
    #         break
    #     except Exception as e:
    #         print e
    if cache_data_list.qsize()>50:
        save_data_to_mongodb_new(cache_data_list)




def save_data_to_mongodb_without_full(cache_data_list):
    if cache_data_list.qsize()>0:
        save_data_to_mongodb_new(cache_data_list)




def send_data_from_list_kafka(i):
    Client = pymongo.MongoClient('localhost', 27017)
    Col = Client['1101_all_data']
    Doc = Col['data_all']


    while True:
        try:
            content = i['data']
            item_id = i['item_id']
            print item_id
            producer.send(topic='1101_STREAM_SPIDER', value=content, key=item_id, updatetime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            Doc.delete_one({'item_id': item_id})
            Client.close()
            break
        except Exception as e:
            print e


def send_data_from_mongo_to_list():
    Client = pymongo.MongoClient('localhost', 27017)
    Col = Client['1101_all_data']
    Doc = Col['data_all']


    while True:
        try:
            for i in Doc.find({'been_pushed':0}).limit(30):
                if len(List_outside)<50:
                    print len(List_outside)
                    Doc.update({'item_id': i['item_id']}, {'$set': {'been_pushed': 1}})
                    List_outside.append(i)
                else:
                    time.sleep(1)

            # Client.close()

        except:
            pass


def save_data_to_mongodb_new(dataqueue):
    Client = pymongo.MongoClient('localhost', 27017)
    Col = Client['1101_all_data']
    Doc = Col['data_all']

    while not dataqueue.empty():
        error_num=0
        while True:
            try:
                thisdata = dataqueue.get()

                data = thisdata['data']
                item_id = thisdata['item_id']
                platform_c = thisdata['platform_c']
                platform_e = thisdata['platform_e']

                data_insert = {
                    'item_id': item_id,
                    'data': data,
                    'been_pushed': 0,
                    'platform_e': platform_e,
                    'platform_c': platform_c
                }
                Doc.insert(data_insert)
                break
            except Exception as e:
                print e
                if error_num<5:
                    error_num+=1
                else:
                    break

    Client.close()
        # print filename



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
