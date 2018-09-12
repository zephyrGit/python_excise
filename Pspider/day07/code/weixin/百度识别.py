# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/22 11:42
@Author  : Fate
@File    : 百度识别.py
'''

from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '11710998'
API_KEY = 'YjjZaiMyNGiwUt4441BuInjf'
SECRET_KEY = 'bL0AVxD6tdegOkwiHEz9AoBq8Zn0R4kL'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('zz.png')

""" 调用通用文字识别, 图片参数为本地图片 """
res = client.basicGeneral(image)
print(res)
