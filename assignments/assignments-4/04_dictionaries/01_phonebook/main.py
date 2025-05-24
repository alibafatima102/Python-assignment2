# Phonebook using dictionary

def display_menu():
    print("\nPhonebook Menu:")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Display All Contacts")
    print("4. Exit")

def add_contact(phonebook):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    phonebook[name] = phone
    print(f"Contact '{name}' added successfully.")

def search_contact(phonebook):
    name = input("Enter name to search: ")
    if name in phonebook:
        print(f"{name}'s phone number is {phonebook[name]}")
    else:
        print(f"Contact '{name}' not found.")

def display_all_contacts(phonebook):
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("\nAll Contacts:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")

def phonebook_program():
    phonebook = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            add_contact(phonebook)
        elif choice == '2':
            search_contact(phonebook)
        elif choice == '3':
            display_all_contacts(phonebook)
        elif choice == '4':
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the phonebook program
phonebook_program()
