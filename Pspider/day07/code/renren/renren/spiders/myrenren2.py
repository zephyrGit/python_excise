# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MyrenrenSpider(CrawlSpider):
    name = 'myrenren2'
    allowed_domains = ['renren.com']

    start_urls = ['http://www.renren.com/353111356/profile']

    rules = [Rule(LinkExtractor(allow=("/(\d+)/profile")), callback="get_parse", follow=True)]

    def start_requests(self):
        yield scrapy.FormRequest(url="http://www.renren.com/PLogin.do",  # 表单提交url
                                 formdata={
                                     "email": "18588403840",
                                     "password": "Changeme_123"
                                 },  # 表单数据
                                 callback=self.after_login
                                 )

    def after_login(self, response):
        print(response.text, '============')
        #
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def get_parse(self, response):
        print(response.text)
