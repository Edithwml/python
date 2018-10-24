作用域:LEGB原则

locals -> enclosing function-> globals -> builtins
locals, 当前所在命名空间（函数、模块），函数的参数也属于命名空间内的变量
enclosing, 外部嵌套函数的命名空间（闭包中常见）
def fun1():
	a = 10
	def fun2():
		# a位于外部嵌套函数的命名空间
		print(a)
globals，全局变量，函数定义所在模块的命名空间
 
 a = 1
 def fun():
 	#需要通过global指令来声明全局变量
 	global a
 	#修改全局变量而不是创建新的locals变量
 	a = 2
builtins, 内键,系统定义好了的
查看内键的方法:dir(__builtin__)

