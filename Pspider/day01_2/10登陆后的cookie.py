# -*- coding:utf-8 -*-
'''
@time   : 2018-08-14 12:35
@author : Zephyr
@file   : 10登陆后的cookie.py
'''

import urllib
from urllib import request

headers = {
    "Cookie": "uuid_tt_dd=-3705920038524074601_20170731; Hm_lvt_3f9df99a208b69b45eb52cfbe2dc3bf8=1510561964; csdn_tt_dd=v10_b4fc70f1643303b4d87c66b30d665407266cfb3cc6ed17140e554bc233574be7; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=1788*1*PC_VC; kd_user_id=be1b4953-85f0-4eed-9e5d-dd0b1d4f3485; UN=Gi1gamesh; smidV2=2018062216352737436c1b8872fcbc966a91d5ac713708004d4067b7b333010; __utma=17226283.1236257065.1512635217.1526449194.1530158118.6; __utmz=17226283.1530158118.6.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dc_session_id=10_1533535377297.926119; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1534215516,1534215593,1534215630,1534216222; UserName=Gi1gamesh; UserInfo=e4%2F0KRcBGuDj7IYVnnqlWN%2FRNCIJud8Ciis00aMvSW8MKXkiCtk2Y8GOqnj9vmUGWVbqAG4XaSjkjzWnjz14pFJHvnQL3%2B60igh%2FRDrtziNJKJr%2By9dsdgMpr7%2FJIdQx; UserNick=Gi1gamesh; AU=523; BT=1534216980525; UserToken=e4%2F0KRcBGuDj7IYVnnqlWN%2FRNCIJud8Ciis00aMvSW8MKXkiCtk2Y8GOqnj9vmUGWVbqAG4XaSjkjzWnjz14pFJHvnQL3%2B60igh%2FRDrtziPxrO5ka6GN36IS%2FdJy9A%2FhLCnR7AtY97jRLXj57uwJ2vbaEOYY5c2vvJ69Sq6hD07yNMj5BZWSkBTQLqBj6aw6; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1534217029; dc_tos=pdflfu",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

url = "https://my.csdn.net/Gi1gamesh"

req = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))
