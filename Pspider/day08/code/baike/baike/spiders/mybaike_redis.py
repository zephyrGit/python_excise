# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider

from baike.items import BaikeItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MybaikeSpider(RedisCrawlSpider):
    name = 'mybaikeRedis'
    allowed_domains = ['baike.baidu.com']
    # start_urls = ['https://baike.baidu.com/item/Python/407313']

    # redis 键名
    redis_key = "mybaike:start_url"

    rules = [Rule(LinkExtractor(allow=("item/(.*)")), callback="get_parse", follow=True)]

    def get_parse(self, response):
        # 实例
        items = BaikeItem()
        # 标题
        title = response.xpath("//dd[@class=\"lemmaWgt-lemmaTitle-title\"]/h1/text()").extract()[0]
        contentList = response.xpath('//div[@class="lemma-summary"]//text()')
        # 描述
        content = ""
        for c in contentList:
            content += c.extract().strip()

        # 存储
        items['title'] = title
        items['content'] = content

        yield items
