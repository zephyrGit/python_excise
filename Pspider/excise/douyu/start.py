# -*- coding:utf-8 -*-
'''
@time   : 2018-08-24 09:21
@author : Zephyr
@file   : start.py
'''

import scrapy.cmdline


def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'mydouyu'])


if __name__ == '__main__':
    main()
