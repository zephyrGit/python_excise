# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 19:27
@author : Zephyr
@file   : 13海贼王.py
'''
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}

url = "https://weibo.com/"
print(requests.get(url, headers=headers).text)