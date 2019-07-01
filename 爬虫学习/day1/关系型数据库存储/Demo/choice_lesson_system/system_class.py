'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: system_class.py
@time: 2019-06-27 13:56
@desc:选课系统的类以及各种方法
'''

import pymysql

def db_action(sql):

    db = pymysql.connect(host="192.168.1.126", user="root", password="123456", port=3307, db="student_system")
    cursor = db.cursor()
    cursor.execute(sql)
    res=cursor.fetchall()
    db.close()
    return res


def check_true(tuple,value):

    for i in tuple:
        if value in i:
            return 0
        else:
            # print("用户不存在")
            return 1




class SYSTEM_STUDENT():

    def __init__(self):

        pass

    def sign_in(self,user,passwd):

        sql='select id from users'
        res=db_action(sql)
        if check_true(res,user) == 0:
            sql1='select password from users'
            res1=db_action(sql1)
            if check_true(res1,passwd)==0:
                print("进入选课界面")
            else:
                print("密码不对")
        else:
            print("用户名错误或不存在")












