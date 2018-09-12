# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 09:40
@author : Zephyr
@file   : 03cookie.py
'''

import urllib
from urllib import request, parse
from http import cookiejar  # import cookiejar

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

# 创建一个cookie对象, 用来保存cookie

cookie = cookiejar.CookieJar()

# 创建一个处理器，处理cookie, 提取
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

# 创建打开器
opener = urllib.request.build_opener(cookie_handler)

# 使用打开器打开
response = opener.open('http://www.baidu.com/')
print(response.code)

print(cookie)
cookies = ''
for c in cookie:
    cookies += c.name + c.value + '\n'

print(cookies)
