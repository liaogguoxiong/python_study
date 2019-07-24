'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: find_all(attrs).py
@time: 2019-07-16 14:47
@desc:
'''

from bs4 import BeautifulSoup as bs
html='''
<title>hello,BeautifulSoup</title>
<div>
<ul name="lgx" >
<li class="item-0"><a href="link1.html">first time</a><span></span></li><li class="item-1"><a href="link2.html">second time</a></li>
<li class="item-inactive"><a href="link3.html">thrid time</a></li>
<li class="item-1 item-2" id="lgx"><a href="link4.html">fourth time</a></li>
<li class="item-0 item-2" name="lgx"><a href="link5.html">fifth time</a></li>
    i am lgx
<p name="lgx"></p>
    hello
</ul>
</div>
'''

soup=bs(html,'lxml')
print(soup.find_all(attrs={'class':'item-1 item-2'}))
print(soup.find_all(id='lgx'))
print(soup.find_all(class_='item-1 item-2'))
