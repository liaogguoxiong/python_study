'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: test_input-file.py
@time: 2019-07-23 14:12
@desc:用来测试输入文件的格式是否正确
'''

import  re

list=[]
f=open('input_file.txt','r')
res=f.readlines()
for i in res:
    if len(i) != 0:
        i = i.replace('\n', '')  # 从txt文件中读出来的每行字符串带换行符,要替换为空格
        i = re.split('-', i)
        list.append(i)
for i in list:
    if len(i) !=6:
        print(i)

    print('输入文件的格式完全正确')