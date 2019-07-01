#今天来学习函数
import time
"""
def test1(x):
    "print a num that you input"
    print(x)
num=input("please input a num,and print it:")
test1(num)
"""
def log():
    time_format="%Y-%m-%d %X"#时间格式,%X指时分秒
    time_current=time.strftime(time_format)#获取当前时间
    with open('a.txt','a') as f:#模式为a+即追加写模式，就可以不断地写入，如果为w模式则会覆盖
        f.write('%s: end action\n' %time_current)


def test1():
    print("in the test1")
    log()


def test2():
    print("in the test2")
    log()
    return 0
def test3():
    print("in the test3")
    log()
    return 1,"hello",[1,2],{"name":"lgx"}
x=test1()
y=test2()
z=test3()
print("不带参数的函数".center(50,'#'))
print(x)
print(y)
print(z)

#有参数的函数

def test_arg(x,y):
    print(x)
    print(y)
print("带参数的函数".center(50,'#'))
test_arg(1,2)#与形参一一对应
test_arg(y=2,x=1)#可以不与形参一一对应
#test_arg(1,x=1)#因为一一对应，第一个传入的参数为x，就相当于x的参数传入了2个，没有一一对应

#默认参数,特点：调用函数的时候，默认参数非必需传
#用途：1.默认安装值 2.

def test_default(x,y=2):#y为默认
    print(x)
    print(y)

#参数组，当传入的参数不确定时候，不用写形参，使用参数组,只接受位置参数
print("参数组".center(50,'#'))
def test_argrp(*args):
    print(args)

test_argrp(1,2,3,4,5,67,8,0)
test_argrp(*[1,2,3,4,5,12,3,4,5])

#形参为字典的时候,**kwargs,把N个关键字参数，转化为字典的方式，接受关键字参数

def test_dic(**kwargs):
    print(kwargs)
print("参数为字典的函数".center(50,'#'))
test_dic(name='lgx',age=22)
test_dic(**{'name':"lgx",'age':22})

#各种模式形参混合,位置形参不能够放在关键字形参前面
def test_mix(name,age=18,*args,**kwargs):

    print(name)
    print(age)
    print(args)
    print(kwargs)
print("多重模式形参混合".center(50,'#'))
test_mix("lgx",22,1,1,2,3,1,name1='lgx',sex="m",age1='22')
