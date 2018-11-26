#生成器generator：在Python中一遍循环一遍计算的机制，称为生成器

'''
创建生成器方法1
'''
L = [x*2 for x in range(4)]
#打印出来[0, 2, 4, 6]
G = (x*2 for x in range(4))
#打印出<generator object <genexpr> at 0x0000000003B9FB88>
#一个是列表一个是生成器，生成器可以用next()函数获得生成器的下一个返回值
#生成器把计算的方法保存了，需要用的时候就生成一个，节省了占用内存
 
'''
创建生成器方法2
'''

#在没有第三个变量的情况交换两个变量的值
a = 9
b = 10
#解决过程
a = a + b
b = a - b
a = a - b
#打印结果：a = 10  b = 9
  
#最简单的方法
#a,b = b ,a

#斐波拉契数列：1,1,2,3,5,8,13,21,34，...
 
def createNum():
	a,b = 0,1
	for i in range(5):
		print b
		a,b = b,a+b
		
createNum()

#用生成器的方法
#只要加了yield的函数就变成了生成器
def createNum():
	print('---start---')
	a,b = 0,1
	for i in range(5):
		print("---1---")
		yield b  #遇到yield时会直接把后面的值返回，程序就中断了
		print("---2---")
		a,b = b,a+b
		print("---3---")
	print('---stop---')
createNum()	#输出结果：<generator object createNum at 0x0000000003BCD990>
			#不能采用这种方法调用生成器
a = createNum()  #找一个变量来接收生成器对象
ret = next(a)   #让这个生成器对象开始执行，如果是第一次执行，那么从createNum开始
				#如果是之前已经执行过了，那么就从上一次停止的位置开始执行
ret = next(a)  
ret = next(a)
ret = next(a)
ret = next(a)
ret = next(a)
ret = next(a)
ret = next(a)

'''
我们在循环过程中不断调用yield就不会中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来
我们基本上不会用next()来获取下一个返回值，而是直接用for循环来迭代
'''

#先创建一个生成器对象
a = createNum()
#再设置一个循环，打印出来哦
for num in a:
	print num
	
#也可以采用next
ret = a.__next__()  #等价于next(a)
print(ret)

