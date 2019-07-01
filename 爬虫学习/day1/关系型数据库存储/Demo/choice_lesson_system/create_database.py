'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: create_database.py
@time: 2019-06-27 14:05
@desc: 创建数据库
'''

import pymysql

def show_databases(db_name):

    db = pymysql.connect(host="192.168.1.126", user="root", password="123456", port=3307)
    cursor = db.cursor()
    cursor.execute('show databases')
    res = cursor.fetchall()

    for i in res:
        if i[0] == db_name:
            return 0
            db.close()
            exit()




def create_db():

    db=pymysql.connect(host="192.168.1.126",user="root",password="123456",port=3307)
    cursor=db.cursor()
    db_name="student_system"

    if show_databases(db_name) == 0:
        print('数据库已经存在')
    else:
        sql = 'create database {db_name} character set gbk'.format(db_name=db_name)
        cursor.execute(sql)
        cursor.execute('show databases')

        if show_databases(db_name) == 0:
            print("%s数据库已经成功建立"%(db_name))

    db.close()




