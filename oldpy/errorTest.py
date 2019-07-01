while True:
    try:
        #判断依据是字符转化不了整数
        x=int(input('Please enter a int number:'))
        break
    except ValueError:
        print('Oops! That was no valid number.Try again')
