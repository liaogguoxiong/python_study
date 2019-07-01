'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: main_process.py
@time: 2019-06-28 10:54
@desc:
'''

from get_chpater import  *
from get_content import  *
from get_info import *

#

book_info=get_book_info()

for i in book_info:
    # print(i)
    #i[1]为书名,i[2]为章节的url
    chapter=get_book_chapter(i[2])
    for j in chapter:
        print(j[0])
        #j[0]为章节名,j[1]为内容url
        content_url=i[2]+j[1]
        get_book_content(content_url,i[1],j[0])




