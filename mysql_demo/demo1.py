#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/9 23:00
# @Author : Tom_tao
# @Site : 
# @File : demo1.py
# @Software: PyCharm

import pymysql

conn = pymysql.connect(host='localhost',user='root',password='root',database='pymysql',port=3306)

cursor = conn.cursor()

cursor.execute("select 1")
result = cursor.fetchone()
print(result)

conn.close()