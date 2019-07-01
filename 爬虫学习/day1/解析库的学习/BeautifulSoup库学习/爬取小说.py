'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 爬取小说.py
@time: 2019-06-27 17:47
@desc:
'''
import requests
from bs4 import BeautifulSoup as BS
import re
import threading

gLock=threading.Lock()

def get_book_info():
    book_info_list=[]

    url='https://www.biquge.info/'
    res=requests.get(url)
    #print(res.status_code)
    #print(res.text)
    soup=BS(res.text,'lxml')
    res=soup.find_all(name='dt')
    gLock.acquire()
    for dt in res[:4]:
        # print(dt)
        temp=[]
        author=dt.find_all('span')[0].string
        chapter_url=dt.find_all('a')[0].attrs['href']
        book_name=dt.find_all('a')[0].string
        print(chapter_url)
        temp.append(author)
        temp.append(book_name)
        temp.append(chapter_url)
        book_info_list.append(temp)


    # print(book_info_list)
    # return book_info_dir

def get_book_chapter():

    chpater_list=[]
    url='https://www.biquge.info/10_10582/'
    res=requests.get(url)
    # 让res.text正确解码网页内容
    res.encoding = res.apparent_encoding
    soup=BS(res.text,'lxml')
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



def get_book_content():

    url='https://www.biquge.info/10_10582/5103237.html'
    res = requests.get(url)
    # 让res.text正确解码网页内容
    res.encoding = res.apparent_encoding
    soup = BS(res.text, 'lxml')
    book_content=soup.find_all(id="content")[0].text.strip()
    book_content=re.sub('    ','\n',book_content)
    print(book_content)
    with open('study','w',encoding='utf-8') as f:
        f.write(book_content)





