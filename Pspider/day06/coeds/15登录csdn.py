# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 19:28
@author : Zephyr
@file   : 15登录csdn.py
'''

from selenium import webdriver
import time

driver = webdriver.Chrome(r'G:\centbrows\CentBrowser\Application\chromedriver.exe')

driver.get("https://passport.csdn.net/account/login?service=https%3A%2F%2Fwww.csdn.net%2F")

driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/h3/a').click()
time.sleep(1)

username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

username.send_keys('18588403840')
password.send_keys('Changeme_123')

driver.find_element_by_xpath('//*[@id="fm1"]/input[8]').click()
time.sleep(2)

cookie = driver.get_cookies()

print(cookie)

