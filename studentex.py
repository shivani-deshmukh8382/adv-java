class studentex :
    
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks 
    
    def talk(self):
        print("Hello My Name is:",self.name)
        print("My Rollno is:",self.rollno)
        print("My Marks are:",self.marks)


s1=studentex("Durga",101,80)
print(s1.name)
print(s1.rollno)
print(s1.marks)
s1.talk()
    