'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 11.py
@time: 2019-07-15 10:49
@desc:
'''


n=0
j=0
while n <= 12/3:
    j=0
    while j <= 12/1.5:
        sum=n*3+j*1.5
        if  sum== 12:
            print("可以买铅笔%d只,钢笔%d只"%(j,n))
        j+=1
    n+=1