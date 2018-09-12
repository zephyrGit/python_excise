# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 14:05
@author : Zephyr
@file   : 11PRoxyHandler_代理设置.py
'''
import urllib
from urllib import request, parse
from http import cookiejar
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

proxy = {
    'http': ' "http": "User1:123456@10.3.133.149:808"'
}

# 创建处理器
proxy_handler = urllib.request.ProxyHandler(proxy)

# 打开器
opener = urllib.request.build_opener(proxy_handler)

response = opener.open('http://www.baidu.com')

print(response.read().decode('utf-8'))
