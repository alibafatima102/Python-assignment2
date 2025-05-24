# Base class
class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called. Name: {self.name}")

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        # Call the constructor of the base class
        super().__init__(name)
        self.subject = subject
        print(f"Teacher constructor called. Subject: {self.subject}")

# Create an object of Teacher
t = Teacher("Alice", "Mathematics")
