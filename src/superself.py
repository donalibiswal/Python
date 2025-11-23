      

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def display(self):
        print("Name is:", self.name)
        print("Age is:", self.age)
        print("Height is:", self.height)
        print("Weight is:", self.weight)

class Student(Person):
    def __init__(self, sno, course, fees, name, age, height, weight):
       
        self.sno = sno
        self.course = course
        self.fees = fees
        
        super().__init__(name, age, height, weight)

    def display(self):
        
        super().display()
        print("SNO is:", self.sno)
        print("Course is:", self.course)
        print("Fees is:", self.fees)

s = Student(101, "C++", 5000, "Donali",21,62,50)
s.display()

        
