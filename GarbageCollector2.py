import time 
import sys
class Test:
    def __init__(self):
        print('Constructor Execution')
    
    def __del__(self):
        print('destructor Execution')
        
t1 = Test()
t2 = t1
t3 = t1
t4 = t1
t5=t1
del t1
print(sys.getrefcount(Test))