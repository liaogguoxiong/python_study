#！/usr/bin/env python
#！@Author：lgx
#！@time：2019年5月22日 00:42:42
#!@Description: As the first vserion of output_data(mysql导出明细)
#               write many information about company ,so i want to
#               write those information in a file and call those when
#               use those

import pymysql
import csv.os

def get_data(ip,port,db_name):

    #连接数据库
    db=pymysql.connect(host=ip,user='root',password='A_ision#8888',port=port,db=db_name)
    #使用cursor()方法来获取mysql操作游标,利用游标来执行sql语句
    cursor=db.cursor()


