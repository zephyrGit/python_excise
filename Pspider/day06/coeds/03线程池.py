# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 09:52
@author : Zephyr
@file   : 03线程池.py
'''
import threadpool
import threading
from house import *
import time

# 线程池
pool = threadpool.ThreadPool(10)

time.clock()

# 开启线程
url = 'https://gz.lianjia.com/ershoufang/pg1'
totalPage = getPage(url)

print(totalPage)

# url 列表
urlList = []
for i in range(1, totalPage + 1):
    url = 'https://gz.lianjia.com/ershoufang/pg%d' % (i)
    urlList.append(i)

# 用线程池管理
requests = threadpool.makeRequests(getHouseInfo, args_list=urlList)

# 启动
for req in requests:
    pool.putRequest(req)

#
pool.wait()

print(time.clock())
