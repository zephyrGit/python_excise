# -*- coding: utf-8 -*-
import scrapy


class MyrenrenSpider(scrapy.Spider):
    name = 'myrenren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/965557295/profile']

    def start_requests(self):
        yield scrapy.FormRequest(url="http://www.renren.com/PLogin.do",  # 表单提交url
                                 formdata={
                                     "email": "18588403840",
                                     "password": "Changeme_123"
                                 },  # 表单数据
                                 callback=self.get_page
                                 )

    def parse(self, response):
        print(response.text)

    def get_page(self, response):
        print(response.text, '============')
        #
        for url in self.start_urls:
            yield self.make_requests_from_url(url)
