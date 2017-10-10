#_*_coding:utf-8_*_
import pymongo
import time


client=pymongo.MongoClient('localhost',27017)
COL=client['1101_all_data']
DB=COL['data_all']

try:
    print '正在查询数据中的数据数量'
    timea=time.time()
    print DB.find({'platform_e':'jifengluntan'}).count()
    # for onecontent in DB.find({'platform_e':'ChengDuQuanSouSuo'}):
    #     print onecontent['data']['data']['content']
    #     print '\n'
    #       DB.delete_one({'_id':onecontent['_id']})
    timeb=time.time()
    print timeb-timea
except Exception as e:
    print e