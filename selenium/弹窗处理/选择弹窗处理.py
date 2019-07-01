'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 选择弹窗处理.py
@time: 2019-06-04 16:00
@desc:
'''

import selenium.webdriver
import time

driver=selenium.webdriver.Chrome()

url="file:///C:/Users/lgx/Desktop/1/test1.html"

driver.get(url)
driver.find_element_by_id("confirm").click()

#实例化弹窗
popup=driver.switch_to.alert
time.sleep(0.5)
#打印弹窗的内容
print(popup.text)
#点击取消按钮
popup.dismiss()
#点击确定按钮 poopu.accept()
time.sleep(3)
driver.close()

