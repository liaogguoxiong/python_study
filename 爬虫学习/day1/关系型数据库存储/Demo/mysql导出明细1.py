#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-28 10:06
#!@Filename:mysql导出明细1.py
import pymysql
import csv,os

def output_data(ip,db_name,port,shuihao,company_name):
    db = pymysql.connect(host=ip, user='root', password='A_isino#888', port=port, db=db_name)
    cursor = db.cursor()
    for i in shuihao:
        name=i
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
        WHERE A.serial_num=B.serial_num AND nsrsbh='{shuihao}' AND kprq BETWEEN '2019-02-01 00:00:00'AND'2019-02-28 23:59:59' ORDER BY kprq
        '''.format(shuihao=shuihao[name])
        if os.path.exists('C:/Users/xiao/Desktop/数据导出/{company_name}/开票明细/{filename}.csv'.format(company_name=company_name,filename=name)):
            print('%s已经存在'%name)
            continue
        #print(sql)
        #os.mkdir('C:/Users/xiao/Desktop/数据导出/{company_name}/开票明细'.format(company_name=company_name))
        f = open('C:/Users/xiao/Desktop/数据导出/{company_name}/开票明细/{filename}.csv'.format(company_name=company_name,filename=name), 'a', newline='', encoding='utf-8')
        writer = csv.writer(f)
        writer.writerow(
            ['开票日期', '分机号', '发票代码', '发票号码', '开票类型', '原发票代码', '原发票号码', '发票行性质', '项目名称', '规格类型', '单位', '项目数量', '项目单价', '项目金额',
             '税率', '税额', '商品编码', '订单合计金额', '订单价税合计', '订单合计税额', '备注', '购货方名称', '购货方纳税人识别号', '购货方地址电话', '购货方银行账号', '开票人',
             '收款人', '复核人', '开票月份'])
        try:
            n = 0
            cursor.execute(sql)
            print('Count:', cursor.rowcount)  # 符合条件的数据条数
            while n < cursor.rowcount:
                n += 1
                row = cursor.fetchone()
                str_date = row[0].strftime("%Y-%m-%d %H:%M:%S")
                # print(type(str_date))
                # print(str_date)
                writer.writerow(
                    [str_date, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                     row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
                     row[23], row[24], row[25], row[26], row[27], row[28]])

            print('%s导出完毕!'%name)
        except:
            db.rollback()
            print('发生错误')
        f.close()
def main():
    '''
    ip:192.168.20.54 端口为3306 数据库:dzfp_zzs_kpfw_arm
    '''
    guande={
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
        '深圳市宝安广安冠德石油贸易有限公司上南加油站': '91440300892472424C',
        '中山市古镇七坊加油站': '914420002820415980',
        '东莞市黄江东盛加油站有限公司': '914419000506533418'
    }
    output_data('192.168.20.54','dzfp_zzs_kpfw_arm',3306,guande,'冠德')



    '''
    ip:192.168.20.54 端口为3306 数据库:dzfp_zzs_kpfw_arm_sign

    '''
    guande1={
                '济南鉴德石油化工有限公司':'91370103787448537Q',
                '山东中惠泽石油有限公司':'91370103575478769F'
    }
    output_data('192.168.20.54','dzfp_zzs_kpfw_arm_sign',3306,guande1,'冠德')



    '''
        ip:192.168.20.54 端口为3306 数据库:dzfp_zzs_kpfw_arm_sign

    '''
    jieshun={
                '厦门市湖里华龙实业公司':'91350206155227568L',
                '厦门市阳光家园物业服务有限公司海沧分公司':'9135020030325215XA',
                '广州鼎通晟物业管理有限公司':'914401135721807990',
                '广州富利物业管理有限公司':'91440106683266317Q',
                '深圳音乐厅运营管理有限责任公司深圳音乐厅停车场':'91440300685354783N',
                '广州科建投资管理有限公司':'914401160784081960',
                '西安市享泰物业管理有限公司':'91610131668680296Q',
                '安徽八里河旅游开发有限公司':'91341226746788738Y',
                '深圳市新润园物业发展有限公司理想时代大厦停车场':'91440300MA5DA8U052'
    }
    output_data('192.168.20.54','dzfp_zzs_kpfw_arm_sign',3306,jieshun,'捷顺')


    # mysqlIP：192.168.20.54/端口3307/Schema：dzfp_zzs_kpfw_arm_drzb
    jieshun1={
                '成都新谷投资集团有限公司':'915101007280880172',
                '成都百扬嘉欣物业服务有限公司':'91510100556400560K'
    }
    output_data('192.168.20.54', 'dzfp_zzs_kpfw_arm_drzb', 3307, jieshun1, '捷顺')



    #   mysqlIP：192.168.20.181/端口3306/Schema：dzfp_zzs_kpfw_arm
    jieshun2={
            '深圳市福田农产品批发市场有限公司停车场':'9144030097935050XF'
    }
    output_data('192.168.20.181', 'dzfp_zzs_kpfw_arm', 3306, jieshun2, '捷顺')


    #   mysqlIP：192.168.20.54/端口3306/Schema：dzfp_zzs_kpfw_arm
    jieshun3={
        '陕西鑫华泰物业管理有限公司':'91610104MA6U2GBA1U',
        '深圳市华侨城物业服务有限公司武汉分公司':'91420100578252853T',
        '深圳市顺易通信息科技有限公司':'91440300664162117K'
    }
    output_data('192.168.20.54', 'dzfp_zzs_kpfw_arm', 3306, jieshun3, '捷顺')


    #   mysqlIP：192.168.20.40/端口3306/Schema：dzfp_zzs_kpfw_arm
    jieshun4={
        '深圳市信利康物业管理有限公司':'91440300MA5DG1PJ2G'
    }
    output_data('192.168.20.40', 'dzfp_zzs_kpfw_arm', 3306, jieshun4, '捷顺')


    # mysqlIP：192.168.20.54/端口3306/Schema：dzfp_zzs_kpfw_arm
    chuoqi={'绰琪服装（深圳）有限公司':'914403007966376128'}
    output_data('192.168.20.54','dzfp_zzs_kpfw_arm',3306,chuoqi,'绰琪')

    # mysqlIP：192.168.20.40/端口3306/Schema：dzfp_zzs_kpfw_arm
    huaqiaocheng={
                '深圳市华侨城物业服务有限公司':'914403001924025138'
    }
    output_data('192.168.20.40','dzfp_zzs_kpfw_arm',3306,huaqiaocheng,'华侨城')

    # 192.168.20.40/端口3306/Schema：dzfp_zzs_kpfw_arm
    fenqile={
        '深圳分期乐贸易有限公司':'91440300MA5DRNEM7D'
    }
    output_data('192.168.20.40','dzfp_zzs_kpfw_arm',3306,fenqile,'分期乐')


if __name__ == '__main__':
    main()