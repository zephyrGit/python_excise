# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 09:27
@author : Zephyr
@file   : 02login.py
'''

import urllib
from urllib import request, parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

loginurl = 'http://www.renren.com/Plogin.do'

data = {
    'email': '18588403840',
    'password': 'Changme_123'
}
data = urllib.parse.urlencode(data).encode('utf-8')
req = urllib.request.Request(loginurl, data=data, headers=headers)

response = urllib.request.urlopen(req)

print(response.read())
