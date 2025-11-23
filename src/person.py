
class person:
    def __init__(self,name,age,height,weight):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def display(self):
        
        print("name is :",self.name)
        print("person age is:",self.age)
        print("person height is:",self.height)
        print("person weight is:",self.weight)
        
        
class student(person):
    def __init__(self,sno,course,fee,name,age,height,weight):
        super().__init__(name,age,height,weight)
        self.sno=sno
        self.course=course
        self.fee=fee
        
    def display(self):
        print("student id no. is:",self.sno)
        print("student's course is:",self.course)
        print("student's fee structure is:",self.fee)
        super().display()
        
   

s=str(input("Enter the student name is:"))
s1=str(input("Enter the student course "))
s2=int(input("Enter the student height:"))
s3=int(input("Enter the student's weight is:"))
s4=int(input("Enter the student's id no is:"))
s5=str(input("Enter the student course is:"))
s6=int(input("Enter the student fee is:"))
     
s=student(s,s1,s2,s3,s4,s5,s6)
s.display()


