#Program：创建一个列表，对它进行增删差改的操作
#History：Lgx    2018-10-16  First release
names=['zsy','lgx','wdy','feige']
print(names)

'''#下面进行查操作
print(names)#查询整个列表
print(names[0])#查询列表第一个数
print(names[-1])#查询列表倒数第一个数
#想查询下表从0到3的数据，最后一个下标为3，
# 应该可以全部查出，但是顾头不顾尾，所以不包括下标为3的数
print(names[:4])
print(names[-4:])

下面进行增操作

#1.是加在列表的最后面
names.append("huanghua")
print(names)
#2.随便加在列表的一个位置
names.insert(0,'huanghua')
print(names)
names.insert(6,'wudishi')
print(names)

下面是进行删除操作

#第一种：remove
names.remove('wudishi')
print(names)
#第二种：pop
names.pop(0)
print(names)
#第三章：del 列表名[下标]
del names[4]
print(names)

下面进行改操作

names[2]="wyl"
print(names)
'''
#copy方法的使用
names_copy=names.copy()#复制name列表
print(names_copy)
names[3]="mengguofei"#修改names下标为3点元素，names2的没变
print(names)
print(names_copy)
names.insert(2,["lgx","lxy"])#增加一个子子列表
names_copy=names.copy()#再次复制
print(names)
print(names_copy)
names[2][0]="LGX"
#修改列表中的元素，二个列表都改变，究其原因
#是copy列表的时候，names2复制的是子列表的内存地址，
#所以当names改成列表中的元素，但是地址没变，所以name2应该是和names一样才对
print(names)
print(names_copy)