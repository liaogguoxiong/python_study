'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: elements.py
@time: 2019-06-06 23:33
@desc:
'''

import selenium.webdriver

driver=selenium.webdriver.Chrome()
url="https://www.baidu.com/"
driver.get(url)
a_elements=driver.find_element_by_tag_name("a")
print(type(a_elements))
print(a_elements.text)

driver.close()