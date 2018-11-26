#coding:utf-8
'''
生成器在函数中调用的方法
'''
def test():
	list = [[0,1,2],[3,4,5]]
	# list = [3,4,5]
	for item in list:
		yield {
		item[0],item[1],item[2]
		}
	# for item in list:
	# 	yield {
	# 	item
	# 	}


for item in test():
	print (item)
# 	
# print(test())