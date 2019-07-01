#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-30 17:11
#!@Filename:爬取小说.py
'''
爬取笔趣阁中的小说
'''
import requests
import re

def get_info_book(url,reg):
    '''
    此方法传入url和正则表达式来获取网页的内容
    :param url:
    :param reg:
    :return:
    '''
    headers = {
        'user - agent': 'Mozilla / 5.0(Windows NT 6.1;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 71.0.3578.98Safari / 537.36'
    }
    res = requests.get(url, headers=headers)
    # 让res.text正确解码网页内容
    res.encoding = res.apparent_encoding
    if res.status_code == 200:
        #compile()把正则表达式编译成正则表达式对象,
        #以便重读使用
        pattern = re.compile(reg,re.S)
        res = re.findall(pattern, res.text)
        return res
    else:
        print('出错了')

def main():
    content_url_list=[]
    #观察url可知,小说的内容的url都是base_url加上书的编号
    base_url="https://www.biquge.info/10_10582/"
    #小说网站主页的url
    web_url = 'https://www.biquge.info/'
    #捕获网站小说的正则表达式
    book_reg='<dt><span>(.*?)</span>.*?href="(.*?)">(.*?)</a>'
    #把小说网站主页的url和捕获网站小说的正则表达式传入,可获得小说的信息
    res_book=get_info_book(web_url,book_reg)
    print(res_book)
    #每个小说目录url
    # book_url=res_book[0][1]
    # #捕获小说目录的正则表达式
    # catalog_reg='<dd.*?href="(.*?)".*?title="(.*?)">'
    # #把小说目录页面的url和捕获小说目录的正则表达式传入,可获得目录信息
    # book_catalog=get_info_book(book_url,catalog_reg)
    # #获取最新5章小说内容的url地址,即把相同的url加上书的编号
    # for i in book_catalog[-5:]:
    #     #相同的url加上书的编号
    #     content_url=base_url+i[0]
    #     print(content_url)
    #     #把小说内容的url存入列表
    #     content_url_list.append(content_url)
    # #捕获小说内容的正则表达式
    # content_reg='<meta\sname="keywords"\scontent="(.*?)">.*?<div\sid="content">(.*?)</div>'
    # #循环输出小说的内容
    # with open("C:/Users/xiao/Desktop/三寸人间.txt", 'w', encoding='utf-8') as f:
    #     f.write("")
    # for url in content_url_list:
    #     content_res=get_info_book(url,content_reg)
    #     print(content_res[0][0][5:])
    #     book_content1 = re.sub('<.*?;', "\n", content_res[0][1])
    #     book_content2 = re.sub('&.*?;', "", book_content1)
    #     print(book_content2)
    #     with open("C:/Users/xiao/Desktop/三寸人间.txt", 'a', encoding='utf-8') as f:
    #         f.write(content_res[0][0][5:]+'\n')
    #         f.write(book_content2)

if __name__ == '__main__':
    main()