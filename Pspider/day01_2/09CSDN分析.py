# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 11:11
@author : Zephyr
@file   : 09CSDN分析.py
'''

import urllib
from urllib import request, parse
import re
from http import cookiejar

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
url = 'https://passport.csdn.net/account/login'

req = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')
print(html)

'''
<input type="hidden" name="lt" value="LT-1347301-Vf0bibJIj7TqE55Dq6SsRwjxxok4be" />
<input type="hidden" name="execution" value="e1s1" />
<input type="hidden" name="fkid" id="fkid" value="" />
'''
ltre = r'<input type="hidden" name="lt" value="(.*?)" />'
executionre = r'<input type="hidden" name="execution" value="(.*?)" />'
lt = re.findall(ltre, html)[0]
execution = re.findall(executionre, html)[0]
fkid = "WHJMrwNw1k/F/Zf3AruXHYMKu5B1SMIezkwR7Bv3Hhhf8ihaqYwYWBVYUdd0wgVRbCDPKc8odqDYyOIPv1KsVRlxCdkmd1s7HNv2h6qHuX4s7WZEu6b+7cpSD3EmPbcN1b2GXgZ5AQVIA/R0GgkaFOwnrIytb2HmLQP0UmbgNi02uOX53ZfF9WDwJCZB+QxoN70gHyP09qdPNtAKvckCXn08P/whVDYFkZo1qCSY6I8ltQCuaI7Ld0twuOXG+4ocFQ2C5nbwxLKYXXT+s9g2g3A==1487582755342"

print(lt, execution)

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
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh,en;q=0.9,zh-CN;q=0.8",
    "Connection": "keep-alive",
    "Host": "passport.csdn.net",
    'Referer': 'https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

data = {
    "gps": "",
    "username": "18588403840",
    "password": "Changeme_123",
    "rememberMe": "true",
    "lt": lt,
    "execution": execution,
    "fkid": fkid,
    "_eventId": "submit",
}

data = urllib.parse.urlencode(data).encode('utf-8')

loginUrl = "http://passport.csdn.net/account/verify"
req = urllib.request.Request(loginUrl, data, headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
