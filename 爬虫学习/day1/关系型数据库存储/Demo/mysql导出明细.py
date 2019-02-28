#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-27 15:45
#!@Filename:mysql导出明细.py

import csv

import pymysql

f=open('1.csv','a',newline='',encoding='utf-8')
writer=csv.writer(f)
writer.writerow(
        ['开票日期', '分机号', '发票代码', '发票号码', '开票类型', '原发票代码', '原发票号码', '发票行性质', '项目名称', '规格类型', '单位', '项目数量', '项目单价', '项目金额',
         '税率', '税额', '商品编码', '订单合计金额', '订单价税合计', '订单合计税额', '备注', '购货方名称', '购货方纳税人识别号', '购货方地址电话', '购货方银行账号', '开票人',
         '收款人', '复核人', '开票月份'])
db=pymysql.connect(host='192.168.20.54',user='root',password='A_isino#888',port=3306,db='dzfp_zzs_kpfw_arm')
cursor=db.cursor()
sql='''SELECT A.kprq AS 开票日期,
A.cardno AS 分机号,
A.fpdm AS 发票代码,
A.fphm AS 发票号码,
A.kplx AS 开票类型,
A.yfpdm AS 原发票代码,
A.yfphm AS 原发票号码,
B.FPHXZ AS 发票行性质,
B.XMMC AS 项目名称,
B.GGXH AS 规格型号,
B.DW AS 单位,
B.XMSL AS 项目数量,
B.XMDJ AS 项目单价,
B.XMJE AS 项目金额,
B.SL AS 税率,
B.SE AS 税额,
B.SPBM AS 商品编码,
A.dd_hjje AS 订单合计金额,
A.dd_jshj AS 订单价税合计,
A.dd_hjse AS 订单合计税额,
A.bz AS 备注,
A.ghf_nsrmc AS 购货方名称,
A.ghf_nsrsbh AS 购货方纳税人识别号,
A.ghf_dzdh AS 购货方地址电话,
A.ghf_yhzh AS 购货方银行账号,
A.kpr AS 开票人,
A.skr AS 收款人,
A.fhr AS 复核人,
DATE_FORMAT(kprq,'%Y%m') AS 开票月份 
FROM invoice_info A,invoice_info_mx B 
WHERE A.serial_num=B.serial_num AND nsrsbh='91441302324755813B' AND kprq BETWEEN '2019-02-01 00:00:00'AND'2019-02-28 23:59:59' ORDER BY kprq
'''

try:
    n=0
    cursor.execute(sql)
    print('Count:', cursor.rowcount)  # 符合条件的数据条数
    while n < cursor.rowcount:
        n +=1
        row = cursor.fetchone()
        str_date=row[0].strftime("%Y-%m-%d %H:%M:%S")
        # print(type(str_date))
        # print(str_date)
        writer.writerow([str_date,row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16],row[17],row[18],row[19],row[20],row[21],row[22],row[23],row[24],row[25],row[26],row[27],row[28]])
        print(row)
except:
    db.rollback()
    print('发生错误')
f.close()