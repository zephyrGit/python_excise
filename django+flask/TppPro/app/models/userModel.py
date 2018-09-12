# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/7 10:13
@Author  : Fate
@File    : userModel.py 用户模块
'''
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    '''
    - 用户名
    - 密码
    - 邮箱
    - 手机号
    - 用户状态（激活否）
    - 用户token

    '''

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(32), nullable=False)
    u_status = db.Column(db.Boolean, default=False)
    u_token = db.Column(db.String(265), nullable=False)

    # 权限
    u_permission = db.Column(db.Integer, default=1)

    # 密码加密
    def generate_password(self, password):
        return generate_password_hash(password)

    # 密码匹配
    def check_password(self, password):
        return check_password_hash(self.password, password)

    # 检测权限
    def check_u_permission(self, permission):
        return self.u_permission & permission == permission
