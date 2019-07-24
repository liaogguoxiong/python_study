'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: basic.py
@time: 2019-07-18 9:22
@desc:
'''

import threading,time

def show(arg):
    time.sleep(1)
    print('thread'+str(arg))

for i in range(10):
    th=threading.Thread(target=show,args=(i,))
    th.start()

print("main thread stop")