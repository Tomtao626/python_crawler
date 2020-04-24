#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/24 7:05 下午
# @Author : admin
# @Software: PyCharm
# @File: test.py

# -*- coding: utf-8 -*-

# excel取数据



import xlrd

data = xlrd.open_workbook('acbm_apply.xlsx')
# 根据下标取sheet
table = data.sheets()[1]
# 用列表存取查询到的产品OE编号数据
pid_list = list()
# 根据下标取名称为'OE编号'所在列的数据 并进行切片去掉标题行
ls = table.col_values(1)[1:]
print(ls)


# 整合纠正数据


# 对取到的全部OE编码数据进行遍历

for i in range(len(ls)):
    # print(str(ls[i]).replace(" ","").replace(".0",""))
    print("当前序号：%s --- 对应数值：%s" % (i + 1, str(ls[i]).replace(" ", "").replace("-", "")))
    # 生成所需的dict结构 并纠正数据
    pid_ds = {
        'pids': (str(ls[i]).replace(" ", "").replace("-",""))
    }
    # pid_ds = {
    #     'pids':(table.row_values(i)[0]).replace(" ", ""),
    # }
    # 存入列表
    pid_list.append(pid_ds)
print(pid_list)


# OE数据转存txt格式


import json
import requests
f = open('pids_2020_04_24_acbm', 'w')
for _pid in pid_list[0:]:
    url = f"http://192.168.191.170:7070/pid_accurate_search?pids={_pid.get('pids')}"
    response = requests.get(url)
    data = json.loads(response.text)
    if data.get('data', []):
        pdata = data.get('data', [])[0]
        brandCode, pid, lable = pdata.get('brandCode'), pdata.get('pid'), pdata.get('label')
        f.write(f'{brandCode},{pid},{lable}\n')
f.close()


# 操作txt数据,存库

# from models.goods.part_category import CategoryPartsMapping
# filename = "pids_2020_04_24_acbm.txt"
# with open(filename, 'r') as file_to_read:
#     l = file_to_read.readlines()
#     for i in l:
#         try:
#             re_data = i[:i.find('<')][:i.find('（')].strip().replace("、", "").replace("、", "").split(",")
#             cam = CategoryPartsMapping.get_or_none(CategoryPartsMapping.pid==re_data[1])
#             if cam:
#                 continue
#             cam = CategoryPartsMapping()
#             cam.category_id = 212
#             cam.public_category_id = 212
#             cam.brandCode = re_data[0]
#             cam.pid = re_data[1]
#             cam.name = re_data[2]
#             cam.save()
#         except:
#             continue