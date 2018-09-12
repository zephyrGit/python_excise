# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 09:24
@author : Zephyr
@file   : 01多线程单核.py
'''
# 多线程
'''
from threading import Thread


def loop():
    while True:
        print("亲爱的，我错了，我能吃饭了吗?")


if __name__ == '__main__':

    for i in range(3):
        t = Thread(target=loop)
        t.start()

    while True:
        pass
'''
# 多进程
'''
from multiprocessing import Process


def loop():
    while True:
        print("亲爱的，我错了，我能吃饭了吗?")


if __name__ == '__main__':

    for i in range(3):
        t = Process(target=loop)
        t.start()

    while True:
        pass
'''
