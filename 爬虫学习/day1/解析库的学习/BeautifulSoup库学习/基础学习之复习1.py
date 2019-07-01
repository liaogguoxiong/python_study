'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 基础学习之复习1.py
@time: 2019-06-27 16:21
@desc:
'''
from bs4 import BeautifulSoup as BS


'''
BeautifulSoup是python的一个html或者xml
的解析库,可以用它来方便地从网页中提取数据
'''

#BeautifulSoup可以自动完整网页结构
soup=BS('<p>hello</p>','lxml')
print(soup)
print("*"*80)

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

soup=BS(html,'lxml')
#print(soup)
print("*"*80)

#获取网页标题
print(soup.title)
print("获取网页标题:",soup.title.string)
print(soup.title.name)


print("li节点:",soup.li)
print("获取li的文本:",soup.li.string)
print("获取li的参数:",soup.li.attrs['class'])
print(soup.a)
print(soup.a.string)
print(soup.p.attrs['name'])
# print(soup.ul.contents)
print(soup.ul.children)
# for i in soup.ul.children:
#     print(i)
print(soup.p.parents)
# print(list(enumerate(soup.p.parents)))
print(soup.p.next_sibling)
print(soup.p.previous_sibling)
print(soup.li.next_sibling.string)
print(list(soup.a.parents)[0])
print(soup.find_all(name='li')[0].text)