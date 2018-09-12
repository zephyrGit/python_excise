# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 10:49
@author : Zephyr
@file   : 07抓包登录.py
'''

import urllib
from urllib import request, parse
from http import cookiejar
import time

# 创建cookie对象

filename = 'zbrenren.txt'

cookie = cookiejar.LWPCookieJar(filename)
# cookie.load(filename, ignore_discard=True, ignore_expires=True)

# 处理器
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

# 打开器
opener = urllib.request.build_opener(cookie_handler)

urllib.request.install_opener(opener)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

data = {
    "email": "18588403840",
    "icode": "",
    "origURL": "http://www.renren.com/home",
    "domain": "renren.com",
    "key_id": "1",
    "captcha_type": "web_login",
    "password": "65d744158a9233dc19f4d7375bfee54e897fa2e2fbc7f6e2c5a446ef980e9d8d",
    "rkey": "449e2cdaaefe6364b26d5b62baab86f5",
    "f": "http%3A%2F%2Fwww.renren.com%2F332095008%2Fprofile",
}

data = urllib.parse.urlencode(data).encode('utf-8')

loginUrl = "http://www.renren.com/ajaxLogin/login?1=1&uniqueTimestamp=2018721021524"

req = urllib.request.Request(loginUrl, data, headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
time.sleep(1)
print(urllib.request.urlopen('http://www.renren.com/967374112/profile').read().decode('utf-8'))
