# -*- coding:utf-8 -*-
'''
@time   : 2018-08-15 15:24
@author : Zephyr
@file   : 06抓取基金.py
'''
import requests
import re
from bs4 import BeautifulSoup
import math

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getPageNum():
    url = "http://quote.stockstar.com/fund/stock_3_1_1.html"

    response = requests.get(url, headers=headers).text

    soup = BeautifulSoup(response, 'lxml')

    page = soup.select('#ClientPageControl1_hdnTotalCount')[0]['value']
    pageOfnum = soup.select('#ClientPageControl1_hdnPageSize')[0]['value']

    # print(page)

    return math.ceil(int(page) / int(pageOfnum))


def getStock(url):
    '''
    获取基金
    :param url:
    :return:
    '''
    # url = "http://quote.stockstar.com/fund/stock_3_1_1.html"

    response = requests.get(url, headers=headers).text

    soup = BeautifulSoup(response, 'lxml')

    stockList = soup.select('#datalist > tr')
    for stock in stockList:
        # print(stock)
        # td:nth-child(1)
        stockNum = stock.select("td:nth-of-type(1) > a")[0].text

        stockName = stock.select("td:nth-of-type(2) > a")[0].text
        # 日增长率
        dayUpRate = stock.select("td:nth-of-type(6) > span")[0].text

        print(stockName, stockNum, dayUpRate)


# print(response)
if __name__ == '__main__':
    pageNum = getPageNum()
    print(pageNum)
    for i in range(1, pageNum + 1):
        url = "http://quote.stockstar.com/fund/stock_3_1_%d.html" % i
        getStock(url)
