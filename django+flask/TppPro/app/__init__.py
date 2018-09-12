# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 9:39
@Author  : Fate
@File    : __init__.py 创建app -- 初始化
'''
# from app == from app.__init__
from flask import Flask
from app.config import config
from app.extensions import extension_config
from app.views import blueprint_config
from app.errors import errors_config

from app.models import *
from app.apis import *


def create_app(config_name):
    '''
    封装创建方法
    :param config_name: 环境名
    :return: app应用
    '''
    # 创建app应用
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config.get(config_name))
    # 额外初始化
    config.get(config_name).init_app(app)

    # 加载扩展
    extension_config(app)

    # 注册蓝本
    blueprint_config(app)

    # 错误捕捉
    errors_config(app)

    return app
