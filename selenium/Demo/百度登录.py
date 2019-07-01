'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 百度登录.py
@time: 2019-06-04 16:17
@desc:测试下登录百度账号
'''

import selenium.webdriver
import time

driver=selenium.webdriver.Chrome()

url='https://www.baidu.com/'

driver.get(url)
driver.find_element_by_link_text("登录").click()
time.sleep(2)
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
time.sleep(2) # 弹窗出现后，使页面等待2S
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("526831381@qq.com")
time.sleep(1)
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("li@o0121")
time.sleep(1)
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()





