'''
__getattribute__����
'''

class Itcast(object):
	"""docstring for Itcast"""
	def __init__(self, subject1):
		self.subject1 = subject1
		self.subject2 = 'cpp'
	#���Է���ʱ����������log
	def __getattribute__(self,obj):
		print("===1>%s"%obj)
		if obj == 'subject1':
			print('log subject1')
			return 'redirect python'
		else:	#����ʱע�͵���2�У����Ҳ���subject2
			temp = object.__getattribute__(self,obj)
			print('====2>%s'%str(temp))
			return temp
	def show(self):
		print('this is Itcast')

s = Itcast("python")
print(s.subject1)
print(s.subject2)

s.show()
'''
��ӡ�����
===1>subject1
log subject1
redirect python
===1>subject2
====2>cpp
cpp
===1>show
====2><bound method Itcast.show of <__main__.Itcast object at 0x0000000003D66320>>
this is Itcast
'''

#s.show()
#���������ִ��ʵ�ʷ������ߣ�
#1. �Ȼ�ȡshow���Զ�Ӧ�Ľ����Ӧ����һ������
#2. ����()
#���԰�return temp ��仰ע�͵���ʱ�򣬷��ص���None����ִ��None()�ͻᱨ��
'''
ע�ͺ��ӡ�����
===1>subject1
log subject1
redirect python
===1>subject2
====2>cpp
None
===1>show
====2><bound method Itcast.show of <__main__.Itcast object at 0x00000000036D6320>>

Traceback (most recent call last):
  File "C:/Users/Administrator/Desktop/getattribute����", line 23, in <module>
    s.show()
TypeError: 'NoneType' object is not callable
'''

'''
__getattribute__�Ŀ�
'''
class Person(object):
	def  __getattribute__(self,obj):
		print("---test---")
		if obj.startwith("a"):
			return "hahaha"
		else:
			return self.test
	def test(self):
		print("heihei")
t.Person()
t.a #����hahaha
t.b #���ó�������
	#ԭ���ǣ���ִ��t.bʱ�������Person���ж����__getattribute__����
	#if���������㣬���Գ���else����Ĵ��룬��return self.test
	#self.test��ֵ���أ���ô����Ҫ��ȡself.test��ֵ����Ϊself��ʱ��ִ��t
	#t.test ��ʱҪ��ȡt��������test���ԣ���ô�ͻ���ת��__getattribute__����
	#�����˵ݹ���ã���������ݹ�����У�û���ж�ʲôʱ���˳��������������ͽ�������ѭ��
	#ÿ�ε��ú���������Ҫ����һЩ���ݣ���ô���ŵ��õĴ���Խ��Խ�࣬���ճ���ͱ���
	#
	#ע�⣺�Ժ�Ҫ��__getattribute__�����е���self.XXX



