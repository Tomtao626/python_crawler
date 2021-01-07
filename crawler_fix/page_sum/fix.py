#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author:tom_tao626 
@license: Apache Licence 
@file: fix.py
@time: 2021/01/07
@contact: tp320670258@gmail.com
@site: xxxx.suizhu.net
@software: PyCharm 
"""
"""
    爬虫的目标很简单，就是拿到想要的数据。
    这里有一个网站，里面有一些数字。把这些数字的总和，输入到答案框里面，即可通过本关。
    网站url: http://www.glidedsky.com/level/web/crawler-basic-1
"""

import requests

base_url = 'http://www.glidedsky.com/level/web/crawler-basic-1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Referer': 'http://www.glidedsky.com/level/crawler-basic-1',
    'Cookie': 'Hm_lvt_020fbaad6104bcddd1db12d6b78812f6=1609990222; _ga=GA1.2.490476567.1609990222; _gid=GA1.2.424318067.1609990222; footprints=eyJpdiI6ImNqS3RrRitWblRVZlNydExmS1AySmc9PSIsInZhbHVlIjoiWDdTVGVKUEVcL1J0UXlRckdUYXQ0S3lPT1V3eTVocmhIRXZTeUJLeGZPZGRSK3hTMU9tMWhQWFYwcU5ucGFmQnciLCJtYWMiOiI0MWIzOTkwMTE2MGU4NzE0YmRmOGUxYzNjOWY3Nzc1MTFjNGQzZjMyZjA3NGM3NjA3ZjBkZjY4NjFkZDk5ODcwIn0%3D; XSRF-TOKEN=eyJpdiI6Ilg1WFA1SXQ0aEZUbkVcLzVJVytyV1pnPT0iLCJ2YWx1ZSI6ImxKajdZemt1NGE2eU5sd3FHU2J4U3k0c1BUenpIQytQUnVaWmVDcStLcmhkdktlWE11bFhDMVlOZTJUSXVkaTEiLCJtYWMiOiI5MWEzN2Y0Y2IzMmE4ZDQ0ZWVjNDI1YzQyNTk2YmU5MTVmYzRkMDFjYjI4YTkyNTBhNzFhNWI1Yzk1OGQ0YWViIn0%3D; glidedsky_session=eyJpdiI6IlFwbzA1NGM3dUhRaG1YRGxIeTU2XC9nPT0iLCJ2YWx1ZSI6IlpHOUtGTjJ0N3BjYW5MRTZPTkhCc1lwWkoyOEZoRGZKbWk4a3JFRVNMRXpHbEJyMFFZS0R2RE1VWnJLck9nRWgiLCJtYWMiOiIzMTg5Mjg0ZWVhZTFjM2JiNTExYWNkODNiMzY3NjA2ZTdmZGQwYTE4Nzg2NDY0NWU2YzA3MzVmYWZkZjJmOTQxIn0%3D; Hm_lpvt_020fbaad6104bcddd1db12d6b78812f6=1609990270'
}
response = requests.get(base_url, headers=headers)
with open('sum.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)
