# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 15:42
@author : Zephyr
@file   : 13greenlet.py
'''
from greenlet import greenlet

'''
十八新娘八十郎，
苍苍白发对红妆。
鸳鸯被里成双夜，
一树梨花压海棠
'''


def make():
    print('十八新娘八十郎，')
    g2.switch()
    print('鸳鸯被里成双夜，')
    g2.switch()


def love():
    print('苍苍白发对红妆。')
    g1.switch()
    print('一树梨花压海棠')


if __name__ == '__main__':
    g1 = greenlet(make)
    g2 = greenlet(love)
    # 让出执行权限, 程序员切换的
    g1.switch()
