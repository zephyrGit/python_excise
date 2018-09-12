# -*- coding:utf-8 -*-
'''
@Time    : 2018/8/23 10:16
@Author  : Fate
@File    : test.py
'''
import time
from selenium import webdriver

driver = webdriver.Chrome()
# 登陆操作
driver.maximize_window()
driver.get("http://passport.csdn.net/account/login")
time.sleep(2)

driver.find_element_by_xpath('//div[@class="login-part"]/h3/a').click()
time.sleep(1)

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.send_keys('18588403840')
password.send_keys('Changeme_123')

driver.find_element_by_xpath('//*[@id="fm1"]/input[8]').click()
time.sleep(2)

# 获取cookie
cookies = driver.get_cookies()

print(cookies)