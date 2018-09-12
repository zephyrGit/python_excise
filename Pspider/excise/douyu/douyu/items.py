# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

    # 存图片
    image_urls = scrapy.Field()  # 图片url
    images = scrapy.Field()  # 图片名


class DouyuMZItem(scrapy.Item):
    # 主播信息
    c2name = scrapy.Field()  # 板块
    nn = scrapy.Field()  # 主播
    rn = scrapy.Field()  # 标签
