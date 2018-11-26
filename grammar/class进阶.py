# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'miao'

class Person(object):
    """docstring for Person"""
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.weight = '100'

    def talk(self):
        print('Person is talking')
        print(self) #self：实例化地址id
        print(self.__class__)   
        print(self.__dict__)    
        #__dict__是用来存储对象属性的一个字典，其键为属性名，值为属性的值

class Chinese(Person):
    """docstring for Chinese"""
    def __init__(self, name,age,language):    #先继承，在重构
        super(Chinese, self).__init__(name,age) #继承父类的构造方法
        #也可以这么写 Person.__init__(self,name,age)
        self.language = language
        
    def said_name(self):
        print(self.name)

    def said_age(self):
        print(self.age)

    def said_weight(self):
        print(self.weight)  #直接调用继承属性

    def other_method(self):
        self.talk()
        self.said_name()    #类的内部方法互相调用

    def talk(self):
        print("Person's talk is too low,i will rewrite it!")
        #父类的方法重写
        
c = Chinese('Bill',22,'Chinese')
c.other_method()
c.said_age()
c.said_weight()
c.talk()
print c.language
a = Person('ling',30)
a.talk()

""""function之间互调"""

def tom():
    print('i am a tom cat')

def Jerry():
    tom()
    print('我要把楼上的tom方法调来用了')
Jerry()

"""
from module import function as fn
from module import class1, class2   # 先实例化，在调用类方法，或者直接继承，直接调用用self.fn()
from module import *
import module
from package.module import function1, function2

 """