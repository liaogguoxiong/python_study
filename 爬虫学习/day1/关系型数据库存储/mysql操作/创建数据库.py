'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 创建数据库.py
@time: 2019-06-23 23:18
@desc:
'''

import pymysql

#连接数据库
db=pymysql.connect(host="192.168.1.126",user="root",password="123456",port=3307)
#获取数据库游标
cursor=db.cursor()
sql="create database test character set gbk"
#执行创建数据库sql语句
cursor.execute(sql)
cursor.execute("show databases")
res=cursor.fetchall()
print(res)
db.close()