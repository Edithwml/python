#Python ：即支持面向过程也支持面向对象
#面向过程：根据业务逻辑从上到下写代码
#面向对象：将对象与函数绑定在一起，进行封装，
#这样能够快速的开发程序，减少了重复代码的重写过程
#面向对象的三个基本要素：继承、多态、封装
#1.多态：定义的时候，不确定调用哪个类中的方法，而是等到真的调用的之后才确定
#即定义时不确定而是运行时确实这就成为多态
#2.继承：子类继承父类
#3.封装：把函数和全局变量找个对象封装在一个，这个东西叫做对象
class Dog(object):
    def print_self(self):
        print("大家好,我是xxxx,希望以后大家多多关照....")

class Xiaotq(Dog):
    def print_self(self):
        print("hello everybody, 我是你们的老大,我是xxxx")


def introduce(temp):
    temp.print_self() #多态，调用的时候才知道要执行哪一个


dog1 = Dog()
dog2 = Xiaotq()

introduce(dog1)
introduce(dog2)
