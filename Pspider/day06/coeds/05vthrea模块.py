# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 10:27
@author : Zephyr
@file   : 05vthrea模块.py
'''
import vthread
import threadpool
from house import *
import time


@vthread.pool(10)
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


time.clock()

# 开启线程
url = 'https://gz.lianjia.com/ershoufang/pg1'
totalPage = getPage(url)

print(totalPage)
print(time.clock())

# url 列表
urlList = []
for i in range(1, totalPage + 1):
    url = 'https://gz.lianjia.com/ershoufang/pg%d' % (i)
    getHouseInfo(url)
