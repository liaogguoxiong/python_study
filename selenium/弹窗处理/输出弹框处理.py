'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 输出弹框处理.py
@time: 2019-06-04 16:08
@desc:
'''

import selenium.webdriver
import time

driver=selenium.webdriver.Chrome()

url="file:///C:/Users/lgx/Desktop/1/test1.html"

driver.get(url)

driver.find_element_by_id("prompt").click()
poppu=driver.switch_to.alert
print(poppu.text)

#在弹框内输入信息
poppu.send_keys("廖国雄")
poppu
poppu.accept()


time.sleep(3)
driver.close()
