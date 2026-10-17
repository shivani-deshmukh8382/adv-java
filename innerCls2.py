class Person:
    def __init__(self,name):
        self.name=name
        self.dob=Person.Dob()

    class Dob: 
        def __init__(self):
            self.dd=15
            self.mm=6
            self.yy=2000
          
        def display(self):
            print('DOB {}/{}/{}'.format(self.dd,self.mm,self.yy))
            
per=Person('shivani')  
print(Person('shivani').Dob().display())