# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 15:31
@author : Zephyr
@file   : 12进程通信-manager.py
'''
from multiprocessing import Process, Manager


def doSth(l, d):
    l.append(1)
    d['name'] = 'zephyr'



if __name__ == '__main__':
    with Manager() as manager:
        # 创建一个列表
        l = manager.list()
        d = manager.dict()

        p = Process(target=doSth, args=(l, d))
        p.start()
        p.join()

        print(l)
        print(d)