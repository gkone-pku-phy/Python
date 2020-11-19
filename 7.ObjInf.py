#首先，我们来判断对象类型，使用type()函数：
#基本类型都可以用type()判断：
#如果一个变量指向函数或者类，也可以用type()判断：
print(type(123),'\n',type('str'),type('None'))
print(type(abs))
#但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123)==int)
#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
    pass
print(type(fn)==types.FunctionType,type(abs)==types.BuiltinFunctionType,type(lambda x:x) == types.LambdaType,type((x for x in range(10))) == types.GeneratorType,
sep='\n')
#使用isinstance()
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
class mydog(object):
    def __len__(self):
        return 100
print(len(mydog()))
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=MyObject()
a=Animal()
d=Dog()
h=Husky()
print(isinstance(h,Husky),
isinstance(h,Dog),
isinstance(h,Animal),
isinstance(d,Husky),
isinstance(1,int),
isinstance([1,2,3],(list,tuple)),sep='\n')
setattr(obj,'y',10)
print(
hasattr(obj,'x'),
obj.x,
hasattr(obj,'y'),
getattr(obj,'y'),
obj.y,
sep='\n')
#如果试图获得不存在的属性，会抛出AttributeError错误:
#print(getattr(obj,'z'))
#也可以获得对象的方法：
print(
    hasattr(obj,'power'),
    getattr(obj,'power'),
    getattr(obj,'power')(),
    sep='\n'
)

#实例属性和类属性
#由于python是动态语言，根据类创建的实例可以任意绑定属性
#给实例绑定属性的方法是通过实例变量，或者通过self变量：
class s(object):
    def __init__(self,name):
        self.name=name
s1=s('BoB')
s.score=90
#但是如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class stu(object):
    name='Student'
#当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下
s=stu()
print(s.name,stu.name)# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
s.name='Michael'# 给实例绑定name属性
print(s.name)# 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
print(stu.name)# 但是类属性并未消失，用Student.name仍然可以访问
del s.name# 如果删除实例的name属性
print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了

#e.g. 添加类属性显示一创建的学生对象个数:
class student(object):
    num=0
    def __init__(self,name):
        student.num+=1
        student.__name=name
stu1=student('A')
stu2=student('B')
print(student.num)