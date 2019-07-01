'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 贴吧登录.py
@time: 2019-06-06 23:15
@desc:
'''

import selenium.webdriver
import time

url="https://tieba.baidu.com/index.html#"

driver=selenium.webdriver.Chrome()
driver.maximize_window()
driver.get(url)
driver.find_element_by_link_text("登录").click()
time.sleep(3)
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
driver.find_element_by_id("TANGRAM__PSP_10__userName").click()
driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys("526831381@qq.com")
driver.find_element_by_id("TANGRAM__PSP_10__password").click()
driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys("li@o0121")
driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@class='onekey_btn']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@class='j_sign_btn sign_btn sign_btn_nonmember']").click()

#######都有验证码
