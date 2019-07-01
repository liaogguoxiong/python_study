'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 初始化数据库.py
@time: 2019-06-23 22:55
@desc:
'''

import pymysql

#连接数据库数据库
db=pymysql.connect(host="192.168.1.126",user="root",password="123456",port=3307)
#获取数据库的游标,但是上面的数据连接并没有选择数据库
cursor=db.cursor()


#利用游标来执行sql语句,执行查询数据库版本的sql语句
cursor.execute('SELECT VERSION()')
print("查询成功")
res=cursor.fetchall()
print("数据库的版本是:",res[0][0])
#进入数据库查询所有数据库的命令是show databases
cursor.execute("show databases")
res1=cursor.fetchall()
print("所有的数据库:",res1)

