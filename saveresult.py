#_*_coding:utf-8_*_
import hashlib
import time
import os
import json
import zipfile
import zipfile
import os.path
import os


#/media/liang/Data/project/YFzhongxin/dataGetBySpider/one #/media/liang/3804CCCA04CC8C76/project/YFzhongxin/dataGetBySpider/one
#F:\project\YFzhongxin\dataGetBySpider\one

BASIC_FILE='F:/project/YFzhongxin/dataGetBySpider/one'
#这里边几个函数的最后一个变量向来是没什么用的

class ZFile(object):
    def __init__(self, filename, mode='r', basedir=''):
        self.filename = filename
        self.mode = mode
        if self.mode in ('w', 'a'):
            self.zfile = zipfile.ZipFile(filename, self.mode, compression=zipfile.ZIP_DEFLATED)
        else:
            self.zfile = zipfile.ZipFile(filename, self.mode)
        self.basedir = basedir
        if not self.basedir:
            self.basedir = os.path.dirname(filename)
    def addfile(self, path, arcname=None):
        path = path.replace('//', '/')
        if not arcname:
            if path.startswith(self.basedir):
                arcname = path[len(self.basedir):]
            else:
                arcname = 'default'
        self.zfile.write(path, arcname)

    def addfiles(self, paths):
        for path in paths:
            if isinstance(path, tuple):
                self.addfile(*path)
            else:
                self.addfile(path)

    def close(self):
        self.zfile.close()

    def extract_to(self, path):
        for p in self.zfile.namelist():
            self.extract(p, path)

    def extract(self, filename, path):
        if not filename.endswith('/'):
            f = os.path.join(path, filename)
            dir = os.path.dirname(f)
            if not os.path.exists(dir):
                os.makedirs(dir)
            file(f, 'wb').write(self.zfile.read(filename))



def Save_result(plantform,date_time,urlOruid,newsidOrtid,datatype,full_data,forum_pubtimestrimp=None):
    basic_file=BASIC_FILE
    date_time=str(date_time)

    print date_time
    if '-' in date_time or ' ' in date_time:#u'1498141405'这里的两个if是时间戳 #改成or
        # timeArray=time.strptime(date_time,'%Y-%m-%d %H:%M:%S')
        timeArray = examing_datetime_format(date_time)
        date_time_strip=str(int(time.mktime(timeArray)))
        # print date_time_strip
    elif len(date_time)==10 or (len(date_time) >=13 and len(date_time)<17) or '.' in date_time:
        date_time_strip=str(date_time.split('.')[0])
    else:
        print 'Wrong'
        date_time="date_time_Wrong"
        date_time_strip='date_time_Wrong'

    if datatype == 'news':#如果是新闻,格式是:平台名称（或者英文）_ 言论发布时间戳 _ 新闻URL的MD5码
        result_file = str(date_time_strip)+'_'+plantform + '_' + str(date_time_strip) + '_' + str(hashlib.md5(urlOruid).hexdigest()) + '_' + str(newsidOrtid)#7-27日发现这里的文件夹的名字可能是时间戳
        ###############################################################  7-27 日  ########################################################
        timeArray2=time.localtime(float(date_time_strip))
        dt_new=time.strftime("%Y-%m-%d %H:%M:%S",timeArray2)
        ###############################################################  7-27 日  ########################################################


        file_path=basic_file+'/'+str(plantform)+'/'+'speeches'+'/'+str(dt_new.split(' ')[0])
        file=file_path+'/'+result_file

        if os.path.exists(file_path):
            with open(file,'w+') as cmfl:
                json.dump(full_data,cmfl)
        else:
            os.makedirs(file_path)
            with open(file,'w+') as cmfl:
                json.dump(full_data,cmfl)
    elif datatype=='forum':
        result_file=plantform+'_'+str(date_time.split(' ')[0])+'_'+urlOruid+'_'+newsidOrtid
        file_path=basic_file+'/'+plantform+'/'+'org_file'+'/'+date_time.split(' ')[0]#如果是论坛,格式是:平台名称（或者英文）_ 言论发布的时间戳 _ 发布用户的ID _ 言论的tid
        file=file_path+'/'+result_file
        if os.path.exists(file_path):
            with open(file,'w+') as cmfl:
                json.dump(full_data,cmfl)
        else:
            os.makedirs(file_path)
            with open(file,'w+') as cmfl:
                json.dump(full_data,cmfl)


def examing_datetime_format(timestr):
    try:
        timestrlist=time.strptime(timestr, "%Y-%m-%d")
        return timestrlist
    except:
        try:
            timestrlist=time.strptime(timestr,'%Y-%m-%d %H:%M')
            return timestrlist
        except:
            try:
                timestrlist=time.strptime(timestr,'%Y-%m-%d %H:%M:%S')
                return timestrlist
            except:
                return '1111-11-11 11:11:11'



if __name__ == '__main__':
    jsondict={
        'one':1,
        'two':2
    }
    file1=BASIC_FILE+'/zip'
    try:
        os.makedirs(file1)
    except Exception as e:
        print e
    if os.path.isdir(BASIC_FILE+'/zip/test.zip'):
        Zf=ZFile(filename=BASIC_FILE+'/zip/test.zip',mode='w')
    else:
        with open(BASIC_FILE+'/zip/test.zip','w+') as fl:
            fl.close()
        Zf=ZFile(filename=BASIC_FILE+'/zip/test.zip',mode='w')

    # Zf.addfile()

    for zipfile in os.listdir('/media/liang/3804CCCA04CC8C76/project/YFzhongxin/dataGetBySpider/one/sohu/org_file/2017-07-03'):
        Zf.addfile('/media/liang/3804CCCA04CC8C76/project/YFzhongxin/dataGetBySpider/one/sohu/org_file/2017-07-03/'+zipfile,arcname=zipfile)
        os.remove('/media/liang/3804CCCA04CC8C76/project/YFzhongxin/dataGetBySpider/one/sohu/org_file/2017-07-03/'+zipfile)
    Zf.close()

    # datajson=json.dumps(jsondict)
    # Save_result(plantform='weibo',date_time='2016-05-05 20:28:54',urlOruid='123456',newsidOrtid='12345',datatype='forum',full_data=datajson)
    # print time.strftime('2017-12-12 12:12:12','%Y-%m-%d %H:%M:%S')