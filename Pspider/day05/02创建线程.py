# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 09:37
@author : Zephyr
@file   : 02创建线程.py
'''
import _thread
import threading
import time


def doSth(a):
    time.sleep(1)
    print(threading.current_thread().name)

    print(threading.current_thread().daemon)
    print('*********', a)


def doSthB(a):
    time.sleep(2)
    # 线程名
    print(threading.current_thread().name)
    # 线程号
    print(threading.current_thread().ident)
    # 守护线程
    print(threading.current_thread().daemon)
    print('*********', a)


def _thread_create():
    '''
    通过_thread_create 创建线程
    :return:
    '''

    # _thread() 守护线程
    # 主线程死去 子线程也必须死
    print(threading.current_thread().name)
    _thread.start_new_thread(doSth, (1,))
    # 阻塞 主线程
    # while True:
    #     pass

    time.sleep(1)


def threadingTread():
    '''
    通过threadingThread（）创建
    :return:
    '''

    '''
    target=None,  方法
    name=None, 线程名  Thread-N
    args=() 实参 元组
    '''
    # t1 = threading.Thread(target=doSth, args=(123,))
    # # 启动
    # t1.start()
    # t2 = threading.Thread(target=doSth, args=(123,))
    # # 启动
    # # 设置为守护线程
    # t2.setDaemon(True)
    # t2.start()
    time.clock()
    for i in range(10):
        t = threading.Thread(target=doSth, args=(i,))
        t.start()
        # 等待 , 必须当前线程执行完
        # t.join()
    print(time.clock())


class myThread(threading.Thread):
    '''
    通过继承实现
    '''

    def __init__(self, name, age):
        super(myThread, self).__init__()
        self.name = name
        self.age = age

    def run(self):
        # 实现线程任务
        print('============')
        print(self.name, self.age)


def importantApi():
    t1 = threading.Thread(target=doSth, args=(1,))
    t2 = threading.Thread(target=doSthB, args=(2,))
    t3 = threading.Thread(target=doSth, args=(3,))

    t1.start()
    t2.start()
    t3.start()

    # 线程数量
    print(threading.enumerate())
    # 当前活动线程数
    print(threading.active_count())
    print(t1.isAlive(), '***')


if __name__ == '__main__':
    # 第二种
    # threadingTread()

    # 第三种 继承
    # t = myThread('zephyr', 18)
    # t.start()
    importantApi()
