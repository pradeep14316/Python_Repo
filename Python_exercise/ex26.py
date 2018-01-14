#Encapsulation
class Circle():

    pi = 3.141592

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def setRadius(self, radius=1):
        self.radius = radius

    def getRadius(self):
        return self.radius

class Rectangle():
    'Finding area of rectangle'

    def __init__(self,length=1,breadth=1):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def setlenbredth(self,length=1,breadth=1):
        self.length = length
        self.breadth = breadth

    def getlenbreadth(self):

        return self.length,self.breadth


