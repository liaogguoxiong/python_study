'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: get_books.py
@time: 2019-07-11 16:26
@desc:
'''

import requests,re,time
from bs4 import BeautifulSoup as BS

def get_soup(url):

    res=requests.get(url)
    # 让res.text正确解码网页内容
    res.encoding = res.apparent_encoding
    soup=BS(res.text,'lxml')
    return soup


def get_chapter(url):

    chpater_list = []
    soup = get_soup(url)
    chpater_html=soup.find_all(name='dd')
    li_node=chpater_html[0].find_all('a')
    for i in li_node:
        temp=[]
        end_url=i['href']
        chpater_name=i.text
        # print(chpater_name)
        temp.append(chpater_name)
        temp.append(end_url)
        chpater_list.append(temp)

    return chpater_list


def get_bookinfo(chpater_list):

    book_info=[]
    bash_url='https://www.vodtw.com/html/book/53/53241/'
    for i in chpater_list:
        temp=[]
        content_url=bash_url+i[1]
        temp.append(i[0])
        temp.append(content_url)
        book_info.append(temp)

    return book_info

def get_content(book_list):

    f=open('C:/Users/lgx/Desktop/大江大河.txt','a',encoding='utf-8')
    for i in book_list:
        book_html=get_soup(i[1])
        # print(book_html)
        book_content=book_html.find_all(id='BookText')[0].text.strip()
        book_content=re.sub('  ','\n',book_content)
        f.write(i[0])
        f.write('\n')
        f.write(book_content)
        f.write('\n\n\n')
        print(i[0])
    f.close()


def main():

    url='https://www.vodtw.com/html/book/53/53241/index.html'
    list=get_chapter(url)
    book_info=get_bookinfo(list)
    get_content(book_info)


if __name__ == '__main__':
    main()

