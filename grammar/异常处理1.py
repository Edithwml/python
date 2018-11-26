#coding=utf-8

try:
    num = input("xxx:")
    int(num)
    #11/0
    #open("xxx.txt")
    #print(num)
    print("-----1----")

except (NameError,FileNotFoundError):
    print("如果捕获到异常后做的 处理....")
#通过as 变量名，保存异常信息
#python3捕获所有异常 except Exception ，python2 里面捕获所有异常 except :
except Exception as ret:
    print("如果用了Exception,那么意味着只要上面的except没有捕获到异常,这个except一定会捕获到")
    #打印保存的异常信息
    print(ret)
else:
    print("没有异常才会执行的功能")
#不管有没有异常都会执行finally
finally:
    print("------finally-----")

print("-----2----")
