# -*- coding: utf-8 -*-
import scrapy
from baike.items import BaikeItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MybaikeSpider(CrawlSpider):
    name = 'mybaike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/Python/407313']

    rules = [Rule(LinkExtractor(allow=("item/(.*)")), callback="get_parse", follow=True)]

    def get_parse(self, response):
        # 实例
        items = BaikeItem()
        # 标题
        title = response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()').extract()[0]
        contentList = response.xpath('//div[@class="lemma-summary"]//text()')
        # 描述
        content = ""
        for c in contentList:
            content += c.extract().strip()

        # 存储
        items['title'] = title
        items['content'] = content

        yield items
