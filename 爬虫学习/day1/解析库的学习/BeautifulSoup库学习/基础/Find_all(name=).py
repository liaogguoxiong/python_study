'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: Find_all(name=).py
@time: 2019-07-16 13:39
@desc:
'''

from  bs4 import  BeautifulSoup as bs

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
ul=soup.find_all(name='ul')[0]
print(ul)
for li in ul.find_all(name='li'):
    print(li.text)
