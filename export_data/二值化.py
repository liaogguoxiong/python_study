'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 二值化.py
@time: 2019-06-06 11:10
@desc:
'''

from PIL import  Image
import sys
from pytesseract import  *




threshold = 140
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)

def  getverify1(name):

    img = Image.open(name)
    imgry=img.convert("L")
    imgry.save("无标题1.png")
    out=imgry.point(table,"1")
    out.save("无标题2.png")






