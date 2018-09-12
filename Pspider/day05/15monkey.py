# -*- coding:utf-8 -*-
'''
@time   : 2018-08-17 15:59
@author : Zephyr
@file   : 15monkey.py
'''
import gevent
import requests
import time
from gevent import monkey


gevent.monkey.patch_all()  # 将网络IO阻塞型，变成被阻塞型


def getPageText(url, order):
    time.sleep(1)

    # response = requests.get(url)
    # print(response.status_code, order)


if __name__ == '__main__':

    time.clock()  # windows

    gevent.joinall([
        gevent.spawn(getPageText, "http://www.sina.com", order=1),
        gevent.spawn(getPageText, "http://www.qq.com", order=2),
        gevent.spawn(getPageText, "http://www.baidu.com", order=3),
        gevent.spawn(getPageText, "http://www.163.com", order=4),
        gevent.spawn(getPageText, "http://www.4399.com", order=5),
        gevent.spawn(getPageText, "http://www.sohu.com", order=6),
        gevent.spawn(getPageText, "http://www.youku.com", order=7),
        gevent.spawn(getPageText, "http://www.iqiyi.com", order=8),
    ])

    print(time.clock())