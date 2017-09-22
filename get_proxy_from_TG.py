#_*_coding:utf-8_*_
import sqlite3
from random import choice
try:
  import xml.etree.cElementTree as ET
except ImportError:
  import xml.etree.ElementTree as ET

def getSetting(file,tagname,tag): #获取设置在值
	result =""
	while True:
		try:
			tree = ET.parse(file)
			root = tree.getroot()
			results = root.find(tagname)
			result = results.find(tag).text
			break
		except Exception as e:
			print e
			pass
	return result




def getSqliteProxy(): #获取IP
	try:
		filename = getSetting('../setting.xml','sqlite_path','name')
		filepath = getSetting('../setting.xml','sqlite_path','path')
		file = filepath+filename
		connect = sqlite3.connect(file)
		curson = connect.cursor()
		sql = "select ip from ip"
		datas =curson.execute(sql)
		if datas:
			ips = []
			for data in datas:
				ip =data[0]
				ips.append(ip)
			ipchoice = choice(ips)
			proxy = {
				'http':str('http://'+ipchoice),
				'https':str('http://'+ipchoice)
			}
			return proxy
	except:
		return False