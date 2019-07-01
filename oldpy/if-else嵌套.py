num=int(input('请输入一个数：\n'))
if num%2==0:
    if num%3==0:
        print(num,'只能被2整除，也能被3整除')
    else:
        print(num,'只能被2整除，不能被整除')
else:
    if num%3==0:
        print(num,'只能被3整除，不能被2整除')
    else:
        print(num,'既不能被2整除，也不能被3整除')
