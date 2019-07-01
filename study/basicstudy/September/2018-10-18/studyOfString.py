#今天学习字符串的操作
name="lgx is  a llll"
print(name.capitalize())#首字母大写
print(name.count('l'))#得出某个字母在字符串中的个数
print(name.center(50,'#'))
print(name.encode())
print(name.endswith('l'))#以什么结尾,可用来做判断
print(name.find('is'))#找出指定字符的位置
print('^woshi'.isidentifier())#标识符，判断是否合法,及命名行不行
print('+'.join(['1','2','3']))#以+来好拼接字符
print('abc'.upper())#把小写转化成大写
print('ABC'.lower())#把大写转化成小写
print('\n    nihao'.lstrip())#去掉左边的空格和换行
print('nihao    \n'.rstrip())#去掉右边的空格和换行
print('\n    nihao \n    '.strip())#去掉二边的的空格和换行
p=str.maketrans('hailgx','123456')#p是转化规则
print('hellonihaoalgx'.translate(p))
print('alex li'.replace('l','L',1))#替换字符，其实1为替换多少个
print('alex li'.rfind('l'))#查找字符在字符串中的最后的位置，输出下标
print('alex li'.split("b"))#以什么来划分字符串，默认是以空格，用来划分的字符会消失
print('Alex Li'.swapcase())#大写变小写，小写变大写
print('alex li'.title())#首字母变大写

