# -*- coding:utf-8 -*-
'''
@time   : 2018-08-13 16:15
@author : Zephyr
@file   : 07安全证书.py
'''

import urllib
from urllib import request, parse
import json
import ssl

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# 忽略安全证书
context = ssl._create_unverified_context()

url = 'https://www.12306.cn/mormhweb/'
req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req, context=context)
print(response.read())
