'''
1、range
Python2中range返回列表，Python3中range返回一个迭代值。
如果想要一个列表可以通过list函数
'''
a = range(5)
list(a)
#创建列表的另一种方法
testlist = [x+2 for i in range(5)]  #testlist=[2,3,4,5,6]

'''
2、map函数
 map函数会根据提供的函数对指定序列做映射
map(...)
	map(function, sequence[, sequence, ...]) -> list
function:是一个函数
sequence:是一个或多个序列,取决于function需要一个参数
返回值是一个list
参数序列中的每⼀个元素分别调⽤function函数，返回包含每次function函数
返回值的list
'''
##函数需要一个参数
map(lambda x: x*x, [1, 2, 3])
#结果为:[1, 4, 9]
#函数需要两个参数
map(lambda x, y: x+y, [1, 2, 3], [4, 5, 6])
#结果为:[5, 7, 9]
def f1( x, y ):
	return (x,y)
l1 = [ 0, 1, 2, 3, 4, 5, 6 ]
l2 = [ 'Sun', 'M', 'T', 'W', 'T', 'F', 'S' ]
l3 = map( f1, l1, l2 )
print(list(l3))
#结果为:[(0, 'Sun'), (1, 'M'), (2, 'T'), (3, 'W'), (4, 'T'), (5,'S')]

'''
3、filter函数
filter函数会对指定序列执⾏过滤操作
filter(...)
	filter(function or None, sequence) -> list, tuple, or string
function:接受一个参数，返回布尔值True或False
sequence:序列可以是str，tuple，list
filter函数会对序列参数sequence中的每个元素调⽤function函数，最后返回
的结果包含调⽤结果为True的元素
'''
filter(lambda x: x%2, [1, 2, 3, 4])
#[1, 3]
filter(None, "she")
#'she'

'''
4、reduce函数
reduce函数，reduce函数会对参数序列中元素进⾏累积
reduce(...)
	reduce(function, sequence[, initial]) -> value
function:该函数有两个参数
sequence:序列可以是str，tuple，list
initial:固定初始值
reduce依次从sequence中取一个元素，和上一次调⽤function的结果做参数
再次调⽤function。 第一次调用function时，如果提供initial参数，会以
sequence中的第一个元素和initial 作为参数调⽤function，否则会以序列
sequence中的前两个元素做参数调用function。 注意function函数不能为
None
'''
reduce(lambda x, y: x+y, [1,2,3,4])  #10
reduce(lambda x, y: x+y, [1,2,3,4], 5) #15  5作为x的固定值initial
reduce(lambda x, y: x+y, ['aa', 'bb', 'cc'], 'dd') #'ddaabbcc'

# 在Python3里,reduce函数已经被从全局名字空间中移除了, 它现在被放
# 置在fucntools模块用的话要先引用：  from functools import reduce

'''
5、sorted函数
sorted(...)
	sorted(iterable, cmp=None, key=None, reverse=False) --> new iterable

sorted([1,4,2,6,3,5]) #[1,2,3,4,5,6]
sorted([1,4,2,6,3,5],reverse = 1) #[6,5,4,3,2,1]
