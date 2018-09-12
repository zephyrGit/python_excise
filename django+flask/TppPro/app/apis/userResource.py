# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/7 10:19
@Author  : Fate
@File    : userResource.py
'''
import uuid
import hashlib
import re
from flask_restful import Resource, reqparse
from app.models.userModel import User
from app.extensions import db, cache
from app.email import async_send_mail_util
from tasks import send_mail_util
from log import logs

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help="请输入用户名")
parser.add_argument('password', type=str, required=True, help="请输入密码")
parser.add_argument('email', type=str, required=True, help="请输入邮箱")


# 密码加密
def genetrate_password(password):
    hash = hashlib.sha256()
    hash.update(password.encode('utf-8'))
    return hash.hexdigest()


# 用户资源
class UserResource(Resource):
    # 注册
    def post(self):
        # 获取表单数据
        args = parser.parse_args()

        username = args.get('username')
        password = args.get('password')
        email = args.get('email')
        # re 邮箱验证
        mailre = "[a-z0-9_]+@[a-z0-9]+\.[a-z]{2,4}"
        if len(re.findall(mailre, email, re.I)) != 0:
            print(username, password, email)

            u_token = uuid.uuid4()
            print(u_token)
            # password = genetrate_password(password)
            # print(password)

            # 插入
            user = User(username=username,
                        email=email, u_token=u_token)

            user.generate_password(password)

            try:
                db.session.add(user)
                db.session.commit()

                # 发送激活邮
                # 设置缓存，用来保存用户信息{字典}
                cache.set(str(u_token), username, timeout=60 * 2)
                '''
                subject, recipients, emailTmp, **kwargs
                '''

                send_mail_util.delay(subject='账号激活',
                                     recipients=[email],
                                     emailTmp='activationUserEmail',
                                     username=username,
                                     url='http://127.0.0.1:5000/activation?u_token=' + str(u_token))

                # async_send_mail_util(subject='账号激活',
                #                      recipients=[email],
                #                      emailTmp='activationUserEmail',
                #                      username=username,
                #                      url='http://127.0.0.1:5000/activation?u_token=' + str(u_token))

            except Exception as e:
                # 回滚
                # print(e)
                logs().error(e)
                db.session.rollback()
                return {"msg": "用户已存在", 'status': 422}
        else:
            return {"msg": "邮箱格式错误", 'status': 422}

        return {"msg": "用户注册成功", 'status': 201}


# 用户激活资源

parser_token = reqparse.RequestParser()
parser_token.add_argument('u_token', type=str, required=True, help='请发送激活邮件')


class ActivationResource(Resource):
    def get(self):
        args = parser_token.parse_args()

        # print(u_token)

        # 获取
        u_token = args.get('u_token')
        username = cache.get(u_token)

        print(u_token, username)

        # 删除
        cache.delete(u_token)

        user = User.query.filter_by(username=username).first()
        user.u_status = True
        db.session.add(user)

        return {'msg': "账号被激活", 'status': 200}


# 登录后

# login_session = reqparse.RequestParser()
# login_session.add_argument('session', type=str, required=True, location='cookies', help='请登录')

login_token = reqparse.RequestParser()
login_token.add_argument('u_token', type=str, required=True, help='请登录')


# 判断用户权限
def check_permission(permission):
    def check_user_perm(func):
        def check(*args, **kwargs):

            # 判断是否登陆
            args = login_token.parse_args()
            u_token = args.get('u_token')

            # 获取用户
            user = User.query.filter_by(u_token=u_token).first()
            # 查看权限
            # if user.u_permission & permission == permission:

            if user.check_u_permission(permission):
                return func(*args, **kwargs)
            else:
                return {'msg': "充钱吧，少年"}

        return check

    return check_user_perm


class PermissionResource(Resource):
    '''
    1 ---> 浏览
    2 ---> 评论
    4
    '''

    look = 1
    say = 2

    @check_permission(look)
    def get(self):
        return {'msg': '有'}
