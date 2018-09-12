# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 15:51
@author : Zephyr
@file   : 14gevent.py
'''
import gevent
import time

'''
净手欲摸杯，
大钊身后催.
独秀且安坐，
待我买橘归.
'''


def a():
    print('净手欲摸杯，')
    gevent.sleep(1)
    print('独秀且安坐，')


def b():
    print('大钊身后催.')
    gevent.sleep(2)
    print('待我买橘归.')


if __name__ == '__main__':
    g1 = gevent.spawn(a)
    g2 = gevent.spawn(b)

    # 启动
    gevent.joinall([g1, g2])
