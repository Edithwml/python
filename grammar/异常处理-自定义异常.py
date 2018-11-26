class ShortInputException(Exception):
	"""自定义异常的类"""
	def __init__(self, length,atleast):
		self.length = length
		self.atleast = atleast
		
def main():
	try:
		s = input('请输入：')
		#加入if判断条件，抛出异常
		if len(s)<3:
			raise ShortInputException(len(s),3)
	#捕获异常
	except ShortInputException as e:
		print('ShortInputException:输入的长度是 %d，长度至少为 %d'%(e.length,e.atleast))
	else:
		print('没有异常发生')
main()