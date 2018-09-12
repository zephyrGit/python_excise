# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/8 15:24
@Author  : Fate
@File    : tasks.py celery
'''

from celery import Celery
import redis
import time

from flask import render_template, current_app
from flask_mail import Message

cpp = Celery('tasks', broker='redis://127.0.0.1:6379')


@cpp.task
def add(x, y):
    time.sleep(5)
    print(x + y)


@cpp.task
def send_mail_util(subject, recipients, emailTmp, **kwargs):
    # 获取当前app
    app = current_app._get_current_object()
    msg = Message(subject=subject,
                  recipients=recipients,
                  sender=app.config['MAIL_USERNAME'])

    # 使用模板发送
    msg.html = render_template('email/' + emailTmp + '.html', **kwargs)


if __name__ == '__main__':
    add.delay(3, 8)
    print("程序运行结束")
