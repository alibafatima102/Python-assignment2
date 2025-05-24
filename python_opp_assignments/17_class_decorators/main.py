# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet  # Add greet method to the class
    return cls

# Apply the decorator to Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Create an object of Person
p = Person("Alice")

# Call the added greet() method
print(p.greet())
