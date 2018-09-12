# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 14:34
@author : Zephyr
@file   : 09 matplotlib.py
'''

import matplotlib
from matplotlib import pyplot as plt  # 绘图

# 显示中文
matplotlib.rcParams["font.sans-serif"] = ["simhei"]  # 配置字体
matplotlib.rcParams["font.family"] = "sans-serif"
# (x,y)
# plt.plot([1, 2], [3, 4], '--', color='r', label='line1')
# plt.xlabel('x轴')
# plt.ylabel('y轴')
# plt.legend()  # 绘制
# plt.show()  # 显示

# 柱状图
# left, 位置x轴
# height, y轴
# width=0.8 柱子的大小
plt.bar([1], [123], label='广州')
plt.bar([2], [23], label='梅州')
plt.bar([3], [63], label='八宝粥')
plt.legend()
plt.show()
