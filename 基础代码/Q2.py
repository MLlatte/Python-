for i in range(1,10):
    print(i)
a=[4,56,78,3,32]
for i in range(len(a)):
    print('i =',i,'number in a=',a[i])



a=list(range(5))
print(a)
print(a[0:-2])

#注意有无逗号的区别
tup1=(5)#如果是list，则有无逗号都是列表
print(tup1)
print(type(tup1))# 不加逗号，类型为整型

tup2=(5,)
print(tup2)
print(type(tup2)) # 加上逗号，类型为元组
