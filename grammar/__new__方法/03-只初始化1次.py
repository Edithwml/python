#__new__方法负责创建对象
#__init__方法只负责初始化对象
class Dog(object):

    __instance = None
    #定义类属性
    __init_flag = False
    #因为实例方法接收了一个参数，这里也加个参数name接收一下，不写的话会报错
    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            #return 上一次创建的对象的引用
            return cls.__instance
    #加if判断只初始化一次对象
    def __init__(self, name):
        if Dog.__init_flag == False:
            self.name = name
            Dog.__init_flag = True


a = Dog("旺财")
print(id(a))
print(a.name)
#打印旺财
b = Dog("哮天犬")
print(id(b))
print(b.name)
#打印哮天犬