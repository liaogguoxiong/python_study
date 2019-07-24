'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: test.py
@time: 2019-07-02 14:16
@desc:
'''
import datetime
shuihao={'name':'廖国雄'}
year=datetime.datetime.now().year
month=datetime.datetime.now().month-1
print(year,month)
sql = '''SELECT A.kprq AS 开票日期,
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
        WHERE A.serial_num=B.serial_num AND nsrsbh='{shuihao}' AND kprq BETWEEN '{S_YEAR}-{S_MONTH}-01 00:00:00'AND'{E_YEAR}-{E_MONTH}-31 23:59:59' ORDER BY kprq
        '''.format(shuihao=shuihao['name'],S_YEAR=year,S_MONTH=month,E_YEAR=year,E_MONTH=month)
print(sql)
