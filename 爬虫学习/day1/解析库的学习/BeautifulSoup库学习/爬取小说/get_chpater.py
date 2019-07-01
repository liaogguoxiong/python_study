'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: get_chpater.py
@time: 2019-06-28 10:32
@desc:用来获取小说章节
'''
from request_method import *

def get_book_chapter(url):

    chpater_list=[]
    soup=get_soup(url)
    #print(soup)
    chpater_html=soup.find_all(name='dd')

    for dd in chpater_html:
        temp = []
        #print(dd)
        end_url=dd.find_all('a')[0].attrs['href']
        chpater_name=dd.find_all('a')[0].attrs['title']
        temp.append(chpater_name)
        temp.append(end_url)
        chpater_list.append(temp)

    return chpater_list


