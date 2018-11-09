class Cat:
    """定义了一个Cat类"""

    #初始化对象
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
    
    #会默认打印出来
    #self接受的实际上是tom这个对象
    #所以这里的self.name，self.age取的实际上是Cat("汤姆", 40)的值
    #而不是__init__里面的
    def __str__(self):
        return "%s的年龄是:%d"%(self.name, self.age)

    #方法
    def eat(self):
        print("猫在吃鱼....")

    def drink(self):
        print("猫正在喝kele.....")

    def introduce(self):
        print("%s的年龄是:%d"%(self.name, self.age))

#创建一个对象
tom = Cat("汤姆", 40)

lanmao = Cat("蓝猫", 10)


print(tom)
print(lanmao)
