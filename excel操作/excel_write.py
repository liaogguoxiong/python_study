'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: excel_write.py
@time: 2019-07-01 10:45
@desc:
'''
import pymysql,os
from openpyxl import Workbook
import datetime

def output_data(ip,db_name,port,shuihao,company_name):

    year=datetime.datetime.now().year
    #因为导数据是导上个月的,所以要减去1
    month=datetime.datetime.now().month-1
    if month == 0:
        month=12
    wb = Workbook()
    ws = wb.active
    #创建多重目录,如果目录不存在则创建,存在不报错
    os.makedirs('C:/Users/lgx/Desktop/数据导出/{company_name}/开票明细'.format(company_name=company_name),exist_ok=True)
    #连接数据库
    db = pymysql.connect(host=ip, user='root', password='A_isino#888', port=port, db=db_name)
    #使用cursor()方法来获取mysql操作游标,利用游标来执行sql语句
    cursor = db.cursor()
    for i in shuihao:
        name=i
        #传入税号
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
        WHERE A.serial_num=B.serial_num AND nsrsbh='{shuihao}' AND kprq BETWEEN '{s_YEAR}-{s_MONTH}-01 00:00:00'AND'{e_YEAR}-{e_MONTH}-31 23:59:59' ORDER BY kprq
        '''.format(shuihao=shuihao[name],s_YEAR=year,s_MONTH=month,e_YEAR=year,e_MONTH=month)
        #如果某个税号已经导出过了,不会再导出
        if os.path.exists('C:/Users/lgx/Desktop/数据导出/{company_name}/开票明细/{filename}.xlsx'.format(company_name=company_name,filename=name)):
            print('%s已经存在'%name)
            continue
        #print(sql)
        title=['开票日期', '分机号', '发票代码', '发票号码', '开票类型', '原发票代码', '原发票号码', '发票行性质', '项目名称', '规格类型', '单位', '项目数量', '项目单价', '项目金额',
             '税率', '税额', '商品编码', '订单合计金额', '订单价税合计', '订单合计税额', '备注', '购货方名称', '购货方纳税人识别号', '购货方地址电话', '购货方银行账号', '开票人',
             '收款人', '复核人', '开票月份']
        ws.append(title)

        try:
            n = 0
            cursor.execute(sql)
            print('Count:', cursor.rowcount)  # 符合条件的数据条数
            while n < cursor.rowcount:        #输出所有的数据
                n += 1
                row = cursor.fetchone()      #执行sql语句的结果,是个列表
                str_date = row[0].strftime("%Y-%m-%d %H:%M:%S") #数据库获取的是时间戳
                # print(type(str_date))
                # print(str_date)
                ws.append(
                    [str_date, row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                     row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22],
                     row[23], row[24], row[25], row[26], row[27], row[28]])
                print("已经导入",n)
            wb.save('C:/Users/lgx/Desktop/数据导出/{company_name}/开票明细/{filename}.xlsx'.format(company_name=company_name,filename=name))
            print('%s导出完毕!'%name)
        except:
            db.rollback()
            print('发生错误')




def main():
    '''
       ip:192.168.20.54 端口为3306 数据库:dzfp_zzs_kpfw_arm
       '''


    huarun={'华润网络（深圳）有限公司':'91440300MA5DK1T202'}

    output_data('192.168.20.54', 'dzfp_zzs_kpfw_arm', 3306, huarun, '华润')




    '''
    ip:192.168.20.54 端口为3306 数据库:dzfp_zzs_kpfw_arm_sign

    '''
    guande1={
                '济南鉴德石油化工有限公司':'91370103787448537Q',
                '山东中惠泽石油有限公司':'91370103575478769F'

    }
    output_data('192.168.20.54','dzfp_zzs_kpfw_arm_sign',3306,guande1,'冠德')

    zhongwaiyun={

        '广东中外运报关有限公司黄埔分公司': '914401123047015781'
    }

    output_data('192.168.20.54','dzfp_zzs_kpfw_arm_sign',3306,zhongwaiyun,'中外运')

    wendemu={
        '深圳市昌盛投资发展有限公司温德姆至尊酒店': '9144030030628267XA'
    }

    output_data('192.168.20.54', 'dzfp_zzs_kpfw_arm_sign', 3306, wendemu, '温德姆')


    '''
    ip:192.168.20.193   端口:3306 数据库:dzfp_zzs_kpfw_arm
    '''

    jieshun6={
        '深圳桑达物业发展有限公司':'91440300192221050R',
        '深圳市东华物业管理有限公司':'914403001922278073',
        '太原市君威物业管理有限公司':'91140100060729485D',
        '太原市玉龙物业管理有限公司':'91140100060736757K',
        '南京新丽华投资发展有限公司':'913201050579905942',
        '深圳市赛格物业管理有限公司赛格工业园停车场':'91440300MA5ENFWQ16',
        '厦门市融坤房地产开发有限公司':'913502006123137294',
        '深圳天安智慧园区运营有限公司龙岗分公司':'91440300665881965G',
        '武汉中商鹏程销品茂管理有限公司':'91420100731088034Y',
        '深圳市润丰不动产运营服务有限公司':'91440300088288060K',
        '太原市石林物业发展有限公司长风街分公司':'91140105068025722R',
        '湖南华天物业管理有限责任公司':'914300007170519726'
    }
    output_data('192.168.20.193','dzfp_zzs_kpfw_arm',3306,jieshun6,'捷顺')

    guande2={
        '成都鸿浩加气站有限公司':'915101325535515157'
    }
    output_data('192.168.20.193','dzfp_zzs_kpfw_arm',3306,guande2,'冠德')

    jieshun5={
        '广东省机场管理集团有限公司惠州机场公司': '91441300579725878W',
        '深圳巴士集团股份有限公司公交大厦停车场': '91440300760469493D'
    }

    output_data('192.168.20.193', 'dzfp_zzs_kpfw_arm', 3306, jieshun5, '捷顺')

    rencai={
        '深圳市人才集团有限公司': '914403006925252451',
        '深圳市人才服务中心（深圳市人才大市场）': '12440300564206418J'
    }

    output_data('192.168.20.193', 'dzfp_zzs_kpfw_arm', 3306, rencai, '人才市场')


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
                '深圳市新润园物业发展有限公司理想时代大厦停车场':'91440300MA5DA8U052',
                '南京江城物业管理有限公司':'91320114MA1Q20XP8A'
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
    #   mysqlIP：192.168.20.40/端口3306/Schema：dzfp_zzs_kpfw_arm
    jieshun4={
        '深圳市信利康物业管理有限公司':'91440300MA5DG1PJ2G',
        '天津盛信商业管理有限公司':'911201046661165952',
        '汇隆置业（杭州）有限公司':'913301000609543240',
        '同泰电子实业（深圳）有限公司同泰总部产业园停车场':'91440300MA5EYXLP2X'


    }
    output_data('192.168.20.40', 'dzfp_zzs_kpfw_arm', 3306, jieshun4, '捷顺')

    tianyin={
        '天音通信有限公司': '91440300279293591L'
    }

    output_data('192.168.20.40', 'dzfp_zzs_kpfw_arm', 3306, tianyin, '天音')



    # mysqlIP：192.168.20.54/端口3306/Schema：dzfp_zzs_kpfw_arm
    chuoqi={'绰琪服装（深圳）有限公司':'914403007966376128'
            }
    output_data('192.168.20.54','dzfp_zzs_kpfw_arm',3306,chuoqi,'绰琪')

    fangdichang={
        '深圳市房地产中介协会': '51440300671855317J'
    }
    output_data('192.168.20.54', 'dzfp_zzs_kpfw_arm', 3306, fangdichang, '房地产')

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

    #mysqlIP:192.168.20.173/端口:3306/数据库:dzfp_zzs_kpfw_arm
    huaqiaocheng={
        '北京华侨城物业服务有限公司':'91110105761426081E'
    }
    output_data('192.168.20.173','dzfp_zzs_kpfw_arm',3306,huaqiaocheng,'华侨城')

    #mysqlIP:192.168.20.197/端口:3306/数据库:dzfp_zzs_kpfw_arm

    jieshun7={
        '深圳市赛格康乐企业发展有限公司':'91440300192182944B',
        '南京兴智科技产业发展有限公司':'913201925894178441'
    }
    output_data('192.168.20.197','dzfp_zzs_kpfw_arm',3306,jieshun7,'捷顺')

    # dbname:dzfp_zzs_kpfw_arm   port:3306  ip:192.168.20.212
    jieshun8={
'深圳市汉京物业服务有限公司汉京大厦地下停车场':'91440300568513650N',
'北京雅宏停车服务有限公司':'91110105556872453J',
'广州市保丰物业管理有限公司':'91440104668141049Q',
'厦门市建坤诚兴物业有限公司':'913502002601487225',
'中航物业管理有限公司龙岗区人民医院停车场':'91440300MA5F73XD2B',
'烟台国际机场集团有限公司航空实业分公司':'91370600796173950H',
'山西万家物业管理有限公司':'911401005759783843',
'山西日报传媒（集团）物业管理有限责任公司':'91140106317172126P',
'厦门天润星辰物业管理有限公司':'91350200MA32F50P4X',
'厦门市成功大酒店有限公司':'91350200581295248D',
'广东顺德佳德业置业投资有限公司':'91440606061478243A',
'上海福克斯资产管理有限公司':'91310112051203908L',
'上海焦点实业有限公司':'91310112687354293N',
'北京岁豪汇俊物业管理服务有限公司':'91110105MA0079915R'
}

    output_data('192.168.20.212','dzfp_zzs_kpfw_arm',3306,jieshun8,'捷顺')




if __name__ == '__main__':

    main()
