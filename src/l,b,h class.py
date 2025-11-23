#wap to create real world object room in the programming world with values (length,breath,height & behaviour & calculate area &volume?

class room:
    def __init__(self,length,breath,height):
        self.length = length
        self.breath = breath
        self.height = height
    def cal_area(self):
        return self.length*self.breath
    def cal_volume(self):
        return self.length*self.breath*self.height
    def display(self):
        print("area of the room:",self.cal_area())
        print("volume of the room:",self.cal_volume())
area=room(4,5,6)
area.display()
        
