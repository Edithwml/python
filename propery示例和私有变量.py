#属性property的作用:相当于把方法进行了封装, 开发者在对属性设置数据的时候更方便
class Test(object):
	def __init__(self):
		self.__num = 100   #私有变量:私有变量是以下划线开头的
						   #想要调用私有变量，可以通过set和get方法
						   #其实python是通过名字重整（name mangling）以防止类意外重写基类的方法或者属性，
						   #例如_class__object机制就可以访问private了
						   #t.__Test__num	这时候调用就不会报错

	#设置set和get方法调用私有变量
	def setNum(self, newNum):
        print("----setter----")
        self.__num = newNum

    def getNum(self):
        print("----getter----")
        return self.__num

     #设置属性：相当于把方法进行了封装
     num = property(getNum, setNum)

t = Test()
# print(t.__num)	#直接掉用是私有变量会报错
# t.__num = 200	#不能直接对私有变量赋值

#print(t.getNum())  #打印出100
#t.setNum(50)	#调用set方法
#print(t.getNum())	#打印出50
#
print("-"*50)

t.num = 200 #相当于调用了 t.setNum(200)

print(t.num) #相当于调用了 t.getNum()

#注意点:
#t.num 到底是调用getNum()还是setNum(),要根据实际的场景来判断,
#1. 如果是给t.num赋值 那么一定调用setNum()
#2. 如果是获取t.num的值,那么就一定调用getNum()


'''
propery的另一种用法:@property 和 @name.setter
'''
class Test(object):
    def __init__(self):
       self.__num = 100

    @property
    def num(self):
        print("----getter----")
        return self.__num

    @num.setter
    def num(self, newNum):
        print("----setter----")
        self.__num = newNum

t = Test()

t.num = 200 #相当于调用了 t.setNum(200)

print(t.num) #相当于调用了 t.getNum()
