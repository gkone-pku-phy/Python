std1={'name':'Michael','score':98}
std2={'name':'Bob','score':81}
def print_score(std):
    print('%s:%s' % (std['name'],std['score']))
print_score(std1)
#如果采用面向对象的程序设计思想，我们首选思考的不是
# 程序的执行流程，而是Student这种数据类型应该被视为
# 一个对象，这个对象拥有name和score这两个属性（Property）。
# 如果要打印一个学生的成绩，首先必须创建出这个学生对
# 应的对象，然后，给对象发一个print_score消息
# ，让对象自己把自己的数据打印出来。
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name,self.score))
    
    def get_grade(self):
        if self.score>=90:
            return 'A'
        elif self.score>=60:
            return 'B'
        else:
            return 'C'
    
bart=Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
#class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
#定义好了student类，就可以根据student类创建出student的实例，创建实例是通过类名加（）实现的：
#bart=Student()
# //TypeError:__init__() missing 2 required positional arguments : 'name' and 'score'
#可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性:
#bart.name=' '
#由于类可以起到模板的作用，因此可以在创建实例的时候，把我们认为必须绑定的属性强制填写进去

#注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。

#但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：

#   访问限制：
#在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

#但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：

#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：

class Student1(object):

    def __init(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s： %s' %(self.__name,self.__score))
    
#改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量._name和实例变量.__score了。这样就确保了外部代码不能随意获取对象内部的状态，这样通过访问限制的保护，代码更加健壮。但要从外部获取name 和score怎么办?可以给Student类增加get_name 和get_score的方法：
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

#需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
#bart._Student__name
#最后注意下面的这种错误写法：

#>>> bart = Student('Bart Simpson', 59)
#>>> bart.get_name()
#'Bart Simpson'
#>>> bart.__name = 'New Name' # 设置__name变量！
#>>> bart.__name
#'New Name'
#表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：

class stu(object):
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def set_name(self,name):
        self.__name=name

    def set_gender(self,gender):
        self.__gender=gender
    def get(self):
        print(self.__name,self.__gender)

l=stu('hello','nogender')
print(l.get())