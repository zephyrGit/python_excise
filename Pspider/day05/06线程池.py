# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 14:16
@author : Zephyr
@file   : 06线程池.py
'''
import time

import threadpool


def doSth(args):
    time.sleep(1)
    print("****", args)


def call_back(a, b):
    # id=2281205328416 args=[1]
    print(a, b)
    print("线程执行完毕")


if __name__ == '__main__':

    pool = threadpool.ThreadPool(5)

    for i in range(20):
        requests = threadpool.makeRequests(doSth,
                                           args_list=[1, 2, 3, 4, 5, 6, 7, 8],
                                        )

    for req in requests:
        pool.putRequest(req)

    pool.wait()
