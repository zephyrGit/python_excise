# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 09:10
@author : Zephyr
@file   : house.py
'''
import requests
import lxml
from lxml import etree
import json
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',

}


def getHouseInfo(url):
    '''
    获取房子信息
    :param url: 页数url
    :return:
    '''
    url = 'https://gz.lianjia.com/ershoufang/pg1'

    response = requests.get(url, headers=headers)
    # print(response.text)

    mytree = lxml.etree.HTML(response.text)

    # 房子列表
    houseList = mytree.xpath('//ul[@class="sellListContent"]/li')

    for house in houseList:
        # pic
        houseImg = house.xpath('./a/img/@data-original')[0]
        # 标题
        houseAlt = house.xpath('./a/img/@alt')[0]
        # address
        houseAddress = house.xpath('.//div[@class="houseInfo"]/a/text()')[0] + \
                       house.xpath('.//div[@class="houseInfo"]/text()')[0]

        # print(houseAddress)
        positionInfo = house.xpath('.//div[@class="positionInfo"]/text()')[0] + \
                       house.xpath('.//div[@class="positionInfo"]/a/text()')[0]

        # 总价
        totalPrice = house.xpath('.//div[@class="totalPrice"]/span/text()')[0] + '万'
        unitPrice = house.xpath('.//div[@class= "unitPrice"]/span/text()')[0]


def getPage(url):
    '''
    获取页数
    :param url: 城市url
    :return: 页数
    '''
    # url = 'https://gz.lianjia.com/ershoufang/pg1'

    response = requests.get(url, headers=headers)
    # print(response.text)

    mytree = lxml.etree.HTML(response.text)
    # 页数
    page = mytree.xpath('.//div[@class="page-box house-lst-page-box"]/@page-data')[0]
    totalPage = int(json.loads(page)['totalPage'])
    print(totalPage)
    return totalPage


if __name__ == '__main__':
    time.clock()
    url = 'https://gz.lianjia.com/ershoufang/pg1'
    totalPage = getPage(url)

    for i in range(1, 11):
        url = 'https://gz.lianjia.com/ershoufang/pg%d/' % (i)
        getHouseInfo(url)

    print(time.clock())
