# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 10:28
@author : Zephyr
@file   : 06使用保存cookie.py
'''
import urllib
from urllib import request, parse
from http import cookiejar
import time

# 创建cookie 对象
filename = 'renren.txt'

cookie = cookiejar.LWPCookieJar(filename)
cookie.load(filename, ignore_discard=True, ignore_expires=True)

# 处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

# 打开器
opener = urllib.request.build_opener(cookie_handler)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

urllib.request.install_opener(opener)

req = urllib.request.Request('http://www.renren.com/967374112/profile', headers=headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
