# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 19:46
@author : Zephyr
@file   : 16使用cookie_dict.py
'''

import requests

from http import cookiejar

filename = 'renren.txt'

# cookie = cookiejar.LWPCookieJar()
# cookie.load(filename, ignore_discard=True, ignore_expires=True)
# print(cookie)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Referer": "http://www.renren.com/"
}

c_dict = {'_de': '8799AF8CDA498E75CA882FBE19A95DF9', 'anonymid': 'jkthf5ktrehhof', 'first_login_flag': '1',
          'id': '965557295',
          'ln_hurl': 'http://hdn.xnimg.cn/photos/hdn121/20180425/1110/h_main_sUHq_0c140000306f195a.jpg',
          'ln_uact': '18588403840', 'loginfrom': 'syshome', 'p': '6fe88714d96b6be9098a5012cd26971f5',
          'societyguester': '28559929ee22adeecc177dd5bac635d15', 't': 'ebf75001ca076c976947b69ffa2a7bb6',
          'xnsid': 'c850f0f0', 'JSESSIONID': 'abcldHUzgSeDw7e_WR3uw'}

change_cookie = {'anonymid': 'jfcb0wwz-aaoe7i', '_r01_': '1', 'ln_uact': '18588403840',
                 '__utma': '151146938.389542758.1524625502.1524625502.1524625502.1',
                 '__utmz': '151146938.1524625502.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/965557295/profile',
                 'ln_hurl': 'http://hdn.xnimg.cn/photos/hdn121/20180425/1110/h_main_sUHq_0c140000306f195a.jpg',
                 '_ga': 'GA1.2.389542758.1524625502', 'depovince': 'GUZ', 'JSESSIONID': 'abc6JJ-hAirX3ecwII3uw',
                 'ick_login': '136c74d0-d373-4361-9331-28609e837615',
                 'jebecookies': '3728f908-550f-4a6c-bfd3-f54b834b5a4b|||||', '_de': '8799AF8CDA498E75CA882FBE19A95DF9',
                 'p': 'beab1a57465dede929b68712b43f57725', 'first_login_flag': '1',
                 't': '28559929ee22adeecc177dd5bac635d15', 'societyguester': '28559929ee22adeecc177dd5bac635d15',
                 'id': '965557295', 'xnsid': 'c85dbd84', 'loginfrom': 'syshome', 'wp_fold': '0'}

cookie = requests.utils.cookiejar_from_dict(change_cookie)
# print(cookie)
# # for c in cookie:
# # 创建session对象

session = requests.session()
session.cookies = cookie

# for c in cookie:
#     session.cookies.set(c.name, c.value)

# print(session.get('http://www.renren.com/965557295/profile', allow_redirects=False).text)
print(session.get(url='http://www.renren.com/965557295/profile', headers=headers).text)
