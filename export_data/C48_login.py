'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: C48_login.py
@time: 2019-06-04 16:36
@desc:这个模块是C48登录所要做的操作,截图验证码,处理验证码,识别验证码,以及输入账号密码
'''

import selenium.webdriver
import time
from  PIL import Image
from  pytesseract import  *
#from  verification_dispose import *
from  verification_incision import  *
from c_noise import *



def getverify1(path,name):
    # 二值化
    threshold = 170
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    # 由于都是数字
    # 对于识别成字母的 采用该表进行修正
    rep = {
        "A 9":'9',"'J":'3','[':'0',"Ml":'4',"Y":'7','4I':'4',",3":'3',"O":"0","o":'0',"~2":'2',"i6":'6',"`F":'7',"15":'5',"'6":'6',"$9":'9',"T5":'5',"-3":'3','BC':'0',"'2":'2',"S]":'0',"~9":'9',
        "\1":'1',"~1":'1',"JR":'5',"-9":'9',",5":'5',"It":'1',"#7":'7',"V 2":'2',"T?":'7',"-6":'6',
        'AC': '0','*7':'7','*1':'1','16':'6','X8':'8',',4':'4','(7':'7','^4':'4','`J':'7','~4':'4',"'II":'4',',1':'1','T':'7','S4':'4','{3':'3',"'X":'7',"~Z`":'7','E':'8','Jz':'1','(':'0','it':'1',"~~1":'1','`f7':'7',"`S":'3',
        "N7":'7',"'O":'0',"Z":'2',"'7":'7',"1;":'1',"3,":'3',
        ",0":'0',"'5":'5',"_5":'5',"\8":'8',"'I":'1',
        '`A;`':'3',';8':'8','Q':'0','C':'0','i':'1','G':'9',
        '?':'7','S':'8','.':'','`':'','A':'1','I':'1','*':'',"'":'1',
        '~': '', '!': '', '@': '', '#': '', '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '','_': '', '=': '', '+': '', ':': '', ';': '', "'": '', '"': '', '<': '', ',': '', '>': '', '.': '', '?': '','/': '', '|': '', '\\': '',
    };
    # 打开图片
    im = Image.open(path+name)
    # 转化到灰度图
    imgry = im.convert('L')
    # 保存图像
    imgry.save(path+name)
    # 二值化，采用阈值分割法，threshold为分割点
    out = imgry.point(table, '1')
    out.save(path+'b' + name)

    #########################################################################################
    # 去除干扰线
    im2 = Image.open(path+'b' + name)
    # 图像二值化
    data = im2.getdata()
    w, h = im2.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            mid_pixel = data[w * y + x]  # 中央像素点像素值
            if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                top_pixel = data[w * (y - 1) + x]
                left_pixel = data[w * y + (x - 1)]
                down_pixel = data[w * (y + 1) + x]
                right_pixel = data[w * y + (x + 1)]
                # 判断上下左右的黑色像素点总个数
                if top_pixel < 10:
                    black_point += 1
                if left_pixel < 10:
                    black_point += 1
                if down_pixel < 10:
                    black_point += 1
                if right_pixel < 10:
                    black_point += 1
                if black_point < 1:
                    im2.putpixel((x, y), 255)
                black_point = 0
    im2.save(path + 'c' + name)

    #########################################################################################
    # 去除干扰线
    im3 = Image.open(path + 'c' + name)
    # 图像二值化
    data = im3.getdata()
    w, h = im.size
    black_point = 0
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if x < 2 or y < 2:
                im3.putpixel((x - 1, y - 1), 255)
            if x > w - 3 or y > h - 3:
                im3.putpixel((x + 1, y + 1), 255)
    im3.save(path + 'd' + name)

    text=image_to_string(im3)
    text=text.strip()
    print("----------")
    print(text)
    print("----------")
    return text





def  verification_get():
     #验证码截取

    url='http://192.168.20.57:9081/zzs_kpfw_manager/login.htm'

    #实例化selenium.webdriver
    driver=selenium.webdriver.Chrome()

    driver.get(url)
    driver.implicitly_wait(1)
    #浏览器窗口最大化
    driver.maximize_window()
    # driver.find_element_by_id("user_account").send_keys("admin")
    # time.sleep(1)
    # driver.find_element_by_id("password").send_keys("Aisino123+")
    # time.sleep(1)

    #截取整个浏览器的图片,并保存起来
    driver.save_screenshot("C:/Users/lgx/Desktop/验证码/1.png")

    #获取验证码的位置信息
    location=driver.find_element_by_id("gencode").location
    print("位置:",location)

    #获取验证码的大小
    size=driver.find_element_by_id("gencode").size
    print("大小:",size)

    coordinate = (int(location['x']) ,int(location['y']), int(location['x'] + size['width']),
              int(location['y'] + size['height']))
    print(coordinate)
    im=Image.open("C:/Users/lgx/Desktop/验证码/1.png")

    #坑爹,电脑分辨率为100%的时候才能够正确截取,其他大小的时候无法正确截取
    im_1=im.crop(coordinate)
     #保存截取成功的验证码
    im_1.save("C:/Users/lgx/Desktop/验证码/1_1.png")

    # time.sleep(3)
    driver.close()


def verification_discern():
    #验证码识别

    #对图片进行二值化,传入图片和图像二值化阀值
    two_value("C:/Users/lgx/Desktop/验证码/1_1.png","C:/Users/lgx/Desktop/验证码/1_2.png")

    #对图片进行降噪处理,传入的参数分别是图片,降噪率(降噪率 0 <N <8),降噪次数
    clear_noise("C:/Users/lgx/Desktop/验证码/1_2.png","C:/Users/lgx/Desktop/验证码/1_3.png")

    clear_noise1("C:/Users/lgx/Desktop/验证码/1_3.png", "C:/Users/lgx/Desktop/验证码/1_4.png")







def main():

    verification_get()
    verification_discern()

    path="C:/Users/lgx/Desktop/验证码/1_4.png"
    out_dir="C:/Users/lgx/Desktop/验证码/"
    img=Image.open(path)
    smart_incise_image(img,out_dir,"aaa",count=4,p_w=3)

    # text1=getverify1("C:/Users/lgx/Desktop/验证码/","aaa_0.png")
    #     # time.sleep(1)
    #     # text2 = getverify1("C:/Users/lgx/Desktop/验证码/", "aaa_1.png")
    #     # time.sleep(1)
    #     # text3 = getverify1("C:/Users/lgx/Desktop/验证码/", "aaa_2.png")
    #     # time.sleep(1)
    #     # text4 = getverify1("C:/Users/lgx/Desktop/验证码/", "aaa_3.png")
    #     # time.sleep(1)
    #     # print(text1,text2,text3,text4)

    list=["C:/Users/lgx/Desktop/验证码/aaa_0.png","C:/Users/lgx/Desktop/验证码/aaa_1.png",
          "C:/Users/lgx/Desktop/验证码/aaa_2.png","C:/Users/lgx/Desktop/验证码/aaa_3.png"]



    for i in list:
        rep = {
            "A 9": '9', "'J": '3', '[': '0', "Ml": '4', "Y": '7', '4I': '4', ",3": '3', "O": "0", "o": '0', "~2": '2',
            "i6": '6', "`F": '7', "15": '5', "'6": '6', "$9": '9', "T5": '5', "-3": '3', 'BC': '0', "'2": '2',
            "S]": '0', "~9": '9',
            "\1": '1', "~1": '1', "JR": '5', "-9": '9', ",5": '5', "It": '1', "#7": '7', "V 2": '2', "T?": '7',
            "-6": '6',
            'AC': '0', '*7': '7', '*1': '1', '16': '6', 'X8': '8', ',4': '4', '(7': '7', '^4': '4', '`J': '7',
            '~4': '4', "'II": '4', ',1': '1', 'T': '7', 'S4': '4', '{3': '3', "'X": '7', "~Z`": '7', 'E': '8',
            'Jz': '1', '(': '0', 'it': '1', "~~1": '1', '`f7': '7', "`S": '3',
            "N7": '7', "'O": '0', "Z": '2', "'7": '7', "1;": '1', "3,": '3',
            ",0": '0', "'5": '5', "_5": '5', "\8": '8', "'I": '1',
            '`A;`': '3', ';8': '8', 'Q': '0', 'C': '0', 'i': '1', 'G': '9',
            '?': '7', 'S': '8', '.': '', '`': '', 'A': '1', 'I': '1', '*': '', "'": '1',
            '~': '', '!': '', '@': '', '#': '', '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '',
            '_': '', '=': '', '+': '', ':': '', ';': '', "'": '', '"': '', '<': '', ',': '', '>': '', '.': '', '?': '',
            '/': '', '|': '', '\\': '',
        };
        text=image_to_string(i)
        text=text.strip()
        for i in rep:
            text=text.replace(i,rep[i])
        print("识别:",text)






if __name__ == '__main__':

    main()













