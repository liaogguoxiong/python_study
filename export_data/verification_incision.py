'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: verification_incision.py
@time: 2019-06-05 14:15
@desc:获取到的验证码为4位数字,现在要讲它们分别切开,分成4个数字
'''

from PIL import Image


def smart_incise_image(img,outDir,ii,count,p_w=3):
    #把验证码切割为4位数字
    '''
    :param img:
    :param outDir:
    :param count: 图片中有多少个图片
    :param p_w: 对切割地方多少像素内进行判断
    :return:
    '''

    w,h=img.size
    pixdata = img.load()
    eachWidth = int(w / count)
    beforeX = 0

    for i in range(count):

        allBCount = []
        # nextXOri = (i + 1) * eachWidth
        if i == 0:
            nextXOri = (i + 1) * eachWidth + 4
        if i == 1:
            nextXOri = (i + 1) * eachWidth + 4
        if i == 2:
            nextXOri = (i + 1) * eachWidth
        if i == 3:
            nextXOri = (i + 1) * eachWidth + 6

        for x in range(nextXOri - p_w, nextXOri + p_w):
            if x >= w:
                x = w - 1
            if x < 0:
                x = 0
            b_count = 0
            for y in range(h):
                if pixdata[x, y] == 0:
                    b_count += 1
            allBCount.append({'x_pos': x, 'count': b_count})
        sort = sorted(allBCount, key=lambda e: e.get('count'))

        nextX = sort[0]['x_pos']
        box = (beforeX, 0, nextX, h)
        print(outDir + str(ii) + "_" + str(i) + ".png")
        img.crop(box).save(outDir + str(ii) + "_" + str(i) + ".png")
        beforeX = nextX