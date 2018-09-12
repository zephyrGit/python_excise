# -*- coding:utf-8 -*-
'''
@time   : 2018-08-13 14:21
@author : Zephyr
@file   : 05爬取阿里招聘.py
'''
import urllib
from urllib import request, parse
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}


# url = "https://job.alibaba.com/zhaopin/positionList.htm?keyWord=cHl0aG9u&_input_charset=UTF-8&#page/1"

def getPytonJob():
    '''
    获取python岗位
    :return:
    '''
    url = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'

    # 表单数据 字典
    data = {
        "pageSize": "10",
        "t": "0.4097248009187844",
        "keyWord": "python",
        "pageIndex": "1"
    }

    # url编码
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data=data, headers=headers)
    response = urllib.request.urlopen(req)

    response = response.read().decode('utf-8')
    response = json.loads(response)

    returnValue = response['returnValue']['datas']
    print(returnValue)
    for job in returnValue:
        # 部门
        departmentName = job['departmentName']
        # 要求
        requirement = job['requirement']

        print(departmentName, requirement)


def getAllJob(url):
    '''
    获取全国岗位
    :return:
    '''

    data = {
        "pageSize": "10",
        "t": "0.4097248009187844",
        "pageIndex": "1"
    }

    # 获取全部岗位数量页数
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data, headers)
    response = urllib.request.urlopen(req).read()
    data = json.loads(response)
    totalPage = data['returnValue']['totalPage']

    for p in range(1, int(totalPage) + 1):
        data = {
            "pageSize": "10",
            "t": "0.4097248009187844",
            "pageIndex": str(p)
        }

        # 获取全部岗位数量页数
        data = urllib.parse.urlencode(data).encode('utf-8')
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req).read()

        returnValue = json.loads(response)['returnValue']['datas']
        print(returnValue)
        for job in returnValue:
            # 部门
            departmentName = job['departmentName']
            # 要求
            requirement = job['requirement']

            print(departmentName, requirement)


if __name__ == '__main__':
    # 种子
    starturl = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'
    getAllJob(starturl)
