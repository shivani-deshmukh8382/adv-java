class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        
    def display(self):
        print("Employee number is : ",self.eno)
        print("Name of the employee is : ",self.ename)
        print("Salary is : ",self.esal)
        
class Test:
    @staticmethod
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display() 
        
e=Employee(100,'Durga',10000)
t=Test()
t.modify(e)   