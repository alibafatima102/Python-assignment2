class MathUtils:
    # Static method to add two numbers
    @staticmethod
    def add(a, b):
        return a + b

# 🔹 Calling the static method without creating an object
result = MathUtils.add(10, 20)

# 🔹 Output the result
print("The sum is:", result)
