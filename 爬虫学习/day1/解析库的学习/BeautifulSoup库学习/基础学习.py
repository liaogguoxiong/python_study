#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-14 13:59
#!@Filename:基础学习.py

'''
BeautifulSoup是python的一个html或者xml
的解析库,可以用它来方便地从网页中提取数据
'''
from bs4 import BeautifulSoup as BS
import re
soup=BS('<p>hello</p>','lxml')
print(soup)
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

'''
节点选择器
'''
soup=BS(html,'lxml')
print(soup)
print("获取网页中的标题的内容:",soup.title.string)        #获取网页中的标题的内容
print(soup.li)
print(soup.a.string)
print("获取节点的名字:",soup.title.name)          #获取节点的名字
print(soup.li.attrs)            #获取li节点的所有属性
print(soup.p['name'])           #获取p节点name属性的值
print('______________________________________________')
print(soup.ul.contents)         #获取ul的直接子节点
print(soup.ul.children)         #获取ul的子孙节点
for i,child in enumerate(soup.ul.children):
    print(i,child)
print('______________________________________________')
'''
如果想获取某个节点的父亲节点,可以调用
parent属性
'''
print(soup.p.parent)

print('______________________________________________')

'''
如果想获取所有的祖先节点,可以调用parents属性

'''

print(type(soup.p.parents))             #返回结果是生成器类型,
print(list(enumerate(soup.p.parents)))  #用列表输出了它的索引和内容

print('______________________________________________')

'''
获取同级的节点即兄弟节点
next_sibling:获取下一个兄弟节点
previous_sibling:获取下一个兄弟节点
next_siblings:获取后面的所有兄弟节点
previous_sibling:获取前面的所有兄弟节点
'''
print(soup.p.next_sibling)
print(soup.p.previous_sibling)

print(list(enumerate(soup.p.next_siblings)))
print(list(enumerate(soup.p.previous_siblings)))   #用列表输出了它的索引和内容

print('______________________________________________')

'''
提取信息,前面选择好节点之后,
如果想要获取他们的一些信息,比如文本
属性等
'''

print(soup.li.next_sibling.string)              #提取第一个li节点的下一个节点的文本
print(list(soup.a.parents)[1])                  #soup.a.parents返回的是生成器类型,用list转为列表,然后下标取值
#print(list(soup.a.parents)[0].attrs['class'])  #取列表中第0个节点class属性的值
#print(list(soup.a.parents)[0]['class'])        #取列表中第0个节点class属性的值,也可以这么写
print(list(soup.a.parents)[1].attrs)            #取列表中第1个节点

'''
find_all()和find()方法,前者返回所有匹配的原色组成的列表
后者返回单个元素,也就是第一个元素
'''
print('#根据节点名来查询元素')
print(soup.find_all(name='li'))         #根据节点名来查询元素
print(type(soup.find_all(name='li')))
print('______________________________________________')
for li in soup.find_all(name='li'):
    print(li.find_all('a'))
    print(li.find_all('a')[0].string)
print('______________________________________________')

'''
传入属性来查询,传入的是attrs参数,参数的类型是
字典类型,得到结果为列表形式
'''
print(soup)
print(soup.find_all(attrs={'class':'item-0'}))      #获取class="item-0"的节点
print(soup.find_all(class_='item-0'))               #获取class="item-0"的节点,也可以这么写
print(soup.find_all(attrs={'name':'lgx'}))          #不是常用的属性,需要加上attrs

print('______________________________________________')

'''
text参数可用来匹配节点的文本,传入的形式可以是字符串,也可以正则表达式对象
compile方法可以将正则字符串编译成正则表达式对象,以便在后面的匹配中重复使用
'''

print(soup.find_all(text=re.compile('time')))       #text参数可用来匹配节点的文本

print('______________________________________________')
'''
ccs选择器,使用ccs选择器时,只需
调用select()方法,传入相应的ccs选择器即可
'''

html1='''
<div class="panel">
<div class="panel-heading">
<h4>hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jar</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
></ul>
</div>
</div>
'''
soup=BS(html1,"lxml")
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))             #选择ul节点下的所有li节点,结果是所有li节点的列表
print(soup.select('#list-2 .element'))
print(soup.select('ul')[0])
for ul in soup.select('ul'):
    print(ul.select('li'))

print('______________________________________________')

'''
获取属性,节点类型是Tag类型,所以获取属性
的方法还用原来的方法
'''
for ul in soup.select('ul'):
    print(ul['id'],ul.attrs['id'])

print('______________________________________________')
'''
获取文本,当然可以使用前面的string方法,也可以使用get_text()
'''
for li in soup.select('li'):
    print("string方法:",li.string)
    print("get_text():",li.get_text())







