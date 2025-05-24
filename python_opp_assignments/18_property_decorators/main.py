class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    # Getter method
    @property
    def price(self):
        return self._price

    # Setter method
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    # Deleter method
    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Create a Product object
p = Product(100)

# Access the price (getter)
print("Price:", p.price)

# Update the price (setter)
p.price = 150
print("Updated Price:", p.price)

# Delete the price (deleter)
del p.price

# Trying to access price after deletion will raise an AttributeError
try:
    print(p.price)
except AttributeError as e:
    print("Error:", e)
