class StatVarDel:
    a=10
    b=50
    c=100
    def __init__(self):
        del StatVarDel.a
        
    def first(self):
        del StatVarDel.a

    @classmethod
    def second(cls):
        StatVarDel.c=90
        #del cls.c
        
stat = StatVarDel()
print(StatVarDel.b)
del StatVarDel.b
stat.second()
print(StatVarDel.c)
