# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 10:33
@author : Zephyr
@file   : 06多进程.py
'''

from multiprocessing import Pool
import time
from house import *

if __name__ == '__main__':
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

    # 用进程池管理
    pool = Pool(4)
    # 启动
    pool.map(getHouseInfo, urlList)

    # 不让新的东西加入
    pool.close()
    # 结束
    pool.join()

    print(time.clock())

# 进程池不能同协程一起用，会冲突
# 内存溢出  一般不存 list dict
