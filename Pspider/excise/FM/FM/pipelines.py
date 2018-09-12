# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from FM.items import FmItem, ChapterItem


class FmPipeline(object):
    def process_item(self, item, spider):
        # 判断是哪一个item
        if isinstance(item, ChapterItem):
            print(item.items())
        elif isinstance(item, ChapterItem):
            print(item.items(), '+++++++++')
        else:
            pass

        return item
