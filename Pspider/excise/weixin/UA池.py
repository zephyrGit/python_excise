# -*- coding:utf-8 -*-
'''
@time   : 2018-08-22 14:31
@author : Zephyr
@file   : UA池.py
'''
from fake_useragent import UserAgent

# 实例
ua = UserAgent()

# ie
print(ua.ie)

print(ua.chrome)

# 随机
print(ua.random)
