#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-02-01 10:15
#!@Filename:爬取小说2.py
'''
爬取小说.py已经实现了爬取小数的功能
爬取小说2.py来完善爬取2本小说

实现思路:
        找出小说对应的章节url,然后在章节url中
        找到章节内容的url,根据章节内容的url
        捕获小说内容,并写入文本中
'''
from lxml import etree
import requests
import re
import time
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
    # while True:
    #     time.sleep(2)
    #     res = requests.get(url, headers=headers)
    #     res.encoding = res.apparent_encoding    # 让res.text正确解码网页内容
    #     if res.status_code == 200:
    #         pattern = re.compile(reg,re.S)      #compile()把正则表达式编译成正则表达式对象,以便重读使用
    #         res = re.findall(pattern, res.text)
    #         return res
    #         break
    #     else:
    #         print(res.status_code)
    #         print('出错了,继续请求!!!')
    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding  # 让res.text正确解码网页内容
    if res.status_code == 200:
        pattern = re.compile(reg, re.S)  # compile()把正则表达式编译成正则表达式对象,以便重读使用
        res = re.findall(pattern, res.text)
        return res
    else:
        print(res.status_code)
        print('出错了,继续请求!!!')
def main():
    web_url='https://www.biqiuge.com'
    books_url_list=[]       #小说URL列表,用来存小说的url
    content_url_list=[]     #用来存小说内容对应的url
    catalog_name_list=[]    #用来存小说章节的名字
    web_reg='<dt>.*?href="(.*?)".*?</dd>'   #找出捕获小说的url
    books_id=get_info_book(web_url,web_reg)   #得到小说的ID,加上小说网站主页的url就可以得到小说章节页面的url
    print(type(books_id))
    '''
    如果http请求失败之后,返回的列表为空
    导致取元组中的值的时候会报错
    '''
    if books_id == None:
        print("请求失败,请稍后再试")
    print(books_id[0:2])
    '''
    把小说主页的url和小说的id连接起来
    就可以得到小说章节页面的url
    '''
    for i in books_id[:2]:
        books_url=web_url + i
        books_url_list.append(books_url)
        print(books_url_list)

    for i in books_url_list:
        print(i)
        catalog_reg='<dd>.*?="(.*?)">(.*?)</a></dd>'    #捕获章节的url的正则表达式
        catalog_content=get_info_book(i,catalog_reg)
        print(catalog_content[-5:])                     #只捕获最新的五章小说的url
        for url in catalog_content[-5:]:
            content_url = web_url + url[0]              #小说章节的url+小说主页的url
            print(content_url)
            content_url_list.append(content_url)
    print(content_url_list)
    with open("圣墟.txt", 'w') as f:    #因为只需要捕获每天更新的章节,所以每次运行先清空再写入
        f.write("")
    i=0
    for url in content_url_list:
        content_reg='<h1>(.*?)</h1>.*?<div id="content" class="showtxt">(.*?)</div>'  #捕获小说章节名字和章节内容的正则表达式
        res1=get_info_book(url,content_reg)
        print(res1)
        if res1 == None:
            print('请求没有响应,请重新运行')
            break
        res2=res1[0][1]                         #小说的内容   小说的章节 res1[0][0]
        res3=re.sub('\u3000\u3000','',res2)
        res_content=re.sub('<br /><br />','\n',res3)
        if i <= 4:
            with open("圣墟.txt", 'w',encoding='utf-8') as f:
                f.write(res1[0][0]+'\n')
                f.write(res_content)
        else:
            with open("三寸人间.txt", 'w',encoding='utf-8') as f:
                f.write(res1[0][0]+'\n')
                f.write(res_content)
        i += 1





if __name__ == '__main__':
    main()