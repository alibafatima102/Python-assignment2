def get_first_element(lst):
    """
    Takes a list lst and prints the first element.
    """
    print(lst[0])


def main():
    lst = []
    n = int(input("How many elements will your list have? "))

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)

    get_first_element(lst)


if __name__ == "__main__":
    main()
