'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 获取节点.py
@time: 2019-07-12 17:28
@desc:
'''
from bs4 import BeautifulSoup as bs

html='''
<title>hello,BeautifulSoup</title>
<div>
<ul name="lgx" >
<li class="item-0"><a href="link1.html">first time</a><span></span></li><li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-inactive"><a href="link3.html">thrid time</a></li>
<li class="item-1 item-2"><a href="link4.html">fourth time</a></li>
<li class="item-0 item-2" name="lgx"><a href="link5.html">fifth time</a></li>
    i am lgx
<p name="lgx"></p>
    hello
</ul>
</div>
'''

soup=bs(html,'lxml')
print(soup.title)
# print(soup.ul)
print(soup.ul.li)
print(soup.ul.li.a)
print(soup.ul.li.a['href'])
#获取ul的直接子孙节点
print(soup.ul.contents)
#获取ul的所有的祖先节点,soup.ul.parents返回的是列表类型,需要用list()输出
# print(list(soup.ul.parents))
#获取ul的父亲节点
print(soup.ul.parent)