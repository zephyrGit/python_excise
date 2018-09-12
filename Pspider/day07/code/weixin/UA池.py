# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/22 14:30
@Author  : Fate
@File    : UA池.py
'''

from fake_useragent import UserAgent

# 实例
ua = UserAgent()

# ie
print(ua.ie)

print(ua.chrome)

# 随机
print(ua.random)
