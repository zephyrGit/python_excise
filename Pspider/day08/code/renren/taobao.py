# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/23 14:37
@Author  : Fate
@File    : taobao.py
'''

import requests

for i in range(10):
    url = "https://s.taobao.com/search?q=T%E6%81%A4&s={}".format(i * 44)
    response = requests.get(url)

    print(response.text)
