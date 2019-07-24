'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: connect_linuxBySSH.py
@time: 2019-07-17 15:08
@desc:
'''
import paramiko

#创建SSH对象
ssh=paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
#连接服务器
ssh.connect(hostname='192.168.1.126',username='root',password='li@o0121')

#执行命令,执行结果有标准输入,标准输出,标准错误
stdin,stdout,stderr=ssh.exec_command('pws')
res=stdout.read().decode('utf-8')

#如果输入的命令正确,有标准输出,无标准错误,如果
#输入的命令错误,输出标准错误
if res:
    print(res)
else:
    res_err=stderr.read().decode('utf-8')
    print(res_err)


#关闭ssh连接
ssh.close()