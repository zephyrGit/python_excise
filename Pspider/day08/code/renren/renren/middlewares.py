# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random

from scrapy import signals
from scrapy.downloadermiddlewares.cookies import CookiesMiddleware
from scrapy.downloadermiddlewares.httpproxy import HttpProxyMiddleware

from renren.settings import PROXIES, COOKIE
from selenium import webdriver
import time
from scrapy.http import HtmlResponse
import requests


class SeleniumMiddleware(object):
    '''
    登陆selenium插件，用于获取cookie
    '''

    # 用一次

    def process_request(self, request, spider):
        # 判断是哪个爬虫
        if spider.name == "mycsdn":
            # 判断是否是登陆
            if request.url.find('login') != -1:
                # 使用selenium
                spider.driver = webdriver.Chrome()
                # 登陆操作
                spider.driver.maximize_window()
                spider.driver.get(request.url)
                time.sleep(2)

                spider.driver.find_element_by_xpath('//div[@class="login-part"]/h3/a').click()
                time.sleep(1)

                username = spider.driver.find_element_by_name('username')
                password = spider.driver.find_element_by_name('password')

                username.send_keys('18588403840')
                password.send_keys('Changeme_123')

                spider.driver.find_element_by_xpath('//*[@id="fm1"]/input[8]').click()
                time.sleep(2)

                # 获取cookie 保存
                spider.cookies = spider.driver.get_cookies()

                print(spider.cookies)

                spider.driver.quit()
                return HtmlResponse(url=spider.driver.current_url,  # 当前url
                                    body=spider.driver.page_source,  # html源码
                                    encoding='utf-8')
            # 不是登陆
            else:

                # request.cookies = {}
                # session
                session = requests.session()
                # 设置cookie
                for cookie in spider.cookies:
                    session.cookies.set(cookie['name'], cookie['value'])

                session.headers.clear()
                response = session.get(request.url)

                # response
                return HtmlResponse(url=request.url,
                                    body=response.text,
                                    encoding='utf-8')



class RandomCookieMiddleware(CookiesMiddleware):
    '''
    随机cookie池
    '''

    def process_request(self, request, spider):
        cookie = random.choice(COOKIE)

        print(cookie)
        request.cookies = cookie


class ExtendsProxy(HttpProxyMiddleware):
    '''
    随机IP池
    '''

    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        print(proxy)
        request.meta['proxy'] = 'http://' + proxy


class RenrenSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
