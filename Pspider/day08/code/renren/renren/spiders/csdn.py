# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/23 9:44
@Author  : Fate
@File    : csdn.py
'''
import scrapy


class MyrenrenSpider(scrapy.Spider):
    name = 'mycsdn'
    allowed_domains = ['csdn.net']
    start_urls = ['http://passport.csdn.net/account/login',
                  'http://my.csdn.net/my/account/changepwd']

    def __init__(self):
        super(MyrenrenSpider, self).__init__()

        # 结合selenium
        self.driver = None
        # 保存cookie
        self.cookies = None


    def parse(self, response):
        print(response.url)
        print(response.text, '******************'*30)
