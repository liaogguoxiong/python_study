'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 确认的弹窗处理.py
@time: 2019-06-04 15:09
@desc:a module that login fapiao systemctl,use selenium to realize it
'''

import selenium.webdriver
import  time


#初始化selenium,使用webdriver中的Chrome浏览器
driver=selenium.webdriver.Chrome()

url='file:///C:/Users/lgx/Desktop/1/test1.html'

#使用driver打开url的网页
driver.get(url)
# driver.find_element_by_id("u1").find_element_by_class_name("lb").click()
# driver.find_element_by_link_text("登录").click()
# driver.find_element_by_link_text("用户名登录").click()

driver.find_element_by_id("alert").click()
time.sleep(0.5)

#弹窗处理,使用driver中的switch_to.alert函数.只是简单的确认弹窗
dig_alert=driver.switch_to.alert
time.sleep(0.5)

#打印弹窗的内容
print(dig_alert.text)
time.sleep(0.5)

#接受确认
dig_alert.accept()


time.sleep(5)
#关闭打开的网页
driver.close()