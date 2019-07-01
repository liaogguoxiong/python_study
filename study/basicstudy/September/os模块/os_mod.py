import os
#os.popen("操作系统的命令") py在哪里就是执行那个系统的命令
cmd_res=os.popen("dir")#dir查看当前目录的文件，把结果赋给cmd_res，存在内存中,是一个内存地址0
print("___________",cmd_res)
cmd_res_read=os.popen("dir").read()#从内存地址中读出结果
print(cmd_res_read)
os.mkdir("mkdirOfTest")#在当前目录下创建文件夹'''
os.makedirs("D:/MAKEDIR/HELLO",exist_ok=True) #递归创建文件夹,如果中间有文件夹不存在,也不会报错