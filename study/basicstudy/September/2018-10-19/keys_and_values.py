# @Author  :lgx
# @Time    :2019-03-18 0:02
# @File    :keys_and_values.py

dir_test={1:"hello",
          2:"lgx",
          3:"nihao"
          }
print(dir_test.keys())
print(dir_test.values())
for key,value in dir_test.items():
    print(key,value)