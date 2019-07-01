'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: test.py
@time: 2019-06-05 13:52
@desc:
'''

dir={"name":"lgx","age":"22","sex":"man"}
print(dir["name"])
print(dir.get("name"))
#print(dir["grade"])
print(dir.get("grade"))
dir["grade"]="gradution"
print(dir)
