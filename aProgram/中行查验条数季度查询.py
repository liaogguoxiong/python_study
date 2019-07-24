'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 中行查验条数季度查询.py
@time: 2019-07-11 10:20
@desc:这个脚本用来查询中行每个季度(3个月)的查验量 去重 不去重
'''

import datetime
import pymysql
from  openpyxl import  Workbook




def select_sum_userful(months,year):

    db=pymysql.connect(host='192.168.20.170',user='root',password='Aisino123+',port=3306,db='boc')
    cursor=db.cursor()
    wb=Workbook()
    ws=wb.active
    title=['月份','查询数量']
    ws.append(title)

    for i in months:

        sql = '''SELECT DISTINCT ENTRY_ID FROM boc_entry WHERE submit_time>='{s_y}-{s_m}-01 00:00:00' AND submit_time<'{e_y}-{e_m}-01 00:00:00' ORDER BY ENTRY_ID;'''.format(s_y=year, s_m=i, e_y=year, e_m=i + 1)
        cursor.execute(sql)
        sum=cursor.rowcount
        ws.append([i,sum])
        print("%d月份去重的查验数量为:%d"%(i,sum))

    wb.save('去重的查询.xlsx')


def selct_sum(months,year):

    db = pymysql.connect(host='192.168.20.170', user='root', password='Aisino123+', port=3306, db='boc')
    cursor = db.cursor()
    #s实例化excel对象
    wb=Workbook()
    #获取当前正在操作的对象
    ws=wb.active
    #excel写入标题写标题
    title=['月份','查询数量']
    ws.append(title)
    for i in months:

        sql = '''SELECT COUNT(1)  FROM boc_entry WHERE submit_time>='{s_y}-{s_m}-01 00:00:00' AND submit_time< '{e_y}-{e_m}-01 00:00:00' '''.format(s_y=year, s_m=i, e_y=year, e_m=i + 1)
        cursor.execute(sql)
        res=cursor.fetchall()[0][0]
        ws.append([i,res])
        # print(res[0][0])
        print("%d月份不去重的查验数量为:%d"%(i, res))

    wb.save('总的查询.xlsx')


def main():

    # 执行的时候一般是季度月的下一个月,比如第一季度是123月,当时执行的月份应该是4月
    # 所以要减去1才是3月
    m_3 = datetime.datetime.now().month - 1
    m_2 = m_3 - 1
    m_1 = m_2 - 1
    months = [m_1, m_2, m_3]
    year=datetime.datetime.now().year
    selct_sum(months,year)
    select_sum_userful(months,year)





if __name__ == '__main__':

    main()







