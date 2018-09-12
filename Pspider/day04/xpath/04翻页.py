# -*- coding:utf-8 -*-
'''
@time   : 2018-08-16 15:27
@author : Zephyr
@file   : 04翻页.py
'''
import requests
import lxml
from lxml import etree
import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getPage(url):
    '''
    获取页数
    :param url:
    :return:
    '''
    # url = "https://jobs.51job.com/guangzhou/p1/"
    response = requests.get(url, headers=headers).content.decode('gbk')
    mytree = lxml.etree.HTML(response)

    totalPage = mytree.xpath('//*[@id="hidTotalPage"]/@value')[0]
    return int(totalPage)


def getCity(url):
    '''
    获取城市列表
    :param url:
    :return:
    '''
    response = requests.get(url, headers=headers)
    # gb2312 常见简体
    # gbk 简体和繁体
    html = response.content.decode('gbk')
    mytree = lxml.etree.HTML(html)

    cityDict = {}
    cityList = mytree.xpath('/html/body/div[2]/div[2]/div[2]/div[1]/a')
    for city in cityList:
        cityName = city.xpath('./text()')[0]
        cityHref = city.xpath('./@href')[0]
        print(cityName, cityHref)

        cityDict[cityName] = cityHref
    return cityDict


def getJob(url):
    '''
    获取岗位信息
    :param url:
    :return:
    '''
    # url = "https://jobs.51job.com/guangzhou/p1/"
    response = requests.get(url, headers=headers).content.decode('gbk', 'ignore')
    mytree = lxml.etree.HTML(response)

    jobList = mytree.xpath('//div[@class="detlist gbox"]/div')
    for job in jobList:
        # 岗位名
        jobName = job.xpath('.//p[@class="info"]/span/a/@title')[0]
        jobHref = job.xpath('.//p[@class="info"]/span/a/@href')[0]
        # 公司名
        company = job.xpath('.//p[@class="info"]/a/@title')[0]
        # 地址
        address = job.xpath('.//p[@class="info"]/span[2]/text()')[0]

        # 薪资
        money = job.xpath('.//p[@class="info"]/span[3]/text()')
        if len(money) != 0:
            money = money[0]
        else:
            money = '面议'
        # print(jobName, jobHref, company, address, money)

        # 要求
        orderList = job.xpath('.//p[@class="order"]/text()')
        order = ""
        for o in orderList:
            order += o.strip()
        print(order)

        # 职责
        jobRes = job.xpath('.//p[@class="text"]/@title')[0]
        print(jobRes)

        # 返回
        yield {
            "jobName": jobName,
            "jobHref": jobHref,
            "company": company,
            "address": address,
            "money": money,
            "order": order,
            "jobRes": jobRes,
        }


if __name__ == '__main__':
    cityUrl = 'http://jobs.51job.com/'
    cityDict = getCity(cityUrl)

    for cityName, cityHref in cityDict.items():
        totalPage = getPage(cityHref)
        for i in range(1, totalPage + 1):
            # 拼接url
            url = cityHref + "p%d" % i
            # 写入文本
            with open('./job/' + cityName + '.txt', 'a+', encoding='utf-8', errors='ignore') as f:
                for data in getJob(url):
                    f.write(str((data['jobName'], data['jobHref'],
                                 data['company'], data['address'],
                                 data['money'], data['order'], data['jobRes'] + '\n')))
                    f.flush()
