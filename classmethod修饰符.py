class A(object):
    """classmethod 修饰符对应的函数不需要实例化，不需要 self 参数，
        但第一个参数需要是表示自身类的 cls 参数，
        可以来调用类的属性，类的方法，实例化对象等。"""
        
    #属性默认为是类属性（可以直接被类本身调用）
    num  = "类属性"

    #实例化方法(必须实例化类之后才能被调用)
    def func1(self):    #self：表示实例化类后的地址id
        print("func1")
        print(self)

    #类方法（不需要实例化类就可以被类本身调用）
    @classmethod
    def  func2(cls):    #cls: 表示没有被实例化类的本身
        print("func2")
        print(cls)
        print(cls.num)
        cls().func1() #调用func1方法

    #不传递默认self参数的方法（该方法也是可以调用的，但是这样做不标准
    def func3():
        print("func3")
        print(A.num)    #属性是可以直接用类本身调用的

#A.func1()会报错：因为func1调用时需要默认传递实例化类后地址id参数，如果不实例化是无法调用的
B = A()     #将类实例化
B.func1()  
A.func2()   #不需要实例化
A.func3()