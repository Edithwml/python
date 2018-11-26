class Dog(object):
    def __init__(self):
        print("----init方法-----")

    def __del__(self):
        print("----del方法-----")

    def __str__(self):
        print("----str方法-----")
        return "对象的描述信息"

    def __new__(cls):#cls此时是Dog指向的那个类对象

        #print(id(cls))

        print("----new方法-----")
        return object.__new__(cls)


#print(id(Dog))   跟上面打印的id一样

xtq = Dog()
#相当于要做3件事：
#1.调用__new__方法来创建对象，然后找一个变量来接收__new__返回值，这个返回值表示_创建出来的的对象的引用
#2.__init__(刚刚创建出来的对象的引用)
#3.返回对象的引用
#__new__方法只负责创建对象
#__init__方法只负责初始化对象
