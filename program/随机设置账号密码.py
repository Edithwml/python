import random
import string
'''随机设置账号密码'''
def randpwd():
    a =''.join(string.digits+ string.letters)   #数字，大写加小写
    b =(random.sample(string.digits,1) +\
        random.sample(string.lowercase,1) +\
        random.sample(string.uppercase,1))
    """
    random.random() 生成一个0到1的随机浮点数
    random.uniform(a,b) 生成a<=n<=b的随机浮点数
    random.randint(a,b) 生成a<=n<=b的随机整数
    random.randrange([start], stop[, step]) 从指定范围内，按指定基数递增的集合中 获取一个随机数
    random.choice(sequence) 序列中获取一个随机元素,sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence
    random.shuffle(x) 打乱
    random.sample(sequence, k)  从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列
    """
    c = random.shuffle(b)   #打乱前三位
    d = random.sample(b,3)  #选取打乱前三位样品
    password = ''.join(d+ random.sample(a,random.randint(5,13)))    #结果
    return password

def account():
    a = string.letters
    b = string.digits
    c = ''.join(a+ b)
    d = random.sample(a,1)
    e = random.sample(b,1) + random.sample(c,random.randint(2,10))
    f = random.shuffle(e)
    account = ''.join(d+e)
    return account

if __name__ == '__main__':
    m = randpwd()
    k = account()
    print '密码的长度为%d'%len(m),m
    print '账号的长度为%d'%len(k),k