#This program satisfies the I in SOLID because it can accept new shapes without modifying the existing code
#get_area() does violate LSP as long as the behavior changes to match the specifications of each shape
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area method")

class Dimensionable(ABC):
    @abstractmethod
    def set_dimensions(self, *args):
        raise NotImplementedError("Subclasses must implement set_dimensions method")

class Circle(Shape, Dimensionable):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius ** 2

    def set_dimensions(self, radius):
        self.radius = radius

class Rectangle(Shape, Dimensionable):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

def calculate_total_area(shapes):
    total_area = 0
    for shape in shapes:
        total_area += shape.get_area()
    return total_area

def main():
    circle = Circle(radius=5)
    rectangle = Rectangle(width=3, height=4)
    triangle = Triangle(base=4, height=3)

    shapes = [circle, rectangle, triangle]
    total_area = calculate_total_area(shapes)
    print("Total area of all shapes:", total_area)

    circle.set_dimensions(7)
    rectangle.set_dimensions(5, 6)

    total_area = calculate_total_area(shapes)
    print("Total area of all shapes after dimension change:", total_area)

if __name__ == "__main__":
    main()


