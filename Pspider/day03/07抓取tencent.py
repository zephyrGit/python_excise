# -*- coding:utf-8 -*-
'''
@time   : 2018-08-15 15:49
@author : Zephyr
@file   : 07抓取tencent.py
'''
import requests
import re
from bs4 import BeautifulSoup
import math

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getPageNum(url):
    response = requests.get(url, headers=headers).text

    # print(response)

    soup = BeautifulSoup(response, 'lxml')

    num = soup.select('.lightblue.total')[0].text

    return math.ceil(int(num) / 10)


def getJobInfo(url):
    url = "https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0"
    response = requests.get(url, headers=headers).text

    # print(response)

    soup = BeautifulSoup(response, 'lxml')
    jobList = soup.find_all('tr', class_=['odd', 'even'])
    # print(jobList)
    for job in jobList:
        jobName = job.select('td:nth-of-type(1) > a')[0].text
        jobUrl = 'https://hr.tencent.com/' + job.select('td:nth-of-type(1) > a')[0]['href']
        jobType = job.select('td:nth-of-type(2)')[0].text
        jobNum = job.select('td:nth-of-type(3)')[0].text

        jobAddr = job.select('td:nth-of-type(4)')[0].text
        jobTime = job.select('td:nth-of-type(5)')[0].text

        print(jobName, jobUrl, jobType, jobNum, jobAddr, jobTime)

        # 写入文本
        with open('tencent.txt', 'a+', encoding='utf-8', errors='ignore') as f:
            f.write(str((jobName, jobUrl, jobType, jobNum, jobAddr, jobTime)) + '\n')
            f.flush()


if __name__ == '__main__':
    url = "https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0"

    pagenum = getPageNum(url)
    print(pagenum)

    for i in range(pagenum):
        url = "https://hr.tencent.com/position.php?keywords=python&lid=0&tid=0&start=%d#a" % (i * 10)
        getJobInfo(url)