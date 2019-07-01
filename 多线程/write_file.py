'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: write_file.py
@time: 2019-06-30 23:31
@desc:
'''

import threading
import time
g_lock=threading.Lock()

def test():

    for i in range(1,11):
        with open('a.txt','a',encoding='utf-8') as f:
            time.sleep(0.5)
            g_lock.acquire()
            f.write(str(i))
            g_lock.release()
            f.write('\n')

for i in range(3):
    th=threading.Thread(target=test)
    th.start()



