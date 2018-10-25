#python是动态语言：可以在运行过程中修改代码

'''
	运行的过程中给对象添加属性
'''
class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge


laowang = Person("老王", 10000)
print(laowang.name)
print(laowang.age)
laowang.addr = "北京...."
print(laowang.addr)	#给对象添加属性，只影响当前对象


laozhao = Person("老赵", 18)
#print(laozhao.addr)	#会报错，laozhao这个对象没有addr的属性

Person.num = 100   #给类添加属性
print(laowang.num)	#实例化对象正常调用
print(laozhao.num)

'''
	运行的过程中给类添加函数
'''

class Person(object):
    def __init__(self, newName, newAge):
        self.name = newName
        self.age = newAge
    
    def eat(self):
        print("-----%s正在吃----"%self.name)


def run(self):
    print("-----%s正在跑----"%self.name)


p1 = Person("p1", 10)
p1.eat()
p1.run = run  #指向run函数
p1.run()#虽然p1对象中 run属性已经指向了run函数,,,但是这句代码还不正确
        #因为run属性指向的函数 是后来添加的,几p1.run()的时候,并没有把p1当做第
        #1个参数,导致了第10行的函数调用的时候, 出现缺少参数的问题


'''
#正确的操作方法
import types

types.MethodType(function,instance)  #该方法默认给一个对象添加属性

p1.run = types.MethodType(run,p1)
p1.run()

#正常操作是赋给一个变量
xxx =types.MethodType(run,p1)  
xxx()       
#types.MethodType(run,p1) 使用该方法的时候会导致run后面再调用的时候，会先默认传入参数p1
'''


'''
	运行过程中给类添加静态方法和类方法
'''
@staticmethod
def test():  #静态方法里面可以不用写参数
	print('---static method---')

Person.test = test  #只需用类名.XX指向test
Person.test()	#调用


@classmethod   #类方法
def printNum(cls):
	print('---class method---')

Person.printNum = printNum	#和静态方法添加的方式一样
Person.printNum()