import math

"""
class: Animal,Dog,Cat
use: polymorphism
methods: speak()
"""

class Animal:
    def speak(self):
        print("Animal speaks in it's unique language")

class Dog():
    def speak(self):
        print("Dog barks!!")

class Cat():
    def speak(self):
        print("Cat says meow!")

animals = [Animal(),Dog(),Cat()]
for animal in animals:
    animal.speak()


"""
class: Shape
subclasses: Circle,Rectangle
methods: area()
used: super() and __str__() as per task requirement
"""

import math

class Shape:
    PI = math.pi

    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def __str__(self):
        return f"{self.name}"


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")      
        self.radius = radius

    def area(self):
        return round(self.PI * (self.radius ** 2), 3)

    def __str__(self):
        return f"{super().__str__()} (radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")   
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return (
            f"{super().__str__()} "
            f"(length={self.length}, width={self.width})"
        )

shapes = [
    Circle(5),
    Rectangle(10, 4),
    Circle(2.5)
]

for shape in shapes:
    print(shape)
    print("Area:", shape.area())
