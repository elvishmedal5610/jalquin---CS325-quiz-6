#This program satisfies the O in SOLID because it can accept new shapes without modifying the existing code
from abc import ABC, abstractmethod
from math import pi

class AreaCalculator(ABC):
    @abstractmethod
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method")

class Circle(AreaCalculator):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

class Square(AreaCalculator):
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length ** 2

class Rectangle(AreaCalculator):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

class ShapeCalculator:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def calculate_total_area(self):
        total_area = 0
        for shape in self.shapes:
            total_area += shape.calculate_area()
        return total_area

def main():
    circle = Circle(radius=5)
    square = Square(side_length=4)
    rectangle = Rectangle(length=3, width=6)


    calculator = ShapeCalculator()


    calculator.add_shape(circle)
    calculator.add_shape(square)
    calculator.add_shape(rectangle)


    total_area = calculator.calculate_total_area()
    print("Total area of all shapes:", total_area)

if __name__ == "__main__":
    main()
