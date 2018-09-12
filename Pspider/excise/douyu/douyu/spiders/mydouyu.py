# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem


class MydouyuSpider(scrapy.Spider):
    name = 'mydouyu'
    allowed_domains = ['douyu.com']
    start_urls = ['http://www.douyu.com/gapi/rkc/directory/2_201/2']

    def parse(self, response):
        # print(response.text)
        # 主播
        zbItems = DouyuItem()
        data = json.loads(response.text)['data']['rl']

        # 图片
        zbImgItems = DouyuItem()

        print(data)
        '''
        image_urls = scrapy.Field()  # 图片url
        images = scrapy.Field()  # 图片名
        
        c2name = scrapy.Field()  # 板块
        nn = scrapy.Field()  # 主播
        rn = scrapy.Field()  # 标签
        '''
        for mz in data:
            # for mz in data:
            # 主播信息
            c2name = mz['c2name']
            nn = mz['nn']
            rn = mz['rn']

            zbItems['c2name'] = c2name
            zbItems['nn'] = nn
            zbItems['rn'] = rn

            # 图片
            image_urls = mz['rs1']
            images = mz['nn']

            # zbImgItems['image_urls'] = [image_urls]  # 图片是个列表
            # zbImgItems['images'] = images

            # yield zbItems
            yield zbImgItems
