class instanceVariable:
    #instance variable declared inside constructor,instance method 
    # and outside of class using object reference variable
    def __init__(self):
        self.name="shivani"
        self.occupation="Software Engineer"
        print(self.name)
        print(self.occupation)
        
    def insta(self):
        self.age=25
        print(self.age)
        
    
    
i=instanceVariable()
print(i.name)
print(i.occupation)
print(i.insta())
i.age=20
print(i.age)
del i.name
print("Now new instance is creating ...")
j=instanceVariable()
print(j.insta())
print(j.age)
print(i.__dict__)
print(j.__dict__)
