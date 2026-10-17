import gc
import time
class Test:
    def __init__(self):
        print("Constructor Execution..")
        
    def __del__(self):
        print("Destructor Execution..")
        
     
test = Test()
test = None
time.sleep(5)
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
print("End of Application ")