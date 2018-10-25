'''
生成器用法-完成多任务:看上去一起执行的东西就叫多任务
多任务中有协程、进程、线程
'''

def test1():
	while True:
		print("---1---")
		yield None	#执行到这里就中断

def test2():
	while True:
		print("---2---")
		yield None

t1 = test1()
t2 = test2()
while True:
	t1.__next__()	#不断的循环调用test1函数
	t2.__next__()	

#设置了三个循环实现了快速的调用
#在速度很快的情况下看起来就是不断的刷新，打飞机游戏控制图片的效果就可以采用这种方法实现
