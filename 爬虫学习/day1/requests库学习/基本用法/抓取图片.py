#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 14:46
#!@Filename:抓取图片.py

import requests
url='https://github.com/favicon.ico'
r=requests.get(url)
print(r.text)
print(r.content)
# with open('C:/Users/xiao/Desktop/picture/icon.ico','wb') as f:
#     f.write(r.content)