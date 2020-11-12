#高级特性 切片(slice)
r=[]
n=3
L=['a','b','c','d','e']
# for i in range(n):  #range(n)为零到n-1的元素
#     r.append(L[i])
# print(r)
#对这种经常取指定索引范围的操作，用循环十分繁琐
#因此，Python提供了切片（Slice）操作符，能大大简化这种操作
print(L[0:3])  #从0开始取，取到3为止，但不包括3
#第一个索引是零时可以省略
print(L[:3])
print(L[1:3])
#既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:]) #从倒数第二个到底
print(L[-2:-1])#从倒数第二个到倒数第一个，不含倒数第一个
print(L[1:-1])

L=list(range(100))
print(L)
for i in L:
    print(i)
#L[:10]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#L[-10:]
#[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

# L[10:20]
# [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# L[:10:2]
# [0, 2, 4, 6, 8]

# L[::5]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
# 55, 60, 65, 70, 75, 80, 85, 90, 95]

# L[:]
# [0, 1, 2, 3, ..., 99]
# tuple也是一种list，唯一区别是tuple不可变。因此，
# tuple也可以用切片操作，只是操作的结果仍是tuple：
# (0, 1, 2, 3, 4, 5)[:3]
# (0, 1, 2)
# 字符串'xxx'也可以看成是一种list，每个元素就是一
# 个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
# 'ABCDEFG'[:3]
def trim(s):
    while(s[:1]==' '):
        s=s[1:]
    while(s[-1:]==' '):
        s=s[:-1]
    return s

# 迭代
# Python的for循环抽象程度要高于C的for循环，因为Python的for循环
# 不仅可以用在list或tuple上，还可以作用在其他可迭代对象上

#dict 的迭代
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)
for ch in 'abc':
    print(ch)
# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常
# 运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable
# 类型判断：
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

# 如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate
# 函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：
for i,value in enumerate(['a','b','c']):
    print(i,value)
#上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x,y in [(1,1),(2,4),(3,9)]:
    print(x,y)

def findMinMax(L):
    if L==[]:
        return (None,None)
    else:
        min=max=L[0]
        for values in L:
            if values > max:
                max = values
            if values < min:
                min = values
        return (min,max)

min,max=findMinMax([7, 1,3,9,5])
print(min,max)
print(list(range(1,11)))
L=[]
for x in range(1,11):
    L.append(x*x)
print(L)
#但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
print([x * x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])
#还可以使用两层循环，构成全排列：
print([m + n + p for m in 'abc' for n in 'xyz' for p in '123'])
#运用列表生成式，可以写出非常简洁的代码。例如，
# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
print([d for d in os.listdir('.')])
# for 循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d={'x':'A','y':'b','z':'c'}
for key,value in d.items():
    print('key=',key,'value=',value)
#列表生成式中if-else的用法：
#1.不能在最后的if加上else，因为跟在for后面的if是个筛选条件
#2.if写for前面必须加else
print([x if x%2 == 0 else -x for x in range(1,11)])
#如果x%2== 0 eql true 则输出x,反之输出-x

#homework:
#如果list中既包含字符串，又包含整数，由于非字符串类型没有
# lower()方法，所以列表生成式会报错：
#使用内建的isinstance函数可以判断一个变量是不是字符串：
L1=['Hello','World',18,'Apple',None]
L2=[x.lower() for x in L1 if isinstance(x,str)]
print(L2)

#生成器
#通过列表生成式可以创建列表，但列表内存容量有限，创建大列表占用内存空间
#很大，此时可用generator（生成器）把列表元素按某种方式推算出来
g=(x*x for x in range(10))
#如何打印出generator中的每一个元素呢？
for n in g:
    print(n)
#generator非常强大。如果推算的算法比较复杂，
# 用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'
#定义generator的另一种方法
#如果一个函数定义中包含yield关键字，
# 那么这个函数就不再是一个普通函数，而是一个generator：
#   这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，
# 遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，
# 遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print ("step 3")
    yield 5
o=odd()
next(o)
next(o)
next(o)
def triangles():
    L=[1]
    while True:
        yield L
        L=[L[i]+L[i+1] for i in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
#generator函数的“调用”实际返回一个generator对象：

#迭代器
# 我们已经知道，可以直接作用于for循环的数据类型有以下几种：

# 一类是集合数据类型，如list、tuple、dict、set、str等；

# 一类是generator，包括生成器和带yield的generator function。

# 这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

# 可以使用isinstance()判断一个对象是否是Iterable对象：
from collections.abc import Iterator
isinstance([],Iterable)
isinstance({},Iterable)
isinstance('abc',Iterable)
#而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值
# ，直到最后抛出StopIteration错误表示无法继续返回下一个值了。

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
#可以使用isinstance()判断一个对象是否是Iterator对象：
print(isinstance([],Iterator))
#生成器都是Iterator对象，但list、dict、str虽然是Iterable，
# 却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]),Iterator))

#函数式编程
#函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数
# 没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的
# 这种纯函数我们称之为没有副作用。而允许使用变量的程序设计语言，
# 由于函数内部的变量状态不确定，
# 同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。
m=abs
print(m(-10))
#那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，
#完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！

#传入函数
#高阶函数：把函数作为参数传入
def add1(x,y,f):
    return f(x)+f(y)
print(add1(-5,6,abs))
#map/reduce 函数
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))#map返回的时Iterator,是一个惰性序列（只能next(r)输出下一个，和
#用for n in r 输出所有元素）
print(list(map(str,[1,2,3,4,5,6,7,8,9])))
#reduce 用法：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收
# 两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
from functools import reduce
def add2(x,y):
    return x+y
print(reduce(add2,[1,3,4,5,6]))
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
    digits={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
reduce(fn,map(char2num,'13579'))

#homework:
def prod(L):
    sum=1
    for x in L:
        sum=sum*x
    return sum
print(prod([3,5,7,9]))

def str2float(s):
    def fn(x,y):
        return x*10+y
    n=s.index('.')
    s1=list(map(int,[x for x in s[:n]]))
    s2=list(map(int,[x for x in s[n + 1:]]))
    return reduce(fn,s1) + reduce(fn,s2)/10**len(s2)
print(str2float("123.456")+str2float("0.01"))

#filter
#python内建的filter()函数用于过滤序列。
#filter()也接收一个函数和一个序列。和map()不同的是，
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
def isodd(n):
    return n%2==1
L=list(filter(isodd,[1,2,4,5,6,7,9,10]))
print(L)

#删除空字符串：
def not_empty(s):
    return s and s.strip()
L=list(filter(not_empty,['A','',None,'c',' ']))
print(L)

#构造素数列
def _odd_iter():
    n=1
    while(True):
        n=n+2
        yield n
def _not_divisible(n):  #返回用来检验x能否被n整除的函数
    return lambda x:x%n>0

#等价于：
# 
# def _not_divisible(n):
#     def f(x):
#           return x%n>0
#     return f
def primes():
    yield 2
    it = _odd_iter()#初始序列
    while(True):
        n=next(it)
        yield n
        it=filter(_not_divisible(n),it)

for n in primes():
    if n<1000:
        print(n,end=' ')
    else:
        break

#匿名函数
#计算f(x)=x^2时除了定义一个fx之外，还可以直接传入匿名函数:
print(list(map(lambda x: x*x,[1,3,5,7,9])))
#lambda x:x*x实际就是：
# def f(x):
#   return x*x
#同样，也可以把匿名函数作为返回值返回：
def build(x,y):
    return lambda: x*x+y*y

#装饰器
#由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量
#也能调用函数：
#函数对象有一个__name__属性，可以拿到函数的名字：
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' %func.__name__)
        return func(*args,**kw)
    return wrapper
@log
def now():
    print("2015-3-25")
f=now
print(now.__name__)
print(f.__name__)
#现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印
# 日志的decorator，可以定义如下
#把@log放到now()函数的定义处，相当于执行了语句:now=log(now)
#这时now变量指向了新的函数，即在log函数中返回的wrapper函数
now()

def log1(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator
@log1('execute')
def now1():
    print('2015-3-25')
#now1=log1('execute')(now1)
now1()
#以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
#因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw)
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper
#模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

#创建自己的模块时，要注意：

#模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
#模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是
# 在Python交互环境执行import abc，若成功则说明系统存在此模块。


