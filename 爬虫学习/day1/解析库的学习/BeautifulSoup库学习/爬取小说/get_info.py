'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: get_info.py
@time: 2019-06-28 9:58
@desc: 获取小说的作者,名称,章节的url,
'''

from request_method import *



def get_book_info():
    book_info_list=[]
    url='https://www.biquge.info/'
    soup=get_soup(url)
    res=soup.find_all(name='dt')
    for dt in res[:4]:
        temp=[]
        author=dt.find_all('span')[0].string
        chapter_url=dt.find_all('a')[0].attrs['href']
        book_name=dt.find_all('a')[0].string
        temp.append(author)
        temp.append(book_name)
        temp.append(chapter_url)
        book_info_list.append(temp)

    return book_info_list


