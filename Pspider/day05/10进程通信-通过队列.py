# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 15:00
@author : Zephyr
@file   : 10进程通信-通过队列.py
'''
from multiprocessing import Process, Queue  # 进程队列
import queue


# q = queue.Queue(4)


def doSth(q):
    q.put(1)


def doSth2(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue(maxsize=10)

    p1 = Process(target=doSth, args=(q,))
    p1.start()

    p2 = Process(target=doSth2, args=(q,))
    p2.start()
    print(q.get())
    # 创建两条进程
