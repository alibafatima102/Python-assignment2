class Bank:
    # Class variable
    bank_name = "State Bank of Python"
    
    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

# Create two instances of the Bank class
account1 = Bank()
account2 = Bank()

# 🔹 Before changing the bank name
print("🔸 BEFORE changing bank name:")
print("Bank Name (account1):", account1.bank_name)
print("Bank Name (account2):", account2.bank_name)

# Change the bank name using the class method
Bank.change_bank_name("Python National Bank")

# 🔹 After changing the bank name
print("\n🔸 AFTER changing bank name:")
print("Bank Name (account1):", account1.bank_name)
print("Bank Name (account2):", account2.bank_name)
