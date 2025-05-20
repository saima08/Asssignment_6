from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, hight):
        self.w = width
        self.h = hight

    def area(self):
        return self.w * self.h

r = Rectangle(5, 4)
print(r.area())
