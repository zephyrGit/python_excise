# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 10:34
@author : Zephyr
@file   : 03线程锁.py
'''

import threading

# 互斥锁  一一匹对的(操作同一数据)
lock = threading.Lock()

# 递归锁  可以在任何地方加
rLock = threading.RLock()

money = 0
age = 0
ageLock = threading.Lock()


def addMoney():
    global money
    global age

    # 加锁
    # if lock.acquire():
    #     for _ in range(1000000):
    #         money += 1
    #
    #     # 释放锁
    #     lock.release()
    # print(money)

    #
    # with rLock:
    #     for _ in range(1000000):
    #         money += 1
    # print(money)

    with lock:
        with rLock:
            for _ in range(1000000):
                money += 1
                age += 1
    print(money, age)


if __name__ == '__main__':
    addMoney()
    threadList = []
    for i in range(10):
        t = threading.Thread(target=addMoney)
        threadList.append(t)
        t.start()
        # 同步
        # t.join()

    # 保证线程正常结束
    for t in threadList:
        t.join()
