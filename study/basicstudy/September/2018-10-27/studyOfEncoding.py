#今天学习字符转编码操作
import  sys
print("系统默认编码".center(50,'#'))
print(sys.getdefaultencoding())#获取系统默认编码,通过实测默认编码是unicode
s="你好"
print(type(s))
#把utf-8格式的字符转为gbk格式
s_utf_8=s.encode("utf-8")#转为utf-8，因为默认编码为unicode，所以只要编码就可以了
s_gbk=s.encode("gbk")#转为gbk
print(s_utf_8,type(s_utf_8))
print(s_gbk,type(s_gbk))
print(s_gbk.decode("gbk"))#把gbk格式解码为unicode
#s_utf8=s_unicode.encode("gbk")
print(s_utf_8.decode())