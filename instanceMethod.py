class Student:
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name
    
    def setMarks(self,marks):
        self.marks = marks
        
    def getMarks(self):
        return self.marks
    
n=int(input('enter number of students :'))
for i in range(n):
    s = Student()
    name = input("Enter name : ")
    marks = int( input("Enter marks :"))
    s.setName(name)
    s.setMarks(marks)
    print('Name of student is : ',s.getName())
    print('marks : ',s.getMarks())    



    