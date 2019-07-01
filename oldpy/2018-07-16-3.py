import sys
list=[1,2,3,4]
it=iter(list)   #迭代器
while True:
    try:
        print(next(it))
    except  StopIteration:
        sys.exit()
