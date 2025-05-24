MAX_LENGTH = 3

def shorten(lst):
    """
    Removes elements from the end of lst until its length is MAX_LENGTH.
    Prints each removed item.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove last item
        print(removed_item)

def main():
    lst = []
    n = int(input("How many elements will your list have? "))

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)

    shorten(lst)

if __name__ == "__main__":
    main()
