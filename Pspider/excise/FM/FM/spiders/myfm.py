# -*- coding: utf-8 -*-
import json
from FM.items import FmItem, ChapterItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy


class MyfmSpider(CrawlSpider):
    name = 'myfm'
    allowed_domains = ['ximalaya.com']
    start_urls = ['http://www.ximalaya.com/youshengshu/wenxue/p1/']

    # 规则
    rules = [Rule(LinkExtractor(allow=("wenxue/p(\d+)/")), callback='get_parse', follow=True)]

    def get_parse(self, response):
        # print(response.text)
        bookList = response.xpath('//div[@class="content"]//li')

        for book in bookList:
            bookName = book.xpath('.//a[@class="u0jN album-title lg"]/@title').extract()[0]
            bookUrl = "http://www.ximalaya.com" + book.xpath('.//a[@class="u0jN album-title lg"]/@href').extract()[0]
            # print(bookName, bookUrl)

            request = scrapy.Request(url=bookUrl, callback=self.get_book_info)

            request.meta['bookName'] = bookName
            request.meta['bookUrl'] = bookUrl

            yield request

    def get_book_info(self, response):

        # mytree = response.etree.HTML(response)

        bookName = response.meta['bookName']
        bookUrl = response.meta['bookUrl']

        bookInfoList = response.xpath(
            '//div[@class="vd4u album-intro "]//text() | //article[@class="vd4u intro"]//text()')
        bookInfo = ""
        for info in bookInfoList:
            bookInfo += info.extract().strip().replace('<div>', '') + '\n'

        # 书id
        bookID = bookUrl.split('/')[-2]
        mediaUrl = "https://www.ximalaya.com/revision/play/album?albumId={}&pageNum=1&sort=-1&pageSize=1000".format(
            bookID)

        request = scrapy.Request(url=mediaUrl, callback=self.get_media)
        request.meta['bookID'] = bookID
        yield request

        bookItems = FmItem()
        bookItems['bookName'] = bookName
        bookItems['bookInfo'] = bookInfo
        bookItems['bookUrl'] = bookUrl
        yield bookItems

    def get_media(self, response):
        items = ChapterItem()

        bookID = response.meta['bookID']
        mediaData = json.loads(response.text)
        mediaList = mediaData['data']['tracksAudioPlay']
        for media in mediaList:
            # 章节名
            chapter = media['trackName']
            # 章节url、
            chapterUrl = media['src']

            # 书id
            items['bookID'] = bookID

            # 章节名
            items['chapter'] = chapter
            # 章节url、
            items['chapterUrl'] = chapterUrl

            yield items
