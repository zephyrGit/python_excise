# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 15:09
@author : Zephyr
@file   : 11进程通信-管道.py
'''
from multiprocessing import Process, Pipe  # 进程队列


def doSth(son):
    son.send('ok')
    # 当管道里有数据时，返回True
    print(son.poll())
    # 一次接收一条 ， 没有就堵塞了
    # print('from father:', son.recv())
    # print('from father:', son.recv())
    # print('from father:', son.recv())
    while son.poll:
        print('from father:', son.recv())


if __name__ == '__main__':
    # 创建管道
    son, father = Pipe()

    p = Process(target=doSth, args=(son,))
    p.start()

    # send（）发送
    father.send('儿子，***')
    # recv()接收
    print(father.recv())

    father.send('快点')

    # 关闭
    father.close()
    son.close()
