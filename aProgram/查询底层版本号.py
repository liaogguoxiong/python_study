'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 查询底层版本号.py
@time: 2019-06-19 19:05
@desc:
'''

import pymysql

dir={'广东广安冠德石化有限公司深圳分公司':'91440300319416657L',
'深圳市顺归加油站有限公司':'91440300731109309T',
'深圳市雄伟李氏经贸物资有限公司威程油气站':'91440300761978388R',
'广东广安冠德石化有限公司惠州鸿业电力加油站':'91441302324755813B',
'广东广安冠德石化有限公司乳源富诚加油站':'91440232398050621Q',
'广东广安冠德石化有限公司四会市贞山加油站':'91441284093122815Y',
'广东广安冠德石化有限公司金乐园加油站':'91440200MA4UH0YE5N',
'四会市凯平加油站有限公司':'91441284MA4UN7452U',
'广东广安冠德石化有限公司肇庆市四通北通加油站':'91441202345311533B',
'广东广安冠德石化有限公司东莞塘厦林村加油站':'914419003042908790',
'东莞市永安石油化工有限公司第二加油站':'914419007192624312',
'台福油品（深圳）有限公司坪地加油站':'914403000638981370',
'西安市长安区八一加油站':'91610116726273243X',
'广东广安冠德石化有限公司珠海和平界冲加油站':'91440400MA4UWXMX67',
'深圳市宝安广安冠德石油贸易有限公司上南加油站':'91440300892472424C',
'中山市古镇七坊加油站':'914420002820415980',
'东莞市黄江东盛加油站有限公司':'914419000506533418',
'济南鉴德石油化工有限公司':'91370103787448537Q',
'山东中惠泽石油有限公司':'91370103575478769F',
'成都鸿浩加气站有限公司':'915101325535515157'
}

#连接数据库
db=pymysql.connect(host='192.168.20.54',user='root',password='A_isino#888',port=3306,db='dzfp_zzs_kpfw_arm')
cursor=db.cursor()

for i in dir:

    #print(dir[i])

    sql='''SELECT rjbb FROM kpfw_jqxx WHERE nsrsbh='{shuihao}' '''.format(shuihao=dir[i])
    #print(sql)
    #执行sql
    cursor.execute(sql)
    #把查询结果一行一行显示出来,实际查询结果也是一行
    data=cursor.fetchone()
    print(i+":",data)





