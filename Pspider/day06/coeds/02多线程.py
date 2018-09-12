# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 09:34
@author : Zephyr
@file   : 02多线程.py
'''
import threading
from house import *
import time


time.clock()

# 开启线程
url = 'https://gz.lianjia.com/ershoufang/pg1'
totalPage = getPage(url)

print(totalPage)

tList = []
for i in range(1, totalPage + 1):
    url = 'https://gz.lianjia.com/ershoufang/pg%d' % (i)
    t = threading.Thread(target=getHouseInfo, args=(url,))
    tList.append(t)
    t.start()

# 保证线程结束
for t in tList:
    t.join()

print(time.clock())