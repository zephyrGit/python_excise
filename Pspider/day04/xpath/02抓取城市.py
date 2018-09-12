# -*- coding:utf-8 -*-
'''
@time   : 2018-08-16 14:39
@author : Zephyr
@file   : 02抓取城市.py
'''
import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

cityUrl = 'http://jobs.51job.com/'


def getCity(url):
    response = requests.get(url, headers=headers)
    # gb2312 常见简体
    # gbk 简体和繁体
    html = response.content.decode('gbk')
    mytree = lxml.etree.HTML(html)

    cityList = mytree.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/a')
    for city in cityList:
        cityName = city.xpath('./text()')[0]
        cityHref = city.xpath('./@href')[0]
        print(cityName, cityHref)


if __name__ == '__main__':
    getCity(cityUrl)
