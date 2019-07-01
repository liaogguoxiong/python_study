'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: get_content.py
@time: 2019-06-28 10:38
@desc:
'''

from request_method import *
import re
import threading

gLock=threading.Lock()

def get_book_content(url,book_name,chapter_name):

    soup=get_soup(url)
    book_content=soup.find_all(id="content")[0].text.strip()
    # print(book_content)
    f = open(book_name, 'a', encoding='utf-8')
    # with open(book_name,'a',encoding='utf-8') as f:
    f.write("\n\n")
    f.write("\t")
    f.write(chapter_name)
    f.write("\n\n\n")
    f.write(book_content)
    f.write("\n")
    f.close()






