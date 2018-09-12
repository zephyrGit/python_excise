# -*- coding: utf-8 -*-
import datetime
import scrapy
import re
import json


class MywenxinSpider(scrapy.Spider):
    name = 'myweixin'
    # allowed_domains = ['weixin.sogou.com', 'mp.weixin.qq.com']
    start_urls = ['http://weixin.sogou.com/pcindex/pc/pc_0/1.html']

    # def start_requests(self):

    def parse(self, response):

        # print(response.text)
        publicNumList = response.xpath('//div[@class="txt-box"]')
        for wx in publicNumList:
            # 微信公众号url
            wechatPublicNumurl = wx.xpath('.//div[@class="s-p"]/a/@href').extract()[0]

            # 构建请求
            yield scrapy.Request(url=wechatPublicNumurl, callback=self.get_weichatPublic)

            # print(wechatPublicNum,wechatPublicNumurl)

        # 翻页
        for i in range(1, 20):
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
            }
            url = "http://weixin.sogou.com/pcindex/pc/pc_0/{}.html".format(i)
            yield scrapy.Request(url, callback=self.parse, headers=headers)

    def get_weichatPublic(self, response):
        '''
        获取公众号
        :param response:
        :return:
        '''

        html = response.text
        # print(html)
        # 公众号
        wechatPublicNum = response.xpath('//p[@class="profile_account"]/text()').extract()[0]

        # # 昵称
        wechatPublicNickname = response.xpath('//strong[@class="profile_nickname"]/text()').extract()[0].strip()

        # # 二维码
        QRcode = "http://mp.weixin.qq.com" + response.xpath('//img[@id="js_pc_qr_code_img"]/@src').extract()[0].strip()

        # # 文章正则
        articleRe = "msgList = (.*)?;"

        articleJson = re.findall(articleRe, html)[0]
        # print(articleJson, '==============')

        data = json.loads(articleJson)

        for articleList in data['list']:
            article_msg_item_list = articleList['app_msg_ext_info']['multi_app_msg_item_list']
            # 文章标题1
            title1 = articleList['app_msg_ext_info']['title']
            # 文章1时间
            time1 = articleList['comm_msg_info']['datetime']

            time1 = datetime.datetime.fromtimestamp(time1)
            print(title1, time1)

            if article_msg_item_list:
                for article_msg in article_msg_item_list:
                    # 文章标题2
                    title2 = article_msg['title']
                    print(title2, time1)

                    print(wechatPublicNickname, wechatPublicNum, QRcode)
