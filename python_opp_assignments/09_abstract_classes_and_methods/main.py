from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Concrete subclass
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Implementing the abstract method
    def area(self):
        return self.width * self.height

# Trying to create an object of Shape will raise an error
# shape = Shape()  # ❌ This will raise TypeError

# Creating an object of Rectangle
rect = Rectangle(5, 10)

# Calling the area method
print("Area of Rectangle:", rect.area())
