# -*- coding:utf-8 -*-
'''
@time   : 2018-08-22 16:06
@author : Zephyr
@file   : renrenSpider.py
'''
import scrapy


class MyrenrenSpider(scrapy.Spider):
    name = 'myrenren'
    # allowed_domains = ['weixin.sogou.com', 'mp.weixin.qq.com']
    # start_urls = ['http://weixin.sogou.com/pcindex/pc/pc_0/1.html']

    # 请求前登陆
    def start_requests(self):
        # 表单请求
        yield scrapy.FormRequest(url='http://www.renren.com/Plogin.do',  # 表单提交url
                                 formdata={
                                     'email': '18288403840',
                                     'password': 'Changeme_123'
                                 },  # 提交的表单数据
                                 # callback=
                                 )

    def parse(self, response):
        print(response.text)