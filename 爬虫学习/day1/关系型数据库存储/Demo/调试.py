# #！/usr/bin/env python
# #！@Author：lgx
# #！@时间：2019-02-27 11:35
# #!@Filename:调试.py
# import pymysql
#
# db=pymysql.connect(host='localhost',user='root',password='li@o0121',port=3306,db='spiders')
# cursor=db.cursor()
# cursor.execute('select id from students ')
# res=cursor.fetchall()
# print(res)
# for r in res:
#     print(r[0])
#     print(type(r[0]))
#
# data={'a':'2'}
# data.update(b=2)
# print(data)
# if 'a' not in data:
#     print('不在')
# else:
#     print('在')
#
# a=()
#
# if 'a'  in a:
#     print('在')
# else:
#     print('不在')

# import csv
#
# with open('a.csv','w',newline='',encoding='utf-8') as f:
#     writer=csv.writer(f)
#     writer.writerow(
#         ['开票日期', '分机号', '发票代码', '发票号码', '开票类型', '原发票代码', '原发票号码', '发票行性质', '项目名称', '规格类型', '单位', '项目数量', '项目单价', '项目金额',
#          '税率', '税额', '商品编码', '订单合计金额', '订单价税合计', '订单合计税额', '备注', '购货方名称', '购货方纳税人识别号', '购货方地址电话', '购货方银行账号', '开票人',
#          '收款人', '复核人', '开票月份'])
# keys=''
# for i in range(26):
#     key="row[%d]"%(i)
#
#     keys +=key+','
#     print(keys)
import os

# guande={'广东广安冠德石化有限公司珠海和平界冲加油站':'91440400MA4UWXMX67'}
# for i in guande:
#     name=i
#     print(name)
#     os.mkdir('C:/Users/xiao/Desktop/数据导出/{dicname}'.format(dicname=name))
#     with open('C:/Users/xiao/Desktop/数据导出/{dicname}/{shuihao}.csv'.format(dicname=name,shuihao=name),'a',encoding='utf-8') as f:
#         f.write("this is a test")

os.mkdir('C:/Users/xiao/Desktop/数据导出/冠德')
