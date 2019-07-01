for n in range(2,10):
    for x in range(2,n): #当range(2,2)的时候,循环不成立,因为区间只包含左区间,不包含右区间.
        if n % x ==0:
            print(n,'等于',x,'*',n//x)
            break
    else:
        print(n,'是质数')
