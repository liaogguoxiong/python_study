#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-22 12:03
#!@Filename:MySql存储.py

'''
主要介绍python下mysql的存储
'''
import pymysql

db=pymysql.connect(host='localhost',user='root',password='li@o0121',port=3306)  #连接数据库
# cursor=db.cursor()      #使用cursor()方法来获取mysql操作游标,利用游标来执行sql语句
# cursor.execute('SELECT VERSION()')              #执行mysql语句
# data=cursor.fetchone()                          #使用fetchone方法获取第一条数据
# print('Database version',data)
# cursor.execute('create database spiders default  character set utf8')          #创建spiders数据库
# db.close()

'''
创建表,也可以直接创建
'''

# db=pymysql.connect(host='localhost',user='root',password='li@o0121',port=3306,db='spiders')
# cursor=db.cursor()
#创建数据库的sql语句
# sql='create table if not exists students(id varchar(255) not null,name varchar(255) not null,age int not null,primary key(id))'
# cursor.execute(sql)               #创建表
# db.close()

'''
插入数据
增删查改操作的标准写法,查找不需要提交
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback
'''


db=pymysql.connect(host='localhost',user='root',password='li@o0121',port=3306,db='spiders')
# id='0001'
# name='lgx'
# age=22
# cursor=db.cursor()
# sql='insert into students(id,name,age) values(%s,%s,%s)'
# try:
#     cursor.execute(sql,(id,name,age))
#     db.commit()
#     print('数据插入成功')
# except:
#     db.rollback()                   #数据异常处理,调用rollback()方法,执行数据回滚,相当于什么事情都没有发生过
# data=cursor.execute('select * from students')
# print(data)
# db.close()

# '''
# # 插入数据的通用方法
# # '''
# # data={
# #     'id':'0002',
# #     'name':'zsy',
# #     'age':'21'
# #
# # }
# # table='students'
# # keys=','.join(data.keys())              #连接字符,用','分割
# # values=','.join(['%s']*len(data))       #插入的字段有多少个,就拼接多少个%s当作占位符
# # cursor=db.cursor()
# # sql='insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)
# # try:
# #     cursor.execute(sql,tuple(data.values()))
# #     print('sucessful')
# #     db.commit()
# # except:
# #     print('failed')
# #     db.rollback()
# # db.close()


# '''
# 抓取数据的时候,在意的是数据重复的问题,
# 如果存在数据重复,我们希望是更新数据,而不是
# 重复保存一次,动态构造sql可以实现去重,如果
# 数据重复,则更新数据,如果不存在则插入数据
# '''
# cursor=db.cursor()
# data={
#      'id':'0003',
#     'name':'廖国雄',
#     'age':'22'
# }
# table='students'
# keys=', '.join(data.keys())
# print(keys)
# values=', '.join(['%s']*len(data))
# print(values)
# # on duplicate key update这行代码的意思是如果主键(id)已经存在,就更新数据,而不是插入数据.如果不存在,才插入数据
# sql='insert into {table}({keys}) values({values}) on duplicate key update'.format(table=table,keys=keys,values=values)
# print(sql)
# update=','.join(["{key}=%s".format(key=key) for key in data])
# print(update)
# sql += ' '+update
# print(sql)
# try:
#     if cursor.execute(sql,tuple(data.values())*2):
#         print('Successful')
#         db.commit()
# except:
#     print('Failed')
#     db.rollback()
# db.close()


# '''
# 删除数据
#
# '''
# cursor=db.cursor()
# table='students'
# condition='name="lgx"'
# sql='delete from {table} where {condition}'.format(table=table,condition=condition)
# print(sql)
# try:
#     cursor.execute(sql)
#     print('删除成功')
#     db.commit()
# except:
#     print('发生错误')
#     db.rollback()
#db.close()

'''
查询数据不会对数据库造成改变,所以不用
db.commit()
fetchone()获取结果的第一条数据
fetchall()获取结果的全部数据
查询数据的时候通过偏移指针来完成的,
使用fetchone()指针偏移一条数据,再使用
fetchall()就从第2条开始了 
'''

cursor=db.cursor()
table='students'
contidion='age > 20'
sql='select * from {table} where {contidion}'.format(table=table,contidion=contidion)
# print(sql)
# try:
#     cursor.execute(sql)
#     print(cursor.rowcount)
#     #print(cursor.fetchone())
#     result=cursor.fetchall()
#     print(result)
#     print("查找成功")
#     print('====指针的偏移')
#     print(cursor.fetchall())
# except:
#     db.rollback()
#     print("查找失败,执行回滚操作")
# db.close()
# username=[]
# for res in result:
#     print(res[1])
#     username.append(res[1])
# if 'zsy' in username:
#     print('zsy is in tuple')
# else:
#     print('no exist')

'''
fetchall()一次性把所有的数据读取出来,如果数据
过大的话,占用的开销很多,可以使用while循环家fetchone()
来获取数据
'''
try:
    cursor.execute(sql)
    print('Count:',cursor.rowcount)    #符合条件的数据条数
    row=cursor.fetchone()

    while row:
        print('Row:',row)
        row=cursor.fetchone()

except:
    print('Error')


