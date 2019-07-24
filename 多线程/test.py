'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: test.py
@time: 2019-07-22 17:05
@desc:
'''
import time,threading
g_lock=threading.Lock()

list=[1,2,3,4,5,6,7,8,9]

f=open('a.txt','a',encoding='utf-8')

# for i in list:
#     f.write(str(i))
#     print(i)
#     time.sleep(0.5)

def a(list):

    while len(list):
        g_lock.acquire()
        r=list.pop()
        g_lock.release()
        print(r)
        f.write(str(r))
        time.sleep(1)

for i in range(4):
    th=threading.Thread(target=a,args=(list,))
    th.start()


# a(list)
