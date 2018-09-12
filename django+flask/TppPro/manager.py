# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 9:32
@Author  : Fate
@File    : manager.py 管理模块
'''
from flask_script import Manager
from flask_migrate import MigrateCommand
from app import create_app
import os

# 环境
config_name = os.environ.get('CONFIG_NAME') or 'default'
# 创建app
app = create_app(config_name)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.route('/')
def hello():
    return "Hello World"


if __name__ == '__main__':
    manager.run()
