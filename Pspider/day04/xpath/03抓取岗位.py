# -*- coding:utf-8 -*-
'''
@time   : 2018-08-16 14:56
@author : Zephyr
@file   : 03抓取岗位.py
'''
import requests
import lxml
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getJob():
    url = "https://jobs.51job.com/guangzhou/p1/"
    response = requests.get(url, headers=headers).content.decode('gbk')
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
        money = job.xpath('.//p[@class="info"]/span[3]/text()')[0]
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


if __name__ == '__main__':
    getJob()
