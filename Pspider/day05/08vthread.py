# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 14:37
@author : Zephyr
@file   : 08vthread.py
'''
import vthread
import time


@vthread.pool(3)
def doSth(url):
    time.sleep(1)
    print('123')
    pr


if __name__ == '__main__':
    for i in range(10):
        doSth('http://www.baidu.com/')
