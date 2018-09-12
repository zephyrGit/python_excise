# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 9:41
@Author  : Fate
@File    : config.py 配置文件
'''

import os

# 项目基路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 定义一个配置父类

class Config(object):
    # 通用配置

    # 秘钥
    # app.config['SECRET_KEY'] = '123'
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

    # 数据库
    # 忽略警告
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 邮件
    # 邮箱服务器
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.aliyun.com'
    # 邮箱账号
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'fate9527@aliyun.com'
    # 邮箱密码
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'Changeme_123'

    # 额外的
    @staticmethod
    def init_app(app):
        pass


# 数据库配置
def mysql_config():
    USERNAME = 'root'
    PASSWORD = '123456'
    HOST = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'Tpp'
    return {'USERNAME': USERNAME,
            'PASSWORD': PASSWORD,
            'HOST': HOST,
            'PORT': PORT,
            'DATABASE': DATABASE}


# 定义环境
# 开发环境
class DevelopmentConfig(Config):
    # sqlite
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'DevDB.sqlite')

    # mysql
    SQLALCHEMY_DATABASE_URI = 'mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/Dev{DATABASE}'.format(**mysql_config())


# 测试环境
class TestConfig(Config):
    # sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'TestDB.sqlite')


# 发布环境
class ProductionConfig(Config):
    # sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'ProDB.sqlite')


# 配置字典
config = {
    'development': DevelopmentConfig,
    'test': TestConfig,
    'product': ProductionConfig,
    'default': DevelopmentConfig
}
