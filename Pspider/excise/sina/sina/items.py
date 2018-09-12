# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 标题
    newsTitle = scrapy.Field()
    # 时间
    newsTime = scrapy.Field()
    # url
    newsUrl = scrapy.Field()
    # 正文
    newsContent = scrapy.Field()

    pass
