def get_last_element(lst):
    """
    Prints the last element of the list lst.
    """
    print(lst[-1])


def main():
    lst = []
    try:
        n = int(input("How many elements will your list have? "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)

    get_last_element(lst)


if __name__ == "__main__":
    main()
