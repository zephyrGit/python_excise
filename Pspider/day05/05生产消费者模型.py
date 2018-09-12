# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 10:59
@author : Zephyr
@file   : 05生产消费者模型.py
'''

import threading
import random
import queue

'''
开两条线程
一条爬
一条存

实现线程通信
'''

# 线程通信（锁）
con = threading.Condition()

# 产品容器
pList = []
qu = queue.Queue(1000)


class Production():
    '''
    产品
    '''

    def __init__(self, num):
        self.num = num

    def __str__(self):
        return '产品数量%d' % self.num


class Producer(threading.Thread):
    '''
    生产者
    '''

    def run(self):
        while True:
            with con:

                # 生产
                p = Production(random.randint(100, 1000))

                print('生产了', p)
                qu.put(p)

                if qu.full():
                    # 通知 消费者
                    con.notify()
                    con.wait()


class Consumer(threading.Thread):
    '''
    消费者
    '''

    def run(self):
        while True:
            with con:
                if not qu.empty():
                    # p = pList.pop()
                    p = qu.get()
                    print('消费了', p)

                # 通知 wait（）
                con.notify()
                con.wait()


if __name__ == '__main__':
    # 开辟产品线
    p = Producer()
    p.start()

    # 开辟消费线
    c = Consumer()
    c.start()
