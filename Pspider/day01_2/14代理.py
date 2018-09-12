# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 15:15
@author : Zephyr
@file   : 14代理.py
'''

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# {'协议（小写）'：“协议：//用户名：密码@ip：port”}

proxy = {
    'https': 'http://User1:123456@10.3.133.149:808',
    # 'http': '10.3.133.146:808'
}

response = requests.get('https://blog.csdn.net/wangxw1803', headers=headers, proxies=proxy)

print(response)
print(response.cookies)
