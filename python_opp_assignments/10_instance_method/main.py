class Dog:
    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    # Instance method
    def bark(self):
        print(f"Woof! My name is {self.name} and I am a {self.breed}.")

# Create an instance of Dog
dog1 = Dog("Buddy", "Golden Retriever")

# Call the instance method
dog1.bark()
