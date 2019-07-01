#Program:1.启动程序，让用户输入工资，然后打印商品列表
#        2.允许根据商品编码购买商品
#        3.用户选择商品后，检测余额是否够，够就扣款，不够就提醒
#        4.可随时退出，退出时，打印已购买的商品和余额
#History：lgx    2018/10/17      First release
import time
goods_list=[
    ("iphonx",8500),
    ("xiaomi2s",3400),
    ("huawei",4000),
    ("vivo",3800)
]
shoppingCarList=[]
balance=float(input("请输入您的余额："))
while True:
    print("商品编号\t\t商品名称\t\t价格")
    for index,item in enumerate(goods_list):
        print(index,"\t\t",item[0],"\t\t",item[1])
    time.sleep(1)
    uc=input('请输入您要购买的商品编号：')#uc=userchoice
    if uc.isdigit():   #判断输入的是不是是不是整数
        uc=int(uc)
        if uc > -1 and uc < len(goods_list): #
            goods=goods_list[uc]
            if balance >= goods[1]:   #如果余额大于商品价格,则可以购买
                balance-=goods[1]
            else:
                time.sleep(1)
                print("余额不足")
                break
            shoppingCarList.append(goods)
            time.sleep(1)
            print("您购买了", goods[0])
        else:
            time.sleep(1)
            print("商品不存在")
    else:
        if uc == 'q':
            break
        else:
            time.sleep(1)
            print("无效的命令！！！请重新输入！！！")
            continue
time.sleep(1)
print("您购物车的中商品有：")
for p in shoppingCarList:
    print(p)
time.sleep(1)
print("您的余额为：%s" %balance)



