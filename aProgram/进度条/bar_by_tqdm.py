'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: bar_by_tqdm.py
@time: 2019-07-18 13:56
@desc:
'''

from  tqdm import tqdm
import time

# 这里同样的，tqdm就是这个进度条最常用的一个方法
# 里面存一个可迭代对象
for i in tqdm(range(1, 100)):
   # 模拟你的任务

