class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Create an instance of Multiplier with factor 3
mult = Multiplier(3)

# Test if the object is callable
print("Is 'mult' callable?", callable(mult))  # True

# Call the object like a function
result = mult(10)
print("Result of mult(10):", result)
