class LocalVar:
    
    def f1(self):
        a=10
        print(a)
    def f2(self):
        self.f1()
        
var = LocalVar()
var.f2() 

