# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 12:34
@author : Zephyr
@file   : 08csdn.py
'''
import urllib
from urllib import request, parse
from http import cookiejar
import time

# 创建cookie对象

filename = 'zbcsdn.txt'

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
    "gps": "",
    "username": "18588403840",
    "password": "Changeme_123",
    "rememberMe": "true",
    "lt": "LT-1218793-aAVVSNjXQXQDTpZ1vGGUfQJeBjfpV1",
    "execution": "e14s1",
    "fkid": "WHJMrwNw1k/F/Zf3AruXHYMKu5B1SMIezkwR7Bv3Hhhf8ihaqYwYWBVYUdd0wgVRbCDPKc8odqDYyOIPv1KsVRlxCdkmd1s7Hk9sEAEljDkaklXMeiNY98pSD3EmPbcN1ZkpoFMVOZtj2d7TnjUs4TCQh11mpGwDE2RfKX3m7ZA0kHzaXlGXLfFE7GMYfgSlH4Lbj7fu+FF42bCBM9cOgFa1FbgYIAp/s8N9JR4yfjMbSYq092/A+NHQltbZXcg85LL4jR37UvaKQVtjWZGHAUk0MwWQLnbQc1487582755342",
    "_eventId": "submit",
}

data = urllib.parse.urlencode(data).encode('utf-8')

loginUrl = "https://passport.csdn.net/account/verify"
req = urllib.request.Request(loginUrl, data, headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
time.sleep(1)
