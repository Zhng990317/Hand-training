import copy

# a = ['name']
# c = copy.copy(a)
# print('修改前----------------------------------------------')
# print('赋值  >>>',[id(_) for _ in a])
# print('浅拷贝>>>',[id(_) for _ in c])

# a[0] = 'NAME'

# print('修改后----------------------------------------------')
# print('赋值  >>>',[id(_) for _ in a])
# print('浅拷贝>>>',[id(_) for _ in c])

# a = [['first'],'name']
# c = copy.copy(a)
# d = copy.deepcopy(a)
# print('修改前----------------------------------------------')
# print('%s赋值  >>>%s'%(a, [id(_) for _ in a]))
# print('%s浅拷贝>>>%s'%(c, [id(_) for _ in c]))

# a[0][0] = 'firstName'
# a[1] = 'lastName'

# print('修改后----------------------------------------------')
# print('%s赋值  >>>%s'%(a, [id(_) for _ in a]))
# print('%s浅拷贝>>>%s'%(c, [id(_) for _ in c]))
# print('%s深拷贝>>>%s'%(d, [id(_) for _ in d]))

# '''
# 不可变对象:str、int、float、bool、tuple。不可改变自身
# 可变对象:list、set、dict。可以改变
#     可变对象改变，地址不变；
#     不可变对象改变后（重新赋值），相当于创建一个新对象，地址改变。
# is:比较的是地址
# ==:比较的是值
# 浅拷贝:
#     不可变对象:构造一个新对象,引用原对象加入到新对象中;当原对象改变时(开辟一个新内存空间),新对象不变;
#     可变对象:构造一个新对象,引用原对象加入到新对象中;当原对象改变时(地址不变),新对象也改变;
# 深拷贝:
#     构造一个新的对象，拷贝原对象指向的的所有对象。和原对象再无联系。
# '''

data = ['PythonCookbook','$120',(2023,5,11)]
_,price,_ = data
print(price)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(fields)

#打印99乘法表
from collections import deque
for i in range(1,10):
    for j in range(1,i+1):
        print("%s*%s=%s\t"%(i,j,i*j),end='')
        if i == j:
            print()

a = 1
while a <= 9:
    b=1
    while b <= a:
        print("%s*%s=%s\t"%(a,b,a*b),end='')
        b+=1
    print()
    a += 1
