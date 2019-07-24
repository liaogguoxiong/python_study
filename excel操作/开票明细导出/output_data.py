'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: output_data.py
@time: 2019-07-19 12:22
@desc:
'''

import pymysql,os
from openpyxl import Workbook
from datetime import datetime
from dispose_input_file import *

#获取当前的年份
year = datetime.now().year
# 因为导数据是导上个月的,所以要减去1
month = datetime.now().month - 1
output_dir='D:/发票明细/{m}月发票明细/'.format(m=str(month))
username='root'
passwd='A_isino#888'

def data_from_mysql(c48_info,path=output_dir,user=username,password=passwd):

    global month
    ip=c48_info['ip']
    company_name=c48_info['company_name']
    shuihao=c48_info['shuihao']
    db_name=c48_info['dbname']
    port=int(c48_info['port'])
    tongcheng=c48_info['tongcheng']
    path=path+tongcheng

    # 如果当月是1月,需要导出12月份的数据
    if month == 0:
        month = 12
    #创建多重目录,如果目录不存在则创建,存在不报错
    os.makedirs(path,exist_ok=True)
    #获取excel对象
    wb = Workbook()
    #获取正在执行的exc
    ws = wb.active
    # 连接数据库
    db = pymysql.connect(user=user,password=password,host=ip,port=port, db=db_name,)
    # 使用cursor()方法来获取mysql操作游标,利用游标来执行sql语句
    cursor = db.cursor()
    sql=sql = '''SELECT A.kprq AS 开票日期,
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
        WHERE A.serial_num=B.serial_num AND nsrsbh='{shuihao}' AND kprq BETWEEN '{s_YEAR}-{s_MONTH}-01 00:00:00'AND'{e_YEAR}-{e_MONTH}-31 23:59:59' ORDER BY kprq
        '''.format(shuihao=shuihao,s_YEAR=year,s_MONTH=month,e_YEAR=year,e_MONTH=month)
    #print(sql)
    file_path=path+'/'+company_name+'.xlsx'
    if os.path.exists(file_path):
        print('%s的发票明细已经存在,路径为:[%s]'%(company_name,file_path))

    else:
        title = ['开票日期', '分机号', '发票代码', '发票号码', '开票类型', '原发票代码', '原发票号码', '发票行性质', '项目名称', '规格类型', '单位', '项目数量', '项目单价',
                 '项目金额',
                 '税率', '税额', '商品编码', '订单合计金额', '订单价税合计', '订单合计税额', '备注', '购货方名称', '购货方纳税人识别号', '购货方地址电话', '购货方银行账号',
                 '开票人',
                 '收款人', '复核人', '开票月份']
        ws.append(title,)
        n=0
        cursor.execute(sql)
        print('%s的发票明细条数为:%d'%(company_name,cursor.rowcount))  # 符合条件的数据条数
        while n < cursor.rowcount:  # 输出所有的数据
            n += 1
            row = cursor.fetchone()  # 执行sql语句的结果,是个列表
            str_date = row[0].strftime("%Y-%m-%d %H:%M:%S")  # 数据库获取的是时间戳
            # print(type(str_date))
            # print(str_date)
            ws.append(
                [str_date, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                 row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
                 row[23], row[24], row[25], row[26], row[27], row[28]])
            print("[%s]已经导出[%d]条" %(company_name,n))
        wb.save(file_path)
        print('%s导出完毕!,路径为%s' %(company_name,output_dir))
        db.close()












