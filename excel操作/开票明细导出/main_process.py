'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: main_process.py
@time: 2019-07-22 9:46
@desc:
'''
from dispose_input_file import *
from output_data import *
import threading
import time

g_lock=threading.Lock()

def test(list):
        # g_lock.acquire()
        # while len(list):
        #     print(list)
        #     print(len(list))
        #     d=list.pop()
        #     # print(d)
        #     data_from_mysql(d)
        # g_lock.release()
        while True:
            g_lock.acquire()
            if len(list)==0:
                g_lock.release()
                break
            else:
                d=list.pop()
                g_lock.release()
                data_from_mysql(d)

        #time.sleep(1)

def main():
    res=deal_method()
    # for i in res:
    #     data_from_mysql(i)
    #     time.sleep(1)
    for t in range(10):
        th=threading.Thread(target=test,args=(res,))
        th.start()
        # th.join()




if __name__ == '__main__':

    main()
