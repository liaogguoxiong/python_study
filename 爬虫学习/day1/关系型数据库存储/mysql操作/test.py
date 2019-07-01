'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: test.py
@time: 2019-06-24 16:45
@desc:
'''

data={
    'id':'1',
    'name':'sss',
    'age':22,
    'sex':'man'

}
print(data.keys())
key=','.join(data.keys())
print(key,)
value=','.join(['%s']*len(data))
print(value)
tab_name='students'
sql='insert into {table}({key}) values({value}) '.format(table=tab_name,key=key,value=value)
print(sql)
print(sql,tuple(data.values()))
print("%s,%s"%('hello','nihao'))