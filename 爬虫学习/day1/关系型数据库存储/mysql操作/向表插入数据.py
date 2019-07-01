'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 向表插入数据.py
@time: 2019-06-24 15:31
@desc:
'''

import pymysql

'''
插入数据
增删查改操作的标准写法,查找不需要提交
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback
'''


db=pymysql.connect(host="192.168.1.126",user="root",password="123456",port=3307,db="test")
cursor=db.cursor()
# sql="insert into students(id,name,age,sex) values('1400360117','廖国雄',22,'男')"

#上面的是比较麻烦的sql写法,介绍个比较通用的方法

data={
    'id':'2',
    'name':'aaa',
    'age':22,
    'sex':'男'
}

table='students'

keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values)


try:
    cursor.execute(sql,tuple(data.values()))
    #执行sql语句之后一定要提交,不然没有插入数据库中
    db.commit()
    print("数据添加成功")
    cursor.execute("select * from students")
    res=cursor.fetchall()
    print(res)

except:
    db.rollback()
    print("插入出错")

db.close()