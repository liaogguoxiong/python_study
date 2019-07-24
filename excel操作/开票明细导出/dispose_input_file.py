'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: dispose_input_file.py
@time: 2019-07-22 9:36
@desc:
'''

import re

def deal_method():
    '''
    这个方法用来处理读取输入文件的时候获取的格式,
    读的时候是一个列表,然后分割字符串,做成字典,最后
    存入一个列表中
    :return:
    '''
    f=open('input_file.txt','r')
    r=f.readlines()
    #print(r)
    #用来存储分割之后的列表
    info_list=[]
    #用于存储字典格式的税号的mysql信息
    in_list=[]
    for i in r:
        if len(i) != 0:
            i=i.replace('\n','')#从txt文件中读出来的每行字符串带换行符,要替换为空格
            i=re.split('-',i)
            info_list.append(i)
    #print(info_list)



    for i in info_list:
        temp={}
        temp['ip']=i[0].strip()
        temp['port']=i[1].strip()
        temp['dbname']=i[2].strip()
        temp['shuihao']=i[3].strip()
        temp['company_name']=i[4].strip()
        temp['tongcheng']=i[5].strip()

        # print(temp)
        in_list.append(temp)

    return in_list
# deal_method()
# r=deal_method()
# # print(r)
