'''
	语法糖
	装饰器简单来说就是打扮函数用的
'''

def w1(func):	#写上一个参数
	print("---正在装饰---")
	def inner():
		print("---正在验证权限---")
		func()	#把
 	return	inner
 #只要Python解释器执行到了这个代码就会自动进行装饰，而不是等到调用的时候才装饰
 @w1	#相当于fi = w1(f1)
 def f1():
 	print("---f1---")

 def f2():
 	print("---f2---")
'''
fi = w1(f1)	#指向了w1，接受了inner
f1()	#指向了inner，执行了func函数
'''
#在调用f1之前，已经进行装饰了
f1()


'''
	使用装饰器对无参数的函数进行装饰
'''
def func(functionName):
	print('---func1---')
	def func_in():	
		print('---func_in---1---')
		functionName()	
		print('---func_in---2---')
	print('---func2---')
	return func_in
@func   #相当于test = func(test)
def test():
	print('---test---')

test()

'''
	使用装饰器对有参数的函数进行装饰
'''
#简单示例1
def func(functionName):
	print('---func1---')
	def func_in(a,b):	#如果没有定义，会导致59行调用失败
		print('---func_in---1---')
		functionName(a,b)	#如果没有定义会导致56行调用失败
		print('---func_in---2---')
	print('---func2---')
	return func_in
@func   
def test(a,b):
	print('---test-a=%d,b=%d--'%(a,b))

test(11,22)

#优化
def func(functionName):
	print('---func1---')
	def func_in(*args,**kwargs):	#拆包、解包
		print('---func_in---1---')
		functionName(*args,**kwargs)	
		print('---func_in---2---')
	print('---func2---')
	return func_in
@func   
def test1(a,b):
	print('---test-a=%d,b=%d--'%(a,b))

@func   
def test2(a,b,c):
	print('---test-a=%d,b=%d,c=%c--'%(a,b,c))

test1(11,22)
test2(11,22,33)

'''
	装饰器对带有返回值的函数进行装饰
'''
def func(functionName):
	print('---func1---')
	def func_in():	
		print('---func_in---1---')
		#functionName()
		ret = functionName() #定义一个变量接受返回值 保存返回来的hahaha
		return ret	#把haha返回到99行处的调用
		print('---func_in---2---')
	print('---func2---')
	return func_in
@func
def test():
	print('---test---')
	return 'hahaha'	#使用装饰器调用的时候 实际返回给了functionName

ret = test()
print('test return value is %s'%ret)

'''
	通用的装饰器
'''
def func(functionName):
    def func_in(*args, **kwargs):
        print("-----记录日志-----")
        ret = functionName(*args, **kwargs)
        return ret

    return func_in

@func
def test():
    print("----test----")
    return "haha"
    #带有返回值的
@func
def test2():
    print("----test2---")
    #没有返回值的
@func
def test3(a):
    print("-----test3--a=%d--"%a)
    #带有参数的
ret = test()
print("test return value is %s"%ret)

a = test2()
print("test2 return value is %s"%a)


test3(11)
'''
	带有参数的装饰器，在原有装饰器的基础上，设置外部变量
'''
def func_arg(arg):
    def func(functionName):
        def func_in():
            print("---记录日志-arg=%s--"%arg)
            if arg=="heihei":
                functionName()
                functionName()
            else:
                functionName()
        return func_in
    return func

#1. 先执行func_arg("heihei")函数,这个函数return 的结果是func这个函数的引用
#2. @func
#3. 使用@func对test进行装饰
@func_arg("heihei")
def test():
    print("--test--")

#带有参数的装饰器,能够起到在运行时,有不同的功能
@func_arg("haha")
def test2():
    print("--test2--")

test()
test2()

