'''
Garbage collection(GC垃圾回收机制)
Python采用的是引用计数机制为主，标记-清除（ruby的）和分代收集两种机制为辅的策略
'''

#引用计数能解决大部分占用内存的问题
#但对于相互引用的情况,引用计数搞不懂
import gc

class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(hex(id(self))))

def f2():
    while True:
        c1 = ClassA()	
        c2 = ClassA()	#指定对象加1
        c1.t = c2  #指定对象加1，加上C2的计数，一共是2
        c2.t = c1  
        del c1 	
        del c2 	#减1，还会剩1 
        #互相引用没法清除占用内存，进入while循环，占用内存不断增大，程序就不稳定
        gc.collect()

gc.disable()

f2()   
#隔代回收(Generational GC)处理了互相引用的问题
#python使用一种不同的链表来持续追踪活跃的对象