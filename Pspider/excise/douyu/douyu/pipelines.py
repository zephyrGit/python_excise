# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class DownloadImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_urls in item['zbImgItems']['image_urls']:
            return Request(image_urls)


class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item
