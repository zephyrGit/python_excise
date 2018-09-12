# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/22 16:30
@Author  : Fate
@File    : newRenrenSpider.py
'''
import scrapy
from scrapy.http import HtmlResponse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MyNewrenrenSpider(CrawlSpider):
    name = 'newRen'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/353111356/profile']

    rules = [Rule(LinkExtractor(allow=("/(\d+)/profile")), callback="get_parse", follow=True)]

    def start_requests(self):
        # 获取登陆前校验
        yield scrapy.Request(url="http://www.renren.com/",
                             meta={"cookiejar": 1},  # 开启cookie，用来保存cookie,在setting把COOKIES_ENABLED设为True
                             callback=self.login)

    def login(self, response):
        # 登陆
        yield scrapy.FormRequest.from_response(response
                                               , url="http://www.renren.com/PLogin.do",  # 表单提交url
                                               formdata={
                                                   "email": "18588403840",
                                                   "password": "Changeme_123"
                                               },  # 表单数据
                                               meta={"cookiejar": response.meta['cookiejar']},  # 保存cookie并传递
                                               callback=self.after_login,
                                               )

    def after_login(self, response):
        print(response.text, '============')
        #
        # for url in self.start_urls:
        #     yield self.make_requests_from_url(url)

        for url in self.start_urls:
            # 传递cookie
            yield scrapy.Request(url, meta={"cookiejar": response.meta['cookiejar']})

    def get_parse(self, response):
        print(response.text)

    def _requests_to_follow(self, response):
        if not isinstance(response, HtmlResponse):
            return
        seen = set()
        for n, rule in enumerate(self._rules):
            links = [lnk for lnk in rule.link_extractor.extract_links(response)
                     if lnk not in seen]
            if links and rule.process_links:
                links = rule.process_links(links)
            for link in links:
                seen.add(link)
                r = self._build_request(n, link)
                # 下面这句是我重写的
                # 更新cookie
                r.meta.update(rule=n, link_text=link.text, cookiejar=response.meta['cookiejar'])
                yield rule.process_request(r)
