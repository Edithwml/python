#类对象
class Tool(object):

    #类属性
    num = 0

    #方法
    def __init__(self, new_name):
        #实例属性  self.name调用的是self，即接受的是tools对象
        self.name = new_name
        #对类属性+=1
        Tool.num += 1


tool1 = Tool("铁锹")  #实例对象
tool2 = Tool("工兵铲")
tool3 = Tool("水桶")

print(Tool.num) #打印3
 #实例属性:和具体的某个实例对象有关系，并且一个实例对象和另外一个实例对象是不共享属性的
 #类属性：类属性所属于类对象并且多个实例对象之间共享一个类属性
