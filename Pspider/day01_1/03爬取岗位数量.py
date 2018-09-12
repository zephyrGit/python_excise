# -*- coding:utf-8 -*-
'''
@time   : 2018-08-13 12:41
@author : Zephyr
@file   : 03爬取岗位数量.py
'''

import urllib
from urllib import request, parse
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getJobNum(jl, kw):
    '''
    获取岗位数量
    :param jl: 地区
    :param kw: 关键字
    :return: 岗位数量
    '''

    search = {'jl': jl, 'kw': kw}
    search = urllib.parse.urlencode(search)
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?' + search

    req = urllib.request.Request(url, headers=headers)

    response = urllib.request.urlopen(req)

    html = response.read().decode('utf8')

    '''
    <em>3010</em>
    '''
    jobre = '<em>(\d+)</em>'
    jobnum = re.findall(jobre, html)[0]
    print(jobnum)


if __name__ == '__main__':
    getJobNum(jl='广州', kw='python')
