#求2-10中的质数，质数只能被1和自己整除的数
#解决思路：求一个范围内的质数，就分别把他们列出来
#然后分别作为被除数，除以从2到本身的数，如果能被一个数
#整除，则不是质数。反之为正数
for n in range(2,10):
    #n除以自己和递减1的数，等于
    print("n为》》》",n)
    #n=2的时候，range(2,2)不成立
    for x in range(2,n):
        print("x>>>",x)
        if n % x ==0:
            print(n,'等于',x,'*',n//x)
            break
    else:
        print(n,'是质数')
