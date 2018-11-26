'''*args是非关键字参数，用于元组，**kw是关键字参数，用于字典

举例：

1.*args
'''
def tupleArgs(arg1, arg2= 'B', *arg3):
    print('arg 1:%s ' % arg1)
    print('arg 2:%s ' % arg2)
    for eachArgNum in range(len(arg3)):
        print('the %d in arg 3 :%s ' % (eachArgNum,arg3[eachArgNum]))
if __name__ == '__main__':
    tupleArgs('A')      
    #   arg 1:A 
    #   arg 2:B 
    tupleArgs('23','C')
    #   arg 1:23 
    #   arg 2:C
    tupleArgs('12','A','GF','L')
    #   arg 1:12 
    #   arg 2:A 
    #   the 0 in arg 3 :GF 
    #   the 1 in arg 3 :L 
    
#2.**kw
    
def dictArgs(kw1, kw2= 'B', **kw3):
    print('kw 1:%s ' % kw1)
    print('kw 2:%s ' % kw2)
    for eachKw in kw3:
        print('the %s ---->:%s ' % (eachKw,kw3[eachKw]))
if __name__ == '__main__':
    dictArgs('A')
    #   kw 1:A 
    #   kw 2:B 
    dictArgs('23','C')
    #   kw 1:23 
    #   kw 2:C 
    dictArgs('12','A', c = 'C',d = '12121212')
    #   kw 1:12 
    #   kw 2:A 
    #   the d ---->:12121212 
    #   the c ---->:C 
    dictArgs('kw',c = 'C',d = '12121212',kw = 'KW')
    #   kw 1:kw 
    #   kw 2:B 
    #   the kw ---->:KW 
    #   the d ---->:12121212 
    #   the c ---->:C
    
#3.*args和**kw
def foo(*args, **kwargs):    

    print 'args = ', args    

    print 'kwargs = ', kwargs    

    print '---------------------------------------'

if __name__ == '__main__':
   foo(1,2,3,4)
   foo(a=1,b=2,c=3)
   foo(1,2,3,4, a=1,b=2,c=3)
   foo('a', 1, None, a=1, b='2', c=3)

# args =  (1, 2, 3, 4)
# kwargs =  {}
# ---------------------------------------
# args =  ()
# kwargs =  {'a': 1, 'c': 3, 'b': 2}
# ---------------------------------------
# args =  (1, 2, 3, 4)
# kwargs =  {'a': 1, 'c': 3, 'b': 2}
# ---------------------------------------
# args =  ('a', 1, None)
# kwargs =  {'a': 1, 'c': 3, 'b': '2'}
# ---------------------------------------