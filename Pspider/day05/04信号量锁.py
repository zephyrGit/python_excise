# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 10:52
@author : Zephyr
@file   : 04信号量锁.py
'''
import threading

# value 并发量
import time

sem = threading.Semaphore(4)


def doSth(a):
    # 足 4 而行 （凑足4条）
    with sem:
        time.sleep(1)
        print('我是的%d条线程' % a)


if __name__ == '__main__':
    for i in range(20):
        t = threading.Thread(target=doSth, args=(i,))
        t.start()
