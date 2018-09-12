# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/6 10:46
@Author  : Fate
@File    : extensions.py 扩展
'''
from flask_restful import Api
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cache import Cache

# from flask_session import Session 发布时

# 创建扩展实例
api = Api()
bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
migrate = Migrate()
cache = Cache()


# 初始化
def extension_config(app):
    api.init_app(app)  # api=Api(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

