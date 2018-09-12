# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 14:14
@Author  : Fate
@File    : errors.py
'''

from flask import render_template


# 处理错误
def errors_config(app):

    @app.errorhandler(404)
    def error_404(e):
        return render_template('error/404.html')


