from math import pi


class circle ():
    def __init__(self, radius):
        self.radius = radius

    def area(self,):
        return 2**pi*self.radius

    def circumfrance(self):
        return 2*self.radius*pi


a = circle(21)
print(a.area())
print(a.circumfrance())
