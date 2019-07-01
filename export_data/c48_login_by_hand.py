'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: c48_login_by_hand.py
@time: 2019-06-06 16:29
@desc:
'''

import selenium.webdriver
import time
from selenium.webdriver.support.select import  Select

url="http://192.168.20.57:9081/zzs_kpfw_manager/login.htm"

driver=selenium.webdriver.Chrome()
#driver.maximize_window()
driver.get(url)
driver.find_element_by_id("user_account").send_keys("admin")
time.sleep(1)
driver.find_element_by_id("password").send_keys("Aisino123+")
time.sleep(1)
yzm=input("请输入验证码:")
driver.find_element_by_id("validCode").send_keys(yzm)
time.sleep(1)
driver.find_element_by_class_name("button_login").click()
time.sleep(1)
driver.find_element_by_xpath("//span[contains(text(),'月度统计')]").click()
time.sleep(3)
# Select(driver.find_element_by_xpath("//select[@id='search_fpzl']")).select_by_index("2")
# select_elements=driver.find_element_by_css_selector("#search_fpzl")
# print(select_elements)
driver.find_element_by_id("_easyui_textbox_input5").send_keys("123456789")