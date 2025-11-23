from abc import ABC,abstractmethod
class simcard(ABC):
  '''def shape(self):
        print("Every sim shape has Nanosturcture")'''  
@abstractmethod
def cost(self):
        pass
class jio(simcard):
    def cost(self):
        print("jio sim cost=rs.666 ")
class airtel(simcard):
    def cost(self):
        print("Airtel sim cost=rs.799")
class Bsnl(simcard):
    def cost(self):
        print("Bsnl sim cost =rs.249")
obj=jio()
#obj.shape()
obj.cost()
obj2=airtel()
#obj2.shape()
obj2.cost()
obj3=Bsnl()
#obj3.shape()
obj3.cost()
