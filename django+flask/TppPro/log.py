# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/8 15:51
@Author  : Fate
@File    : log.py 日志模块
'''

import logging
import os


# /sys/log/tpp/
def logs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    LOG_FORMAT = "%(asctime)s - %(pathname)s%(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"  # 设置输出格式
    DATE_FORMAT = "%Y/%m/%d %H:%M:%S"  # 设置时间格式
    logging.basicConfig(filename=base_dir + '/Tpp.log', filemode='a+', format=LOG_FORMAT, datefmt=DATE_FORMAT)

    return logging

if __name__ == '__main__':
    logs().warning('警告')