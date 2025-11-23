class Car:
    def _init_(self, make, model, colour, milage):
        self.make = make
        self.model = model
        self.colour = colour
        self.milage = milage

    def display(self):
        print("Car making company:", self.make)
        print("Car model is:", self.model)
        print("Car colour is:", self.colour)
        print("Car mileage is:", self.milage)


class Person:
    def _init_(self, name, age, job_in, make, model, colour, milage):
        self.name = name
        self.age = age
        self.job_in = job_in
        self.car = Car(make, model, colour, milage)

    def display_car(self):
        print("Car's driver name is:", self.name)
        print("Car's driver age is:", self.age)
        print("Car's driver job:", self.job_in)
        self.car.display() 
car_info1 = Person("Alok", 25, "IT", "TATA", "Nexon", "blue", "12km/l")
car_info2 = Person("sam", 34, "technical", "honda", "amaze", "white", "13km/l")
car_info1.display_car()
car_info2.display_car()
