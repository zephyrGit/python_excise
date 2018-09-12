# -*- coding:utf-8 -*-
'''
@time   : 2018-08-15 09:48
@author : Zephyr
@file   : 02广度爬取.py
'''

from queue import Queue

import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getHTML(url):
    '''
    获取网页源码
    :param url
    :return: HTML源码
    '''

    response = requests.get(url, headers=headers)

    return response.content.decode('utf-8', 'ignore')


def getUrl(url):
    '''
    筛选出url
    :param: url,上一层url
    :return:
    '''

    html = getHTML(url)
    '''
    <a href="https://www.baidu.com/link?url=a" target="_blank"><em>富二代</em>_百度百科</a>
    '''
    urlre = '<a .*href=\"(https?://.*?)\" .*>'
    # 预编译
    urlc = re.compile(urlre)

    urlList = urlc.findall(html)
    return urlList


def vastSpider(depth):
    '''
    广度爬虫
    :param depth: 深度
    :return:
    '''
    # 判断队列是否为空
    while urlList:
        url = urlList.pop(0)
        # 判断是否超出层级
        if depthDict[url] <= depth:
            print('\t\t\t' * depthDict[url], "已经抓取了第%d层：%s" % (depthDict[url], url))

            # 生成新的
            sonUrlList = getUrl(url)
            for newUrl in sonUrlList:
                # 去重
                if newUrl not in depthDict:
                    depthDict[newUrl] = depthDict[url] + 1
                    # 加入队列
                    urlList.append(newUrl)


if __name__ == '__main__':
    # 起始url
    starturl = "https://www.baidu.com/s?wd=富二代"
    # 用队列实现 list
    urlList = []
    urlList.append(starturl)

    # 层级控制
    depthDict = {}
    depthDict[starturl] = 1

    # 广度爬虫
    vastSpider(4)
