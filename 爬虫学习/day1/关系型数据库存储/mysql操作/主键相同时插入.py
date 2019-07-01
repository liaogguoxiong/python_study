'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 主键相同时插入.py
@time: 2019-06-26 16:52
@desc:
'''


# '''
# 抓取数据的时候,在意的是数据重复的问题,
# 如果存在数据重复,我们希望是更新数据,而不是
# 重复保存一次,动态构造sql可以实现去重,如果
# 数据重复,则更新数据,如果不存在则插入数据
#
# 相关的sql语句为:insert into 表名 values(值) on duplicate key update 字段=值,字段=值
#
#  意思是如果插入的主键,比如下面例子中的主键是id,如果id已经存在了,执行update操作,如果其他字段的值有
#变化,则更新这个变化,如果插入的字段和原先字段一样,则没有发生改变,0行受影响,用if判断的
#话,返回false,如果插入的字段不一样,则2行受影响
#       如果插入的主键不存在,则执行插入操作
# '''

import pymysql

db=pymysql.connect(host="192.168.1.126",user="root",password="123456",port=3307,db="test")
cursor=db.cursor()
data={
      'id':'0004',
     'name':'廖国雄',
     'age':'22',
    'sex':'女'
}
table='students'
keys=','.join(data.keys())
print(keys)
num=','.join(['%s']*len(data))
print(num)

#print(sql)
update=','.join(["{key}=%s".format(key=key) for key in data])
print(update)
sql='insert into {tab_name}({keys}) values ({values}) on duplicate key  update '.format(tab_name =table,keys=keys,values=num)
print(sql)
sql +=' ' +update
print(sql)
print(sql,tuple(data.values())*2)

try:

    #如果字段不一样,发生变化,返回true
    if cursor.execute(sql,tuple(data.values())*2):
        db.commit()
        print('successful')

    # 如果字段都一样的话,没有发生变化,返回false
    else:

        print("none chage")

except:

    print('failed')
    db.rollback()

db.close()
