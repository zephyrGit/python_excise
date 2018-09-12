# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 14:52
@author : Zephyr
@file   : 09进程.py
'''
import multiprocessing
import threading


def doSth():
    print('***********')


threading.Thread(target=doSth).start()
if __name__ == '__main__':
    # fork()机制
    # 创建进程
    p = multiprocessing.Process(target=doSth, args=())
    # 启动
    p.start()
    # 等待
    p.join()
