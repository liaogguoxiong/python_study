#今天学习文件的操作
'''
#打开文件,得到文件句柄并赋给一个变量,这样写法是规范的写法
f=open('study','r',encoding='utf-8')#写模式

print(f.read())
print("重新打印一遍________+",f.read())#第一次读句柄(相当于光标)已经到了最下面了,下面已经没有内容了.所以读不到内容


#写模式,如果文件之前存在,会覆盖掉,相当于创建一个新文件,需要注意
f=open('study2','w',encoding='utf-8')
f.write("\n我爱我家,我爱我滴家乡\n")#向文件中读入
f.write("哪里有我最爱的银")


write写入一次之后,如果再次写入,这次写入的内容就会把上次的内容覆盖掉,
如果想接着上次写入的内容继续写入,这时候就得需要用到a模式即(append)追加模式,如下
f=open('study2','a',encoding='utf-8')
a模式下,只能够追加,不能够读

'''
#f=open('study','r',encoding='utf-8')
'''
print(f.readline())#读取一行
print(f.readlines())#读取所有,并把文件转化为列表
'''
'''
读操作
读出所有内容,但不打印第十行
'''
'''
第一种方法,但是效率不高.这个方法把所有的内容取出来之后赋给变量存在内容中,
如果文件很大,这就需要花费很多时间.
for index,line in enumerate(f.readlines()):
    if index == 9:
        print("-------这行不打印--------")
        continue
    print(line.strip())#由于原来的内容每一行默认有一个换行符,使用strip来清除换行和空格
'''
'''
第二种方法,也是最有效率的方法,即一行一行读出容易,读出来之后就删除掉,
最后只保留一行
'''
'''
count=0
for line in f:
    if count == 9:
        print("-------这行不打印--------")
        count+=1#为了防止当count==9的时候,跳出当前循环,下面的count就无法执行到,导致后面输出的都是if语句中的
        continue
    print(line.strip())
    count+=1
'''


'''
上面说过,如果全部把内容读出来,第二次读的时候,就没有内容读了
主要是因为指针(光标)处于最后面了,没内容读了.如果需要重新读的话,就
需要把指针放到开始的位置,这就需要用到f.tell()方法和f.seek()方法.
二者都是以字符为单位,tell()是说明指针所在的位置,seek()把指针放于那个
位置
'''
f=open('study2','r',encoding='utf-8')
print(f.tell())#没读文件的时候,没有字符,所以输出0
print(f.read())
print(f.tell())#现在指针已经在最后面,如果想重新读,就要把指针置为0
f.seek(0)
print("重新读的内容:\n",f.read())




f.close()