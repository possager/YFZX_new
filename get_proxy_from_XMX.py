#_*_coding:utf-8_*_


#因为reids在idc上挂了，所以写了这么一个新的代理
import requests
import json
import time
from saveresult import BASIC_FILE




class Proxy:
    def __init__(self,url_proxy='http://192.168.8.52:8899/'):
        self.url_proxy=url_proxy

    def save_proxy(self):
        response=requests.get(self.url_proxy)
        jsondata=json.loads(response.text)
        file1=BASIC_FILE+'/proxy.txt'
        with open(file1,'w') as fl:
            json.dump(jsondata,fl,encoding='utf-8')
        # json.dump(jsondata,file1)

    def get_proxy_couple(self,num):
        file1 = BASIC_FILE + '/proxy.txt'
        with open(file1,'r') as fl:
            datajson=json.load(fl,encoding='utf-8')
        if datajson:
            # return (str(datajson[num]['ip']),str(datajson[num]['port']))
            return str(datajson[num]['ip'])+':'+str(datajson[num]['port'])


url_proxy='http://192.168.8.52:8899/'


def save_proxy():
    while True:
        response = requests.get(url_proxy)
        jsondata = json.loads(response.text)
        file1 = BASIC_FILE + '/proxy.txt'
        with open(file1, 'w') as fl:
            json.dump(jsondata, fl, encoding='utf-8')
        time.sleep(30)

def get_proxy_couple(num):
    file1 = BASIC_FILE + '/proxy.txt'
    with open(file1,'r') as fl:
        datajson=json.load(fl,encoding='utf-8')
    if datajson:
        # return (str(datajson[num]['ip']),str(datajson[num]['port']))
        return str(datajson[num]['ip'])+':'+str(datajson[num]['port'])


if __name__ == '__main__':
    # thisclass=Proxy()
    # # thisclass.save_proxy()
    # print thisclass.get_proxy_couple(2)
    # print get_proxy_couple(2)
    save_proxy()