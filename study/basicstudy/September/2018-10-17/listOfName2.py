#Program:还是讲列表的用法，之前讲的是浅复制，现在使用copy模块来进行深复制
#History:lgx    2018/10/17      Second revision

a=[1,2,3]
b=a
a.remove(1)
print(b)#搞不懂改了a列表，b列表也改变。可能这个也是浅复制,个人觉得应该a赋值给b列表,只是把地址给了b
print(a)


import copy
names=['zsy','lgx','wdy','feige',[1,2]]
names_cp=copy.copy(names)#其实相当于[列表].copy,是浅复制
print(names_cp)


#深复制，复制和之前列表完全一样的
# 不会因为列表的改变而改变
names_deepcp=copy.deepcopy(names)
print(names_deepcp)
names[-1][1]=8#修改原的列表
print("我是浅复制:",names_cp)#浅复制就相当于引用，引用原列表的内存地址，获得值
print("我是深复制:",names_deepcp)#深复制是重新开辟一片内存空间，故不受影响

#列表的循环

for i in names:
    print(i)

#列表的隔一个输出
print(names[::2])#::表示整个列表中的所有元素