def add_three_copies(lst, message):
    """
    Adds three copies of the message to the given list.
    Does not return anything.
    """
    lst.append(message)
    lst.append(message)
    lst.append(message)


def main():
    # User se input lete hain
    message = input("Enter a message to copy: ")

    my_list = []  # Empty list banate hain
    print("List before:", my_list)

    # Function call karke list me message ki 3 copies add karte hain
    add_three_copies(my_list, message)

    # List ko print karte hain function ke baad
    print("List after:", my_list)


if __name__ == "__main__":
    main()
