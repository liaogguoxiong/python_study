age=int(input('请输入你家狗狗的年龄：\n'))
print("")
if age<0:
    print('你仿佛在逗我')
elif age==1:
    print('相当于14岁的人了')
elif age==2:
    print('相当于22岁的人了')
elif age>2:
    human=22+(age-2)*5
    print('相当于',human,'岁的人了')

