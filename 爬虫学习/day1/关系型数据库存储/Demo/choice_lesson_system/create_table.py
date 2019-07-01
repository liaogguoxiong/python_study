'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: create_table.py
@time: 2019-06-27 14:47
@desc:
'''

import pymysql

def create_tab():

    db = pymysql.connect(host="192.168.1.126", user="root", password="123456", port=3307, db="student_system")
    cursor = db.cursor()
    sql = "create table if not exists users(id varchar(255) not null primary key ,password varchar(255) not null  )"
    cursor.execute(sql)
    cursor.execute("show tables")
    res = cursor.fetchall()
    print(res)
    db.close()

