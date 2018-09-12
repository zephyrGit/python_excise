# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/22 16:06
@Author  : Fate
@File    : renrenSpider.py
'''
import scrapy


class MywenxinSpider(scrapy.Spider):
    name = 'myrenren'
    # allowed_domains = ['weixin.sogou.com', 'mp.weixin.qq.com']
    start_urls = ['http://weixin.sogou.com/pcindex/pc/pc_0/1.html']

    # 请求前登陆
    def start_requests(self):
        # 表单请求
        # scrapy.Request
        yield scrapy.FormRequest(url='http://www.renren.com/PLogin.do',  # 表单提交url
                                 formdata={
                                     "username": "18588403840",
                                     "password": "Changeme_123"
                                 },  # 提交的表单数据
                                 # callback=
                                 )

    def parse(self, response):
        print(response.text)
