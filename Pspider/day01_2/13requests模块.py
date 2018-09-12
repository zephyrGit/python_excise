# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 14:33
@author : Zephyr
@file   : 13requests模块.py
'''
import json

import requests

'''
url, 
params=None,  字典， get参数
**kwargs urllib可用的参数
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

}
response = requests.get('http://www.baidu.com/', headers=headers)
# print(response.text)  # Unicode格式
# print(response.content.decode('utf-8'))  # 字节流


xcresponse = requests.get('https://www.baidu.com/s', {'wd': '西刺代理', 'ie': 'utf-8'}, headers=headers)
print(xcresponse.url)

# 抓取有道翻译 post请求
# 去掉_o
ydurl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {
    'i': '蟒蛇',
    "rom": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "1534229263508",
    "sign": "65d0f683641c0bc3246cb9922531a067",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTIME",
    "typoResult": "false",
}
ydresponse = requests.post(ydurl, data=data, headers=headers)
print(ydresponse.text)
data = json.loads(ydresponse.text)['translateResult'][0]
print(data)

# .json() 转为字典
print(ydresponse.json()['translateResult'][0])
