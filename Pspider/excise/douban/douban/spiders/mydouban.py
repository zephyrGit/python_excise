# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem


class MydoubanSpider(scrapy.Spider):
    name = 'mydouban'
    allowed_domains = ['movie.douban.com/']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):

        movieList = response.xpath('.//div[@class="item"]')
        for i in movieList:
            item = DoubanItem()
            item['ranking'] = i.xpath('.//div[@class="pic"]/em/text()').extract()
            item['movieName'] = i.xpath('.//div[@class="pic"]/a/img/@alt').extract()
            item['AD'] = i.xpath('.//div[@class="bd"]/p/text()').extract()
            item['score'] = i.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract()
            item['commentNum'] = i.xpath('.//div[@class="star"]/span[4]/text()').extract()

            yield item
            pass

        #     # 翻页
        # next_page = response.xpath('.//span[@class="next"]/a/@href')
        # if next_page:
        #     url = response.urljoin(next_page[0].extract())
        #     yield scrapy.Request(url, self.parse)

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield scrapy.Request(next_url, callback=self.parse)
