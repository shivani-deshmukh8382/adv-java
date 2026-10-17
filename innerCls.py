class Outer:
    def __init__(self):
        print('outer class constructor')
    
    class Inner:
        def __init__(self):
            print('inner class constructor')
            
o=Outer()
i=o.Inner()