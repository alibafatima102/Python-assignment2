class A:
    def show(self):
        print("Method from class A")

class B(A):
    def show(self):
        print("Method from class B")

class C(A):
    def show(self):
        print("Method from class C")

class D(B, C):
    pass

# Create an object of class D
d = D()

# Call the show() method
d.show()

# Print the Method Resolution Order
print("MRO of class D:", [cls.__name__ for cls in D.__mro__])
