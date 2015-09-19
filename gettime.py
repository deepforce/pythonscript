# coding = utf-8
import time
import datetime


#打印当前时间
print(time.ctime())




#当前时间
now_time = datetime.datetime.now()
print(now_time)


#昨天的现在
yesterday = now_time +datetime.timedelta(days = -1)
print(yesterday)

#现在的前一秒
now_old = now_time + datetime.timedelta(seconds = -1)
print(now_old)