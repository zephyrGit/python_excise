# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 19:28
@author : Zephyr
@file   : 14登录知乎.py
'''
from selenium import webdriver
import time

driver = webdriver.Chrome(r'G:\centbrows\CentBrowser\Application\chromedriver.exe')

driver.get("https://www.zhihu.com/signup?next=%2F")

driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[2]/span').click()
# driver.find_element_by_link_text("登录").click()

time.sleep(1)
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.send_keys('18588403840')
password.send_keys('Changeme_123')
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()

time.sleep(5)

# 获取cookie
cookie = driver.get_cookies()

print(cookie)
