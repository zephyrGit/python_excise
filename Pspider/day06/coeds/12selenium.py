# -*- coding:utf-8 -*-
'''
@time   : 2018-08-20 15:50
@author : Zephyr
@file   : 12selenium.py
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# executable_path 驱动路径
driver = webdriver.Chrome(r'G:\centbrows\CentBrowser\Application\chromedriver.exe')

driver.maximize_window()  # 最大窗口

'''
# get 打开网站
# driver.get("https://www.bilibili.com/")

driver.get('https://tieba.baidu.com/')
wd = driver.find_element(By.ID, 'wd1')
wd.clear()  # 清除
# wd.send_keys('海贼王', Keys.ENTER)
wd.send_keys('海贼王')
# 点击
# submit = driver.find_element_by_class_name('search_btn search_btn_enter_ba j_enter_ba search_btn_down')
submit = driver.find_element_by_xpath('//*[@id="tb_header_search_form"]/span[1]/a')
submit.click()

# 获取HTML源码
page_source = driver.page_source

print(page_source)
'''

driver.get('https://weibo.com/')
# 执行脚本
# 保证所有js加载成功
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
print(driver.page_source)
print("***" * 100)

# 动态下拉条
while True:
    # 可能像这样要拉很多次，中间要适当的延时。
    # 如果说说内容都很长，就增大下拉的长度。
    for i in range(10):
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    break

print(driver.page_source)

# # 关闭 关闭父类
# driver.close()
# # 退出 全部关闭
# driver.quit()
