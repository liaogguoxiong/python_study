#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-26 16:57
#!@Filename:login_students.py\
'''
做一个简单的学生登录
1.[登录,注册]
2.[如果密码输错超过三次,将被锁死,需要24小时才能够解锁]
'''
import pymysql

class MYSQL():

    def __init__(self,db_name):

        self.database_name=db_name

    def create_db(self):

        db=pymysql.connect(host='localhost',user='root',password='li@o0121',port=3306)
        cursor=db.cursor()
        sql='create database {db_name} default character set utf8'.format(db_name=self.database_name)
        try:
            cursor.execute(sql)
            print('创建%s数据库成功'%(self.database_name))
        except:
            db.rollback()
            print('创建数据库%s失败'%(self.database_name))
        db.close()
    def create_table(self,table_name):
        '''
        创建表,需要传入数据库和创建的表
        :return:
        '''
        db = pymysql.connect(host='localhost', user='root', password='li@o0121', port=3306,db=self.database_name)
        cursor=db.cursor()
        sql = 'create table if not exists {table_name}(username varchar(255) primary key ,password varchar(255) not null )'.format(table_name=table_name)
        try:
            cursor.execute(sql)
            print('创建%s数据表成功' % (table_name))
        except:
            db.rollback()
            print('创建数据表%s失败' % (table_name))
        db.close()



    def find_user(self,sql):
        db = pymysql.connect(host='localhost', user='root', password='li@o0121', port=3306,db=self.database_name)
        cursor=db.cursor()
        try:
            cursor.execute(sql)
            res=cursor.fetchall()
            return res
        except:
            db.rollback()
            print("查找失败")
        db.close()


    def add_user(self,sql):
        '''
        插入新的用户信息,需要传的参数有
        数据库,表名,插入的sql语句
        :param sql:
        :return:
        '''
        db = pymysql.connect(host='localhost', user='root', password='li@o0121', port=3306, db=self.database_name)
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            print('添加数据成功')
        except:
            db.rollback()
            print('添加数据失败')
        db.close()


class SUBJRCT_SYSTEM():

    def login(self):
        lock_user = []
        account={}
        uname=input('请输入您的用户名>>:')
        passwd=input('请输入您的密码>>:')
        print("输入的账号和密码:",uname,passwd)
        db=MYSQL('subject_system')
        locked_data=db.find_user('select * from locked_user')
        print("锁定用户表:",locked_data)
        for r in locked_data:
            print(r[0])
            lock_user.append(r[0])
        if uname in lock_user:
            print("帐号%s已经被锁定了!!!请明天再试"%uname)
            exit()
        account_data=db.find_user('select * from student_account')
        print('用户表:',account_data)
        for a in account_data:
            keys=a[0]
            print(keys)
            values=a[1]
            account.update({keys:values})
        print(account)
        if uname not in account:
            print('帐号错误或者帐号不存在')
            exit()
        if passwd==account[uname]:
            print('欢迎进入%s用户选课系统'%(uname))

    def enroll(self):
        '''
        用户注册
        :return:
        '''
        account={}
        print('===============注册=================')
        uname = input('请输入您的用户名>>:')
        passwd = input('请输入您的密码>>:')
        print("注册的账号和密码:",uname,passwd)
        db = MYSQL('subject_system')
        account_data = db.find_user('select * from student_account')
        print('用户表:', account_data)
        for a in account_data:
            keys=a[0]
            # print(keys)
            values=a[1]
            account.update({keys:values})
        print(account)
        if uname in account:
            print('%s已经存在,不能重复注册'%(uname))
            exit()
        db.add_user('insert into student_account(username,password) values("{uname}","{passwd}")'.format(uname=uname,passwd=passwd))



def main():
    suj_sys=SUBJRCT_SYSTEM()
    index_page='''
    
        1:登录
        2:注册
        3:退出
               '''
    print(index_page)
    choice=input('请输入您的选择>>:')
    if choice == '1':
        suj_sys.login()
    elif choice == '2':
        suj_sys.enroll()
    elif choice == '3':
        exit()
    else:
        print('无效的选择!!!!')


if __name__ == '__main__':

    main()
