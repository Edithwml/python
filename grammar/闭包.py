'''闭包
在函数内部再定义一个函数，里面的函数用到了外面函数的变量，
那么将这个函数以及用到的一些变量称之为闭包
'''
def test（num）：
	def test_in(num_in):
		return num + num_in
		#其实这里返回的就是闭包的结果
	return test_in

ret = test(100)  #定义一个变量来接收test_in，指向了一个函数体
ret() #ret指向函数test_in，通过调用函数的方法来调用内