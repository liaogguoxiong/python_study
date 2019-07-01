'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 创建表.py
@time: 2019-06-24 15:02
@desc:
'''

import pymysql

db=pymysql.connect(host="192.168.1.126",user="root",password="123456",port=3307,db="test")
cursor=db.cursor()
sql="create table if not exists students(id varchar(255) not null primary key ,name varchar(255) not null ,age int not null ,sex char not null )"
cursor.execute(sql)
cursor.execute("show tables")
res=cursor.fetchall()
print(res)
db.close()