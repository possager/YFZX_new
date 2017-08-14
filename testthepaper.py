import requests
import re
from bs4 import BeautifulSoup

user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36'
user_agent2='Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'

headers={
    'User-Agent':user_agent2
}
# response1=requests.get(url='http://m.thepaper.cn/channel_25950',headers=headers)
# # print response1.text
# Re_pattern=re.compile(r'data.*?\:.*?\".*?Math\.random\b')
# datare=Re_pattern.findall(response1.text)
#
# url_in_content =datare[0].split('"')[1]
# nexturl='http://m.thepaper.cn/load_channel.jsp?'+url_in_content+str(1)
# print nexturl

url1='http://www.thepaper.cn/load_index.jsp?nodeids=nodeids=25448,26609,25942,26015,25599,25842,26862,25769,25990,26173,26202,26404,26490,&topCids=1762084,1759534&pageidx=0'
url2='http://www.thepaper.cn/load_index.jsp?nodeids=nodeids=25444,27224,26525,26878,25483,25457,25574,25455,26937,25450,25482,25445,25456,25446,25536,26506,&topCids=1763063&pageidx=0'
url3='http://www.thepaper.cn/load_index.jsp?nodeids=nodeids=25434,25436,25433,25438,25435,25437,27234,25485,25432,&topCids=1762842,1762790,1763110&pageidx=0'
url4='http://www.thepaper.cn/load_index.jsp?nodeids=nodeids=26912,26918,26919,26965,26906,26907,26908,27260,26909,26910,26911,26913,26914,26915,&topCids=1763003,1763173,1762843&pageidx=0'
url5='http://www.thepaper.cn/load_index.jsp?nodeids=nodeids=25462,25488,25489,25490,25423,25426,25424,25463,25491,25428,25464,25425,25429,25481,25430,25678,25427,25422,25487,25634,25635,25600,&topCids=1763004,1763242,1763002&pageidx=0'


response1=requests.get(url=url4,headers=headers)
# print response1.text
datasoup=BeautifulSoup(response1.text,'lxml')
print str(datasoup)
print '------------------------------------------------------------------------------------------------------'
for urlmark1 in  datasoup.select('body > div'):
    # print urlmark1.get('href')#href
    print urlmark1.select('h2 > a')[0].get('href')#url
    print urlmark1.select('p')[0].text#abstract
    print urlmark1.select('a')[2].text
    print urlmark1.select('a')[1].text