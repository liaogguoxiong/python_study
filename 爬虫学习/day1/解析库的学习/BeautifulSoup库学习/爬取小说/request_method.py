'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: request_method.py
@time: 2019-06-28 9:59
@desc:用于获取
'''
import requests
from bs4 import BeautifulSoup as BS

def get_soup(url):

    res=requests.get(url)
    # 让res.text正确解码网页内容
    res.encoding = res.apparent_encoding
    soup=BS(res.text,'lxml')
    return soup
