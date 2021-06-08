#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: solution.py
@time: 2021/01/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""
import re

"""
    爬虫的目标很简单，就是拿到想要的数据。
    这里有一个网站，里面有一些数字。把这些数字的总和，输入到答案框里面，即可通过本关。
    网站url: http://www.glidedsky.com/level/web/crawler-basic-1
    由于网站策略发生变化，cookie无法直接从浏览器拿到，需要登录进行身份鉴权 
"""
import parsel
import requests
from lxml import etree

base_url = 'http://www.glidedsky.com/level/web/crawler-basic-1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
}
# 登录url
login_url = "http://www.glidedsky.com/login"
# 会话保持 在跨请求时保存某些参数
session = requests.session()
# 根据session发送get请求 获取token
token_request = session.get(login_url, headers=headers)
# print(token_request.text)
_token = re.search('"_token" value="(.*?)"', token_request.text).group(1)
print(_token)
data = {
    "_token": _token,
    "email": "tp320670258@gmail.com",
    "password": "tp751825253"
}
# 发送post请求 登录
res = session.post(url=login_url, data=data)
# get请求获取目标页面数据
response = session.get(base_url)
data = etree.HTML(response.text)
# print(response.text)
last_list = "".join(data.xpath('//div[@class="row"]/div/text()')).split()
# 推导式
print(sum(int(i) for i in last_list))

# map
print(sum(map(int, last_list)))

# parsel
selector = parsel.Selector(response.text)
lis = selector.css("div.col-md-1").getall()
# print(lis)
sum = 0
for i in lis:
    num = int(re.findall('\s*([0-9]+)\s', i)[0])
    sum += num
print(sum)