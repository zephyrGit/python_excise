# -*- coding:utf-8 -*-
'''
@time   : 2018-08-13 12:41
@author : Zephyr
@file   : 02get传参.py
'''

import urllib.request
import urllib.parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}


def getWD(wd):
    '''
    浏览器，可搜索
    :return: 响应
    '''

    # url编码
    wd = urllib.parse.urlencode({'wd': wd})
    print(wd)
    print(urllib.request.unquote(wd))
    url = 'https://www.baidu.com/s?' + wd

    requset = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(requset)

    print(response.read())
    print(requset.full_url)


if __name__ == '__main__':
    wd = input('请输入要查询的关键字：')

    getWD(wd)