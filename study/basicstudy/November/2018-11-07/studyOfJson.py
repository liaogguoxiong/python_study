#时间：    2018/11/7 22:21
#作者：    lgx
#文件名：  studyOfJson

#学习json序列化

f=open("test1","r",encoding="utf-8")
dic={
    "boy":"lgx",
    "girl":"zsy"
}
#f.write(str(dic))#把字典变成字符串
# f.write(dic)
# data=f.readline()#其实读出来的是字符串
# print(data)
# print(data[1])
# data2=eval(data)#把字符串变成字典
# print(data2)
# print(data2[1])
# f.close()

"""
简单的数据类型序列化,用json序列化，有dumps方法和loads方法
"""
import json
#
# data=json.dumps(dic)#序列化，即把字典转化为字符串，标准的.这条代码等同于：data=json.dump(dic,f)
# print(data)
# f.write(data)
# data=json.loads(f.read())#反序列化，把字符串变成字典.这条代码等同于：data=json.load(f)
# print(data["boy"])
# f.close()

# """
# 复杂的数据类型转化，用pickle序列化，有dumps、loads方法，只能在python中使用
# """
def hello(name):
    print("say hello to %s"%name)

dic={
    "boy":"lgx",
    "girl":"zsy",
    "func":hello#value为内存地址
}
f=open("test1","rb")
import json
import pickle
# data=json.dumps(dic)
# f.write(data)#json不可以把内存地址序列化
# #=====================================
# data=pickle.dumps(dic)#pickle序列化复杂的数据
# f.write(data)
#=====================================
#反序列化
data=pickle.loads(f.read())
print(data["func"]("lgx"))
"""
一般来说，dumps一次，loads一次。如果想多次dumps，则存入不同的文件中
"""
f.close()





