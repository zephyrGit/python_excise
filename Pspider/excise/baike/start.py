# -*- coding:utf-8 -*-
'''
@time   : 2018-08-23 15:09
@author : Zephyr
@file   : start.py
'''
import scrapy.cmdline


def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'mybaike'])


if __name__ == '__main__':
    main()
