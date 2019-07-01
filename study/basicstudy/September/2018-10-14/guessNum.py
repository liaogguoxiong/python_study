'''
Program:使用if-elfi-else来进行猜字谜，使用while或者for循环来让每个玩家只能够猜三次
Hitory：lgx      2018-10-14      First release
'''
import random
count=0
_kw=random.randint(1,10) #keyword
while (count < 3):
    count+=1
    kw=int(input("请输入您想猜的整数数字，在1-10之间："))
    if kw > 10 or kw < 1:
        print("您输入的数字不在范围内")
        continue
    elif _kw==kw:
        print("恭喜您猜对了！！！！")
        exit(0)
    elif _kw > kw:
        print("您猜的数字小了,您还有{counts}次机会".format(counts=3-count))

    else:
        print("您猜的数字大了,您还有{counts}次机会".format(counts=3-count))
else:
    print("您已经猜了三次，游戏结束！！！！")#这个else和while构成if-else结构，
print(_kw)