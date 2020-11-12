
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()

#第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

#第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

#第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

#以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。

#后面开始就是真正的代码部分。
#你可能注意到了，使用sys模块的第一步，就是导入该模块：

#import sys
# 导入sys模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能。

# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：

# 运行python3 hello.py获得的sys.argv就是['hello.py']；

# 运行python3 hello.py Michael获得的sys.argv就是['hello.py', 'Michael']。

# 最后，注意到这两行代码：
# if __name__=='__main__':
#     test()
# 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

# 我们可以用命令行运行hello.py看看效果：

# $ python3 hello.py
# Hello, world!
# $ python hello.py Michael
# Hello, Michael!
# 如果启动Python交互环境，再导入hello模块：

# $ python3
# Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import hello
# >>>
# 导入时，没有打印Hello, word!，因为没有执行test()函数。

# 调用hello.test()时，才能打印出Hello, word!：

# >>> hello.test()
# Hello, world!
# 作用域
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。

# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。

# private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：

# def _private_1(name):
#     return 'Hello, %s' % name

# def _private_2(name):
#     return 'Hi, %s' % name

# def greeting(name):
#     if len(name) > 3:
#         return _private_1(name)
#     else:
#         return _private_2(name)
# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：

# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()


# 7.1 输入输出：更漂亮的输出格式
year=2016
event='Referendum'
print(f'Results of the {year} {event}')
yes_votes=42_572_654
no_votes=43_132_495
percentage = yes_votes/(yes_votes+no_votes)
print('{} YES votes {:2.10%}'.format(yes_votes,percentage))
#当你不需要花哨的输出而只是想快速显示某些变量以进行调试时
# ，可以使用 repr() or str() 函数将任何值转化为字符串。
#str() 函数是用于返回人类可读的值的表示，而 repr() 是用于生成解释器
# 可读的表示（如果没有等效的语法，则会强制执行 SyntaxError）对于没有
# 人类可读性的表示的对象， str() 将返回和 repr() 一样的值。很多值使
# 用任一函数都具有相同的表示
# ，比如数字或类似列表和字典的结构。特殊的是字符串有两个不同的表示。
x=10*3.25
y=200*200
print(str('Hello world'))
print(repr('Hello world'))
s='The value of x is '+repr(x)+', and y is '+repr(y)+'...'
print(s)
l=list(range(100))
r=repr(l)
print(r)
print(str(1/7)[:4])
#7.1.1格式化字符串文字
import math
#格式化字符串字面值 （常简称为 f-字符串）能让你在字符串前加上 f 和
#F 并将表达式写成 {expression} 来在字符串中包含 Python 表达式的值
print(f'The value of pi is approximately {math.pi:.3f}.')
#在 ':' 后传递一个整数可以让该字段成为最小字符宽度。这在使列对齐时很有用。:
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}#define a dict
for name ,phone in table.items():
    print(f'{name:10}==>{phone:10d}')
#其他的修饰符可用于在格式化之前转化值。 '!a' 应用 ascii() ，'!s' 应用 str()，还有 '!r' 应用 repr():

#7.1.2. 字符串的 format() 方法
print('We are the {} who say "{}!"'.format('knights','Ni'))
print('{1} and {0}'.format('spam', 'eggs'))
#使用关键字参数：
print('This {food} is {adj}'.format(food='apple',adj='sweet'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
other='Georg'))
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

s=['apple','banana','orange','fruit']
for string in s:
    print(string.rjust(8))
# 7.2 读写文件
# open() 返回一个file object，最常用的有两个参数：open(filename,mode)
#mode: 'r':readonly    'w':writeonly  'a':attach to the end of file
#'r+':read and write    default:r

# import json
# f=open('jsonfile','r+')
# x=json.load(f)
# print(x)

# y=[e^2 for e in x if e%2==0]
# json.dump(y,f)
# 在文本模式下读取时，默认会把平台特定的行结束符 (Unix 上的 \n, Windows 上的 \r\n) 转换为 \n。
# 在文本模式下写入时，默认会把出现的 \n 转换回平台特定的结束符。
# 这样在幕后修改文件数据对文本文件来说没有问题，但是会破坏二进制数据例如 JPEG 或 EXE 文件中的数据。
# 请一定要注意在读写此类文件时应使用二进制模式。

#在处理文件对象时，最好使用 with 关键字。 
# 优点是当子句体结束后文件会正确关闭，即使在某个时刻引发了异常。 
# 而且使用 with 相比等效的 try-finally 代码块要简短得多:
with open('workfile','w') as f:
    f.write("Hello world!\n")
    f.write("Hi\n")
    f.write("This is a line\n")
    f.write("this is the end of the file\n")
    f.close()
#文件对象的方法：
#要读取文件内容，请调用 f.read(size)，它会读取一些数据并将其作为字符串
# （在文本模式下）或字节串对象（在二进制模式下）返回。 size 是一个可选的
# 数值参数。
#  当 size 被省略或者为负数时，将读取并返回整个文件的内容
# 当取其他值时，将读取并返回至多 size 个字符（在文本模式下）或 size 个字节（在二进制模式下）
# 如果已到达文件末尾，f.read() 将返回一个空字符串 ('')。
with open('workfile','r') as f:
    print(f.readline())
    print(f.readline())
#f.readline() 从文件中读取一行；换行符（\n）留在字符串的末尾
f=open('workfile')
for line in f:
    print(line,end='')
f.close()
#如果你想以列表的形式读取文件中的所有行，你也可以使用 list(f) 或 f.readlines()。
f=open('workfile')
lst=f.readlines()
print(lst)
f.close()

f=open('workfile')
print(list(f))
f.close()
#f.write(string) 会把 string 的内容写入到文件中，并返回写入的字符数。:
#在写入其他类型的对象之前，需要先把它们转化为字符串（在文本模式下）或者字节对象（在二进制模式下）:
f=open('workfile','r+')
value = ('the answer', 42)
s = str(value)
f.write(s)
f.close()
#要改变文件对象的位置，请使用 f.seek(offset, whence)。
#  通过向一个参考点添加 offset 来计算位置；参考点由 whence 参数指定。
#  whence 的 0 值表示从文件开头起算，1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。
#  whence 如果省略则默认值为 0，即使用文件开头作为参考点。
f = open('workfile1.txt', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)  # Go to the 6th byte in the file
f.read(1)
f.seek(-3, 2)# Go to the 3rd byte before the end
f.read(1)