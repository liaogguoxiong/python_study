#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 13:54
#!@Filename:get请求.py

'''
HTTP中最常见的的请求之一就是get请求,
首先构建一个简单的get请求,请求链接为
http://httpbin.org/get,该网站会判断如果
客户端发起的是GET,它返回相应的请求信息
'''

import requests
url='http://httpbin.org/get'
#######基本实例

r=requests.get(url)
#输出response的内容
print(type(r))
print(r.text)

#######基本实例

######添加参数

print("="*50)
data={

    'name':"lgx",
    'age':22
}
print('######添加参数')
r=requests.get(url,params=data)
print(r.text)
print(type(r.text))
######添加参数

print("="*50)

######response返回内容处理

'''
网页的返回类型实际上是str类型,但是它很特殊,是JSON格式的,
如果想直接解析返回结果,得到一个字典格式的话,可以直接调用json()方法
'''
print('######response返回内容处理')
r=requests.get(url)
print(type(r.text))
cont=r.json()
print(type(cont))
print(r.text)
print(cont['headers']['Host'])

######response返回内容处理


