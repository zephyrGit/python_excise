# -*- coding:utf-8 -*-
'''
@time   : 2018-08-21 14:20
@author : Zephyr
@file   : start.py
'''

import scrapy.cmdline


def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'mysina'])


if __name__ == '__main__':
    main()
