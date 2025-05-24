class Employee:
    def __init__(self, name, salary, ssn):
        # Public variable
        self.name = name

        # Protected variable (by convention)
        self._salary = salary

        # Private variable (name mangled)
        self.__ssn = ssn

# Create an object of Employee
emp = Employee("John Doe", 50000, "123-45-6789")

# 🔹 Accessing public variable
print("Public: Name =", emp.name)  # Works fine

# 🔹 Accessing protected variable
print("Protected: Salary =", emp._salary)  # Works, but not recommended outside class

# 🔹 Accessing private variable directly (will cause error)
try:
    print("Private: SSN =", emp.__ssn)  # Will raise AttributeError
except AttributeError as e:
    print("Private: Cannot access __ssn directly:", e)

# 🔹 Accessing private variable using name mangling
print("Private (accessed safely): SSN =", emp._Employee__ssn)  # Works with name mangling
