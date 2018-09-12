# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 10:22
@author : Zephyr
@file   : 04future模块.py
'''
import threadpool
from house import *
import time

from concurrent.futures import ThreadPoolExecutor

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

# with ThreadPoolExecutor(20) as exc:
#     for url in urlList:
#         exc.submit(getHouseInfo, url)  # 无序

with ThreadPoolExecutor(20) as mapexc:
    mapexc.map(getHouseInfo, urlList)

print(time.clock())
