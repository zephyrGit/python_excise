# -*- coding: utf-8 -*-

import scrapy
import requests
import lxml
from lxml import etree
from sina.items import SinaItem

from scrapy.linkextractors import LinkExtractor  # 提取连接
from scrapy.spiders import CrawlSpider, Rule  # 爬虫规则


class MysinaSpider(CrawlSpider):
    name = 'mysina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml']

    # 定制规则
    '''
    link_extractor, 规则
    callback=None,  回调
    follow=None, 追踪  如果为True 就追踪
    '''
    '''
     allow=(正则),  允许 --符合正则的提取
     deny=(正则)  不允许 --符合正则的就不提取
    '''
    link_extractor = LinkExtractor(allow=('index_(\d)+.shtml'))
    '''
    tags=('a', 'area'), attrs=('href',)↑
    '''
    rules = [Rule(link_extractor=link_extractor, callback='get_parse', follow=True)]

    def get_content(self, url):
        '''
        获取正文
        :param url: 新闻url
        :return: 正文
        '''
        response = requests.get(url).content.decode('utf-8')
        mytree = lxml.etree.HTML(response)

        contentList = mytree.xpath('.//div[@id="article"]/text()')
        content = ''
        for c in contentList:
            content += c.strip() + '\n'

        return content

    # 一定不能用parse
    def get_parse(self, response):

        # 新闻列表
        newsList = response.xpath('.//ul[@class="list_009"]/li')
        for news in newsList:
            # newsTitle = news.xpath('./a/text()').extract_first()  # 获取真实数据，拿第一个

            # 标题
            newsTitle = news.xpath('./a/text()').extract()[0]  # 返回列表
            # print(newsTitle.get('data'))  # get()

            # url
            newsUrl = news.xpath('./a/@href').extract()[0]

            # 时间
            newsTime = news.xpath('./span/text()').extract()[0]

            # 正文
            # newsContent = self.get_content(newsUrl)

            # print(newsTitle, newsUrl, newsTime)

            '''
             url, callback=None
             meta 传递内容 字典
            '''

            request = scrapy.Request(newsUrl, callback=self.news_content)

            request.meta['newsTitle'] = newsTitle
            request.meta['newsUrl'] = newsUrl
            request.meta['newsTime'] = newsTime
            # 发送请求
            yield request

            # yield scrapy.Request(newsUrl, callback=self.news_content,
            #                      meta={'newsTitle': newsTitle,
            #                            'newsUrl': newsUrl})

    def news_content(self, response):

        # 实例化
        items = SinaItem()

        # 接收传递内容
        newsTitle = response.meta['newsTitle']
        newsUrl = response.meta['newsUrl']
        newsTime = response.meta['newsTime']

        contentList = response.xpath('.//div[@id="article"]/text()')
        content = ''
        for c in contentList:
            content += c.extract().strip() + '\n'

        items['newsTitle'] = newsTitle
        items['newsUrl'] = newsUrl
        items['newsTime'] = newsTime
        items['newsContent'] = content

        yield items
