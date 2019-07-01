#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019年4月22日17:06:36
'''
导出冠德一年各个油站的发票明细，并总计数量
'''
import pymysql
import csv,os

def output_data(ip,db_name,port,shuihao):
    os.makedirs('C:/Users/lgx/Desktop/冠德一年开票明细和汇总/开票明细',exist_ok=True)
    # 连接数据库
    db = pymysql.connect(host=ip, user='root', password='A_isino#888', port=port, db=db_name)
    # 使用cursor()方法来获取mysql操作游标,利用游标来执行sql语句
    cursor = db.cursor()
    with open('C:/Users/lgx/Desktop/冠德一年开票明细和汇总/汇总.csv', 'a', newline='', encoding='utf-8-sig') as f:
        writer1 = csv.writer(f)
        writer1.writerow(['油站名称', '开票总量'])
    for i in shuihao:
        name = i
        # 传入税号
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
            WHERE A.serial_num=B.serial_num AND nsrsbh='{shuihao}' AND kprq BETWEEN '2018-04-01 00:00:00'AND'2019-03-31 23:59:59' ORDER BY kprq
            '''.format(shuihao=shuihao[name])
        with open('C:/Users/lgx/Desktop/冠德一年开票明细和汇总/开票明细/{youzhan}.csv'.format(youzhan=name),'a',newline='',encoding='utf-8-sig') as f:
            writer=csv.writer(f)
            writer.writerow(
                ['开票日期', '分机号', '发票代码', '发票号码', '开票类型', '原发票代码', '原发票号码', '发票行性质', '项目名称', '规格类型', '单位', '项目数量', '项目单价',
                 '项目金额',
                 '税率', '税额', '商品编码', '订单合计金额', '订单价税合计', '订单合计税额', '备注', '购货方名称', '购货方纳税人识别号', '购货方地址电话', '购货方银行账号',
                 '开票人',
                 '收款人', '复核人', '开票月份'])
            try:
                n=0
                cursor.execute(sql)
                print("开票量总数：",cursor.rowcount)
                while n < cursor.rowcount:
                    n +=1
                    row=cursor.fetchone()
                    str_date = row[0].strftime("%Y-%m-%d %H:%M:%S")  # 数据库获取的是时间戳
                    writer.writerow(
                    [str_date, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                     row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
                     row[23], row[24], row[25], row[26], row[27], row[28]])
                    num=cursor.rowcount
                print("%s导出完成"%name)
            except:
                db.rollback()
                print("发生错误！！！")
        with open('C:/Users/lgx/Desktop/冠德一年开票明细和汇总/汇总.csv','a',newline='',encoding='utf-8-sig') as f:
            writer1=csv.writer(f)
            writer1.writerow([name,num])
        print("%s发票总数已写入文件中"%name)


def main():
    '''
    ip:192.168.20.54 端口为3306 数据库:dzfp_zzs_kpfw_arm
    '''
    guande = {
        '广东广安冠德石化有限公司深圳分公司': '91440300319416657L',
        '深圳市顺归加油站有限公司': '91440300731109309T',
        '深圳市雄伟李氏经贸物资有限公司威程油气站': '91440300761978388R',
        '广东广安冠德石化有限公司惠州鸿业电力加油站': '91441302324755813B',
        '广东广安冠德石化有限公司乳源富诚加油站': '91440232398050621Q',
        '广东广安冠德石化有限公司四会市贞山加油站': '91441284093122815Y',
        '广东广安冠德石化有限公司金乐园加油站': '91440200MA4UH0YE5N',
        '四会市凯平加油站有限公司': '91441284MA4UN7452U',
        '广东广安冠德石化有限公司肇庆市四通北通加油站': '91441202345311533B',
        '广东广安冠德石化有限公司东莞塘厦林村加油站': '914419003042908790',
        '东莞市永安石油化工有限公司第二加油站': '914419007192624312',
        '台福油品（深圳）有限公司坪地加油站': '914403000638981370',
        '西安市长安区八一加油站': '91610116726273243X',
        '广东广安冠德石化有限公司珠海和平界冲加油站': '91440400MA4UWXMX67',
        '深圳市宝安广安冠德石油贸易有限公司上南加油站': '91440300892472424C'
    }
    output_data('192.168.20.54','dzfp_zzs_kpfw_arm',3306,guande)


if __name__ == '__main__':
    main()



