# print absolute value of an integer
a = -100
if a>= 0:
    print(a)
else:
    print(-a)
    print("hello","world!")
print("hello world!")
#name=input("please input your name:")
#print("hello",name)
print("1024 * 768 = ",1024*768)
print(r'''line 1\nline2\n
line3\\\\''')  #r:取消转义,'''表示可多行输入
print('line1\nline2\nline3\n') 
print('''line1
line2
line3
''')
a=123
print(a)
a='abc'
print(a)      #动态语言
print(10/3)
print(10//3)
print(10%3)
x=b'ABC' #Python对bytes类型的数据用带b前缀的单引号或双引号表示：
print('ABC'.encode('ascii'))

#list 的使用
classmates=['Michael','bob','Tracy']
print(len(classmates),'\n',classmates[0],classmates[1],classmates[2])
print(classmates[-1])#最后一个元素
print(classmates[-2])#倒数第二个元素
classmates.append('Adam')#z追加到末尾
classmates.insert(1,'Jack')#插入元素到索引号位置
classmates.pop()#删除末尾元素
classmates.pop(1)#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates[1] = 'Sarah'#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
print(classmates.pop())
#list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
#list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
#tuple
#另一种有序列表叫元组：tuple。tuple和list非常类似，
#但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
classmates = ('Michael', 'Bob', 'Tracy')
#classmates[0]='a'  错误！

#if使用
age=3
if age>=18:
    print("adult")
elif age>=6:
    print("teenager")
else:
    print("kid")

s=1984
birth=int(s)
if birth<2000:
    print("00前")
else:
    print("00后")

#homework:
weight=80.5
height=1.75
BMI=weight/pow(height,2)
if BMI<18.5:
    print("too light")
elif BMI<25:
    print("normal")
elif BMI<28:
    print("too heavy")
elif BMI<32:
    print("fat")
else:
    print("too fat")

#the usage of for:
names=['a','b','c']
for name in names:
    print(name)
num=list(range(1,100,1))
#range()函数，可以生成一个整数序列，再通过list()函数可以转换为list
sum=0
for x in num:
    sum= sum+x
print (sum)

n=1
while n<=100:
    print(n)
    n+=1
    if n==10 and n==9 or n==2:
        break
print("END")

#dict and set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}#create a dictionary
print(d['Michael'])
print(d)
#把数据放入dict的方法，除了初始化时指定外，还可以通过key放入：
d['Adam'] = 67
#由于一个key只能对应一个value，
#所以，多次对一个key放入value，后面的值会把前面的值冲掉：
#如果key不存在，dict就会报错：
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print('Thomas' in d) #false
#二是通过dict提供的get()方法，如果key不存在，可以返回None，或
# 者自己指定的value：
print(d.get('Thomas')) #None
print(d.get('Bob'))  #75
print(1,2,sep=' ',end='\n\n')
s=set([1,2,3])#类似于集合,无序，无重复元素
s.add(4)
print(s)
s.remove(4)
print(s)

s1=set([1,2,3])
s2=set([1,3,4])
#a=input()
#s2.add(int(a))
print(s2)
print(int('100',base=2))
a="abc"
print(a.replace('a','A'))
print(a)

#homework
print('\n\n')
dict={'a':(1,2,3),'b':(1,[2,3])}
s=set([1,2,3])
print(dict)
print(s)

#function
from add import add 

def minus(x,y):
    return x-y

print(add(3,5))
print(minus(3,5))
#如果想定义一个什么事也不做的空函数，可以用pass语句：
def f(x):
    pass
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#让我们修改一下my_abs的定义，对参数类型做检查，只允许
#整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：

#返回多个值
import math
def move(x,y,step,angle=0):
    nx = x + step *math.cos(angle)
    ny= y - step * math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)
#但这只是假象，python函数返回的仍然是单一值：
r=move(100,100,60,math.pi/6)
print(r)#(151.96,70.0)

def root(a,b,c):
    if b*b>=4*a*c:
        res1=(-b+math.sqrt(b*b-4*a*c))/2/a
        res2=(-b-math.sqrt(b*b-4*a*c))/2/a
        return res1,res2
    else:
        return None,None

print(root(1,2,1))

#函数的参数
#的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以
# 使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理
# 复杂的参数，还可以简化调用者的代码。
#默认参数
#默认参数最大的好处是降低调用的难度

def power(x,n=2):
    s=1
    while n>0:
        n=n-1
        s=s*n
    return s
print(power(5,3),power(5))
def enroll(name,gender,age=6,city="peking"):
    print("name:",name)
    print("gender:",gender)
    print("age:",age)
    print("city:",city)
enroll(123,0)
#可见，默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现
#无论是简单调用还是复杂调用，函数只需要定义一个
#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下
def add_end(L=[]):
    L.append('end')
    return L
print(add_end([1,2,3]))#当你正常调用时，结果似乎不错
print(add_end())#当你使用默认参数调用时，一开始结果也是对的
print(add_end())#再次调用时就不对了
#原因解释如下：

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容
#则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end_s(L=None):
    if L is None:#or: if L == None
        L = []
    L.append('END')
    return L
print(add_end_s())
print(add_end_s())

#可变参数
def calc(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc([1,2,3]))
print(calc((1,3,5,7)))
#使用可变参数，在参数名前加星号，可简化调用
def calc2(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc2(1,2))
print(calc2(0))
nums=[1,2]
print(calc2(*nums))

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装
# 为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些
# 关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name,age,**kw):
    if 'city' in kw:#检查是否有某参数
        pass
    if 'job' in kw:
        pass
    print('name:',name,'age:',age,'other:',kw)
person('Michael',30)
person('Michael',30,city='Beijing',job='engineer')
#关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们
#保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，
# 我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填
# 项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。
extra = {'city': 'Beijing', 'job': 'Engineer'}
#person('Michael',30，city=extra['city'],job=extra['job'])
person('Michael',30,**extra)
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和
#job作为关键字参数。这种方式定义的函数如下
def person2(name , age, *, city, job):
    print(name, age, city, job)
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。

#以及调用函数时如何传入可变参数和关键字参数的语法：

#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：
# func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：
# func(**{'a': 1, 'b': 2})

#用list，tuple->*参数（可变参数）时，调用时变量前面加星号
#用dict->**参数（关键字参数）时，调用时变量前面加两个星号

#尾递归优化
def fact(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
#所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。