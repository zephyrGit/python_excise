# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 书名
    bookName = scrapy.Field()
    # 书简介
    bookInfo = scrapy.Field()
    bookUrl = scrapy.Field()


class ChapterItem(scrapy.Item):
    # 书ID
    bookID = scrapy.Field()
    # 章节名
    chapter = scrapy.Field()
    # 章节url、
    chapterUrl = scrapy.Field()

    pass
