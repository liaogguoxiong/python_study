#时间：    2018/11/5 22:23
#作者：    lgx
#文件名：  BuiltInFunctions

#今天来学习内置函数


print(all([-1,5,3,0]))#如果括号里面的为真，则返回True，非0为真
print("="*50)
print(any([]))#如果括号中的元素有一个为真，则返回True，空返回False
print("="*50)
print(bin(254))#十进制转二进制
print("="*50)
print(callable(print))#如果括号内的元素能够被调用，则返回True，即后面能加括号
print("="*50)
print(chr(97))#返回数字对应的ASCII码
print("="*50)
print(ord('a'))#返回ASCII码对应的数字
print("="*50)
print(divmod(10,3))#二个数相除，返回商和余数
print("="*50)
res=filter(lambda n:n < 5,range(10))#筛选出符合条件的元素，用for循环输出
for i in res:
    print(i)
print("="*50)
res1=map(lambda n:n*2,range(10))#相当于[i*2 for i in range(10)]
for i in res1:
    print(i)
print("================")
import functools
res2=functools.reduce(lambda x,y:x+y,range(10))#累加
print(res2)
res3=functools.reduce(lambda x,y:x*y,range(1,10))#累乘
print(res3)
print(hex(15))#把数字转化为16进制
