# @Author  :lgx
# @Time    :2019-03-21 23:36
# @File    :replace_text.py
with open('test_content','r',encoding='utf-8') as f:
    content=f.read()
    print(type(content))
    print(content)

print("--"*50)
print(content.replace("2017","2019"))
print("--"*50)
print(content.split("\n"))
