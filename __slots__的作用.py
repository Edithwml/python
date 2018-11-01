'''
	为了达到限制的目的，Python允许在定义class的时候，定义一个特使的__slots__变量，来限制该class实例添加属性
	使用__slots__要注意，__slots__定义的属性仅对当前的类实例起作用，
	对继承的子类是不起作用的
'''
class Person(object):
	__slots__ = ("name")

p = Person()
p.name = "xiaoming"
p.age = 10   #会报错
