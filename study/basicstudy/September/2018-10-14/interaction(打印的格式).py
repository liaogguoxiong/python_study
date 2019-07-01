#今天学习的是格式输出
name=input("Please input your name:")
age=int(input("Please input your age:"))
salary=input("Please input your salary:")
info='''-------the first information of %s---------
name is :%s
age  is :%d
salary is :%s
print(---------------------------------------)
'''%(name,name,age,salary)
print(info)

info2='''-------the second information of {_name}-------
name is :{_name}
age is :{_age}
salary is :{_salary}
'''.format(_name=name,_age=age,_salary=salary)
print(info2)

info3='''----------the third information of {0}--------
name is :{1}
age is :{2}
salary is :{3}
'''.format(name,name,age,salary)
print(info3)