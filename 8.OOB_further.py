#数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。在Python中，面向对象还有很多高级特性，允许我们写出非常强大的功能。

#我们会讨论多重继承、定制类、元类等概念。
#使用__slots__

#正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
    pass
s=Student()
s.name='Michael'
print(s.name)

#给实例绑定方法：
def set_age(self,age):
    self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定方法
s.set_age(25)
print(s.age)
#但是，给一个实例绑定的方法，对另一个实例是不起作用的.为了给所有实例都绑定方法，可以给class绑定方法：给class绑定方法后，所有实例均可调用.通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
def set_score(self,score):
    self.score=score
Student.set_score=set_score
#但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

#使用@property
#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
#但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！

#还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class stu(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value<0 or value>100:
            raise ValueError('Score must between 0 and 100!')
        self._score=value
#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
s=stu()
s.score=60 #ok,实际转化为s.set_score(60)
s.score #ok,实际转化为s.get_score()
#s.score=9999 ValueError

#注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

#还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class people(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self,value):
        self._birth=value
    @property
    def age(self):
        return 2015-self._birth
     #上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。   
#@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,num):
        self._width=num
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,num):
        self._height=num
    @property
    def resolution(self):
        return self._height*self._width

#多继承
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。
#class Flyable(object):
#   pass
#class Bat(Mammal, Flyable):
#    pass
#MixIn
#在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
#MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
#Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。
#比如，编写一个多进程模式的TCP服务，定义如下：
# class MyTCPServer(TCPServer,ForkingMixIn):
#     pass
#编写一个多线程模式的UDP服务，定义如下：
# class MyUDPServer(UDPServer,ThreadingMixIn):
#     pass
#如果你打算搞一个更先进的协程模型，可以编写一个CoroutineMixIn：
# class MyTCPServer(TCPServer, CoroutineMixIn):
#     pass
#这样一来，我们不需要复杂而庞大的继承链，只要选择组合不同的类的功能，就可以快速构造出所需的子类。

#定制类
#看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。

#__slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。

#除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
class Student2(object):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return 'Student object (name:%s)' % self.name
    __repr__=__str__

print(Student2('Michael'))
#打印出一堆<__main__.Student object at 0x109afb190>，不好看。

#怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

#__iter__
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)

#__getitem__
#Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素.要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib2(object):
    def __getitem__(self,n):
        a,b=1,1
        for x in range(n):
            x=x
            a,b=b,a+b
        return a
f=Fib()
#print(f[0])
#总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
#__getattr__
#正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类中存在name属性，那么调用name属性没问题，但是调用不存在的score属性就有问题了
#要避免这个错误，除了可以加上一个score属性之外，python还有一个机制，就是写一个__getattr__方法，动态返回一个属性。
# class stu(object):
#     def __init__(self):
#         self.name='Michael'
#     def __getattr__(self,attr):
#         if attr=='score':
#             return 99

#__call__
#一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
#任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例:
#class Student(object):
    # def __init__(self, name):
    #     self.name = name

    # def __call__(self):
    #     print('My name is %s.' % self.name)

#枚举类
#当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份.好处是简单，缺点是类型是int，并且仍然是变量。

#更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例。Python提供了Enum类来实现这个功能：
from enum import Enum
Month=Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
for name,member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
#value属性则是自动赋给成员的int常量，默认从1开始计数。
#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum,unique

@unique
class Weekday(Enum):
    Sum=0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6    
    #@unique装饰器可以帮助我们检查保证没有重复值。

#访问这些枚举类型可以有若干种方法：
day1=Weekday.Mon