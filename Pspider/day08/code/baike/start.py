# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/23 15:09
@Author  : Fate
@File    : start.py
'''

import scrapy.cmdline


def main():

	scrapy.cmdline.execute(['scrapy', 'crawl', 'mybaike'])


if __name__ == '__main__':
	main()