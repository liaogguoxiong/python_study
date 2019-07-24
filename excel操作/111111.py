'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 111111.py
@time: 2019-07-19 12:36
@desc:
'''
import re
f=open('input_file','r',encoding='utf-8')
r=f.readlines()
info_list=[]
in_list=[]
for i in r:
    i=i.replace('\n',' ')
    i=re.split('-',i)
    print(i)
    info_list.append(i)

print(info_list)

for i in info_list:
    temp={}
    temp['ip']=i[0]
    temp['port']=i[1]
    temp['dbname']=i[2]
    temp['shuihao']=i[3]
    temp['company_name']=i[4]
    # print(temp)
    in_list.append(temp)

print(in_list)