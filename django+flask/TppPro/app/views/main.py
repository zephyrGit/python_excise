# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 10:58
@Author  : Fate
@File    : main.py 主视图
'''

from flask import Blueprint, render_template

# 创建视图对象
main = Blueprint('main', __name__)


@main.route('/index/')
def index():

    return render_template('common/base.html')
    # return "Main Index"
