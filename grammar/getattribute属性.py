'''
__getattribute__属性
'''

class Itcast(object):
	"""docstring for Itcast"""
	def __init__(self, subject1):
		self.subject1 = subject1
		self.subject2 = 'cpp'
	#属性访问时拦截器，打log
	def __getattribute__(self,obj):
		print("===1>%s"%obj)
		if obj == 'subject1':
			print('log subject1')
			return 'redirect python'
		else:	#测试时注释掉这2行，将找不到subject2
			temp = object.__getattribute__(self,obj)
			print('====2>%s'%str(temp))
			return temp
	def show(self):
		print('this is Itcast')

s = Itcast("python")
print(s.subject1)
print(s.subject2)

s.show()
'''
打印结果：
===1>subject1
log subject1
redirect python
===1>subject2
====2>cpp
cpp
===1>show
====2><bound method Itcast.show of <__main__.Itcast object at 0x0000000003D66320>>
this is Itcast
'''

#s.show()
#这个方法的执行实际分两步走：
#1. 先获取show属性对应的结果，应该是一个方法
#2. 方法()
#所以把return temp 这句话注释掉的时候，返回的是None，再执行None()就会报错
'''
注释后打印结果：
===1>subject1
log subject1
redirect python
===1>subject2
====2>cpp
None
===1>show
====2><bound method Itcast.show of <__main__.Itcast object at 0x00000000036D6320>>

Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/getattribute属性", line 23, in <module>
    s.show()
TypeError: 'NoneType' object is not callable
'''

'''
__getattribute__的坑
'''
class Person(object):
	def  __getattribute__(self,obj):
		print("---test---")
		if obj.startwith("a"):
			return "hahaha"
		else:
			return self.test
	def test(self):
		print("heihei")
t.Person()
t.a #返回hahaha
t.b #会让程序死掉
	#原因是：当执行t.b时，会调用Person类中定义的__getattribute__方法
	#if条件不满足，所以程序else里面的代码，即return self.test
	#self.test的值返回，那么首先要获取self.test的值，因为self此时就执行t
	#t.test 此时要获取t这个对象的test属性，那么就会跳转到__getattribute__方法
	#生成了递归调用，由于这个递归过程中，没有判断什么时候退出，所以这个程序就进入了死循环
	#每次调用函数，就需要保存一些数据，那么随着调用的次数越来越多，最终程序就崩了
	#
	#注意：以后不要在__getattribute__方法中调用self.XXX



