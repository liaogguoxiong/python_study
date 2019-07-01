#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-28 14:27
#!@Filename:抓取网页.py

'''
抓取的页面url:https://www.zhihu.com/explore
'''
import re
import requests
url="https://www.zhihu.com/explore"
#构造头部信息,伪造为浏览器访问
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r=requests.get(url,headers=headers)
print(r.status_code)
pattern=re.compile('explore-feed.*?question_link.*>(.*?)</a>',re.S)
print(pattern)
titles=re.findall(pattern,r.text)
print(titles)