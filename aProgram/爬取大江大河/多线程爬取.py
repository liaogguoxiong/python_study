'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 多线程爬取.py
@time: 2019-07-18 10:27
@desc:
'''
import requests,re,time
from bs4 import BeautifulSoup as BS
import threading
from  tqdm import tqdm

g_lock=threading.Lock()
CHAPTER_LIST=[]
CONTENT_LIST=[]
BASH_URL='https://www.vodtw.com/html/book/53/53241/'


def get_soup(url):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    res=requests.get(url,headers=headers)
    # 让res.text正确解码网页内容
    res.encoding = res.apparent_encoding
    soup=BS(res.text,'lxml')
    return soup

def get_chapter():
    soup = get_soup(BASH_URL)
    #print(soup)
    chpater_html=soup.find_all(name='dd')
    while len(chpater_html)==0:
        print("请求为空,稍等2秒继续请求")
        time.sleep(2)
        soup = get_soup(BASH_URL)
        chpater_html = soup.find_all(name='dd')
    li_node=chpater_html[0].find_all('a')
    for i in li_node:
        temp=[]
        end_url=i['href']
        chpater_name=i.text
        # print(chpater_name)
        temp.append(chpater_name)
        temp.append(end_url)
        CHAPTER_LIST.append(temp)


def get_book_info():
    get_chapter()
    for i in CHAPTER_LIST:
        temp=[]
        content_url=BASH_URL+i[1]
        temp.append(i[0])
        temp.append(content_url)
        CONTENT_LIST.append(temp)


def download_book(list):
    f = open('大江大河.txt', 'a', encoding='utf-8')
    while True:
        g_lock.acquire()
        if len(list)==0:
            g_lock.release()
            break
        else:
            url=list.pop()[1]
            chapter_name=list.pop(0)[0]
            g_lock.release()
            book_html = get_soup(url)
            book_content = book_html.find_all(id='BookText')
            #book_content = book_html.find_all(id='BookText')[0].text.strip()
            while len(book_content)==0:
                time.sleep(2)
                print("请求为空,稍等2秒继续请求")
                book_html = get_soup(url)
                book_content = book_html.find_all(id='BookText')
            book_content = book_html.find_all(id='BookText')[0].text.strip()
            book_content = re.sub('  ', '\n', book_content)
            f.write(chapter_name)
            f.write('\n')
            f.write(book_content)
            f.write('\n\n\n')
            #print(chapter_name)
    f.close()

def main():
    for i in tqdm(range(1, 100)):
        get_book_info()
        #print(CHAPTER_LIST)
        for x in range(10):
            th=threading.Thread(target=download_book,args=(CONTENT_LIST,))
            th.start()
        # get_chapter()



if __name__ == '__main__':
    main()









