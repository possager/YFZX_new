import datetime
import time



time1='2017-6-9 8:40:30'
time2= time.strptime(time1,'%Y-%m-%d %H:%M:%S')

print time.strftime('%Y-%m-%d %H:%M:%S',time2)