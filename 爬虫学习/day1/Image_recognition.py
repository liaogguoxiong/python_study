#！/usr/bin/env python
#！@Author：lgx
#！@时间：2019-01-18 15:53
#!@Filename:图片识别.py
import pytesseract
from PIL import Image
import time
#打开图片

image_path="C:/Users/lgx/Desktop/照片识别/1.png"
image=Image.open(image_path)
#识别图片中的文字,转化为字符串
text=pytesseract.image_to_string(image)
with open("C:/Users/lgx/Desktop/照片识别/info.txt",'w',encoding="utf-8") as f:

    f.write(text)
