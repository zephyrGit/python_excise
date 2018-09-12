# -*- coding:utf-8 -*-
'''
@time   : 2018-08-22 20:47
@author : Zephyr
@file   : start.py
'''

import scrapy.cmdline


def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'mydouban'])


if __name__ == '__main__':
    main()
