#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/20 10:15
# @Author : Tom_tao
# @Site : 
# @File : demo7.py
# @Software: PyCharm

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver_path = r"d:\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

driver.get("hrrps://www.douban.com/")
# 隐式等待
# driver.implicitly_wait(5)
# driver.find_element_by_id('efdfdfdfd')


# 显式等待
element = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID, 'form_email'))
)
print(element)