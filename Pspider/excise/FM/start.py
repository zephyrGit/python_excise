# -*- coding:utf-8 -*-
'''
@time   : 2018-08-28 20:48
@author : Zephyr
@file   : start.py
'''
import scrapy.cmdline


def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'myfm'])


if __name__ == '__main__':
    main()
