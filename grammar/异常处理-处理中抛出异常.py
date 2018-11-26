class Test(object):
	"""docstring for Test"""
	def __init__(self, switch):
		self.switch = switch
		
	def calc(self,a,b):
		try:
			return a/b
		except Exception as e:
			if self.switch = True
			print('捕获已开启,已经捕获到了异常，信息如下')
			print(e)
		else:
			#重新抛出这个异常，此时就不会异常处理给捕获到，从而触发默认的异常处理
			raise		
a = Test(True)
a.calc(11,0)

print('---------华丽的分割线----------')

a = Test(False)
a.calc(11,0)