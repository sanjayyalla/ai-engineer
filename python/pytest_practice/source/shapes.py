class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.radius = r

    def  area(self):
        return 3.14 * self.radius * self.radius
    def  perimeter(self):
        return 2 * 3.14 * self.radius


class Rectangle:

    def __init__(self, length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    