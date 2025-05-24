# Employee class (independent)
class Employee:
    def __init__(self, name):
        self.name = name

    def display_employee(self):
        print(f"Employee Name: {self.name}")

# Department class (aggregates Employee)
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Reference to an Employee object

    def display_department(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_employee()

# Create an Employee object independently
emp = Employee("Sarah")

# Pass the Employee object to Department (aggregation)
dept = Department("HR", emp)

# Display details
dept.display_department()

# Employee object still exists independently
print("Employee object still accessible:")
emp.display_employee()
