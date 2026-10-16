class StaticVariable:
    '''static variable declaration'''
    a=10
    def __init__(self):
        print("Constructor")
        StaticVariable.b=20
        print(StaticVariable.a)
        print("....................................................")
    
    def first(self):
        print("instance method")
        StaticVariable.c=30
        print(self.b)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        
    def random(self):
        print('instance method')
        print("random")
        print(self.a,self.b,StaticVariable.c)
        del StaticVariable.a
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
       
    @classmethod
    def second(cls):
        print("classs method")
        StaticVariable.d=40
        del cls.b
        cls.a=57
        print(cls.a,cls.b,StaticVariable.c)
        print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        
    @staticmethod
    def third():
        print('static method')
        StaticVariable.e=50
        StaticVariable.b=98
        print(StaticVariable.a,StaticVariable.b,StaticVariable.c,StaticVariable.d,StaticVariable.e)
        print('..........................................................')
        
    def add(self,a,b):
        print('instance method')
        print(self.a,StaticVariable.b,self.c,StaticVariable.d,StaticVariable.e)
        return a+b
   
    
print(StaticVariable.a)
staticVariable = StaticVariable()
staticVariable.first()
staticVariable.second()
staticVariable.third()
staticVariable.random()
print(staticVariable.add(10,100)) 
print(StaticVariable.a,StaticVariable.b,StaticVariable.c,StaticVariable.d,StaticVariable.e)
print(StaticVariable.__doc__)
