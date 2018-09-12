# -*- coding:utf-8 -*-
'''
@time   : 2018-08-15 14:08
@author : Zephyr
@file   : 05智联.py
'''
import re
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getJobInfo(url):
    '''
    获取岗位详细信息
    :return:
    '''
    response = requests.get(url, headers=headers).content.decode('gbk')
    soup = BeautifulSoup(response, 'lxml')
    jobResponsebilityList = soup.select('div.bmsg.job_msg.inbox > p')

    jobResponsebility = ''

    for jobRes in jobResponsebilityList:
        jobResponsebility += jobRes.text

    print(jobResponsebility)
    return jobResponsebility


def getJob(url):
    url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html'
    response = requests.get(url, headers=headers).content.decode('gbk')
    # print(response)

    soup = BeautifulSoup(response, 'lxml')

    jobList = soup.select('#resultList > div.el')
    # print(jobList)

    for job in jobList[1:]:
        # resultList > div:nth-child(4) > span.t2 > a
        # resultList > div:nth-child(4) > span.t3
        jobName = job.select('span:nth-of-type(1) > a')[0]['title']

        jobUrl = job.select('span:nth-of-type(1) > a')[0].attrs['href']

        jobInfo = getJobInfo(jobUrl)

        company = job.select('span.t2 > a')[0]['title']

        jobAddr = job.select('span.t3')[0].text

        money = job.select('span.t4')[0].text

        time = job.select('span.t5')[0].text

        print(jobName, jobUrl, company, jobAddr, money, time, jobInfo)


def getPageNum(url):
    '''
    获取岗位页数
    :param url: 首页
    :return: 页数
    '''
    response = requests.get(url, headers=headers).content.decode('gbk')

    soup = BeautifulSoup(response, 'lxml')

    pageNum = soup.select('div.p_in > .td')[0].text[1:3]

    print(pageNum)

    return int(pageNum)


if __name__ == '__main__':
    # getJobInfo(' https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html')
    # getJob()
    startUrl = url = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html'

    pagenum = getPageNum(startUrl)
    for num in range(1, pagenum + 1):
        newurl = 'https://search.51job.com/list/030200,000000,0000,00,9,99,python,2,%d.html' % num
        getJob(newurl)
