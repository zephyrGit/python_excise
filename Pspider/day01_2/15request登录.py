# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 15:33
@author : Zephyr
@file   : 15request登录.py
'''

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

loginurl = 'http://www.renren.com/PLogin.do'
data = {
    'email': '18588403840',
    'password': 'Changeme_123'
}

# 创建session对象
session = requests.session()
# 保存cookie
res = session.post(url=loginurl, data=data, headers=headers)
print(session.get(url='http://www.renren.com/965557295/profile', headers=headers).text)
# 保存
cookie_dict = requests.utils.dict_from_cookiejar(session.cookies)

print(cookie_dict)

'''
c_dict = {
    '_de': '8799AF8CDA498E75CA882FBE19A95DF9', 'anonymid': 'jktejo069tk5hp', 'first_login_flag': '1',
    'id': '965557295',
    'ln_hurl': 'http://hdn.xnimg.cn/photos/hdn121/20180425/1110/h_main_sUHq_0c140000306f195a.jpg',
    'ln_uact': '18588403840', 'loginfrom': 'syshome', 'p': 'beab1a57465dede929b68712b43f57725',
    'societyguester': '28559929ee22adeecc177dd5bac635d15', 't': 'ebf75001ca076c976947b69ffa2a7bb6',
    'xnsid': 'c89a9d9d', 'JSESSIONID': 'abcYYciiuPe0687hwz3uw'
}

cookie = requests.utils.cookiejar_from_dict(cookie_dict)
session.cookies = cookie


response = requests.post(url=loginurl, data=data, headers=headers)
print(response.text)
print(response.cookies)

# print(requests.get(url='http://www.renren.com/965557295/profile', headers=headers).text)
'''
