coding:utf-8
'''
装饰器decorator
1. 引入日志
2. 函数执行时间统计
3. 执行函数前预备处理
4. 执行函数后清理功能
5. 权限校验等场景
6. 缓存

装饰器函数其实是这样一个接口约束，它必须接受一个callable对象作为参数，
然后返回一个callable对象。在python中一般callable对象都是函数，但是也有例外。
只要某个对象重写了__call__()方法，那么这个对象就是callable的
'''
class Test():
	def __call__(self):
		print('call me!')

t = Test()
t()	#call me

#类装饰器
class Test(object):
	def __init__(self,func):
		print("---初始化---")
		print("func name is %s"%func.__name__)
		self.__func = func

	def __call__(self):
		print("---装饰器中的功能---")
		self.__func()

@Test
def test():
	print("---test---")
test()

#说明
#1.当用Test来装作装饰器对test函数进行装饰的时候，首先会创建Test的实例对象
#	并且会吧Test这个函数名当做参数传递到__init__方法中
#	即在__init__方法中的func变量指向了test函数体
#	
#2.test函数相当于指向了Test创建出来的实例对象
#
#3.当在使用test()进行调用时，会调用这个对象的__init__()
#
#4.为了能够在__call__方法中调用原来test指向的函数体，所以在__init__方法将__func重新指向test
#	所以才有了在self.__func = func 这句代码，从而在调用__call__方法中能够调用test

'''
运行结果如下：
---初始化---
func name is test
---装饰器中的功能---
----test---
'''