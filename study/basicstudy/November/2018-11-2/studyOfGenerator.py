#时间：    2018/11/2 23:16
#作者：    lgx
#文件名：  studyOfGenerator

#学习生成器，先学习列表生成器

num=[i*2 for i in range(10)]#列表生成式
print(num)
#如果想得到上面的结果，需要像下面那样做
_num=[]
for i in range(10):
    _num.append(i*2)
print(_num)
__num=(i*2 for i in range(10))#这个才是生成器，用小括号括起来
print(__num.__next__())#读生成器里面的数据只能够用__next__方法来读，一次只能够读一次
print(__num.__next__())#一般使用循环输出生成器中的元素

"""
举例，斐波拉契数列来说明生成器
"""
print("=="*25)
def fib(num):
    a,b,n=0,1,0
    while n < num:
        print(b)
        """
        # 相当于 a=b,b=b+a,但是二者运算是分开的，比如a=1，b=2，所以
        a=b=2       b=b+a=1+2=3  前面a=2并不参与b=b+a的运算
        """
        a,b=b,b+a
        n += 1
fib(10)