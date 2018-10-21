#coding=utf-8
import time
"""定义一个计时装饰器用来计时函数执行时间"""


def timer(func):
    """*args,**kwargs分别表示位置参数，关键字参数"""
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        stop=time.time()
        print(stop-start)
        return result
    return wrapper


@timer
def test(parameter,firstname):
    time.sleep(2)
    print("test is running!" + parameter + "." + firstname + "!")
    return "returned value"
test("jerry", "wind")


"""下面我们讲下类方法装饰器怎么写"""


def decorator(func):
    """在wrapper里面传入参数instance，对于类方法来说，都会有一个默认的参数self
    ，都会有一个默认的参数self，它实际表示的是类的一个实例，
    所以在装饰器的内部函数wrapper也要传入一个参数 """
    def wrapper(instance):
        start_time = time.time()
        func(instance)
        end_time = time.time()
        print(end_time - start_time)
    return wrapper


class Method(object):

    @decorator
    def func(self):
        time.sleep(0.8)

p1 = Method()
p1.func() # 函数调用


"""接下来将如何实现多装饰器装饰函数"""


def deco01(func):
    def wrapper(*args, **kwargs):
        print("this is deco01")
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
        print("deco01 end here")
    return wrapper


def deco02(func):
    def wrapper(*args, **kwargs):
        print("this is deco02")
        func(*args, **kwargs)

        print("deco02 end here")
    return wrapper


@deco01
@deco02
def func(a, b):
    print("hello，here is a func running")
    time.sleep(1)
    print("result is %d" % (a+b))


"""结果预期你将会发现，装饰器执行完成顺序是从近到远先func函数再向外像盒子一样一层层包裹起来，
先装饰完的是deco02,再是dec01完成"""
if __name__ == '__main__':
    f = func
    f(3, 4)
