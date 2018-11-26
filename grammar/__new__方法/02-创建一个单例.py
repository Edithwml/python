#单例：自己一个人
#所谓单例就是不管创建多少次，实际只有一个对象
class Dog(object):

    __instance = None
    #只创建一个单例
    def __new__(cls):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #return 上一次创建的对象的引用
            return cls.__instance

a = Dog()
print(id(a))
b = Dog()
print(id(b))  #a和b的id都是一样的，因为__new__只创建了一个单例
