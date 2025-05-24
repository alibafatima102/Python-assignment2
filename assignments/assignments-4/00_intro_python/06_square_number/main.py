def main():
    # Prompt the user to enter a number
    num = float(input("Type a number to see its square: "))

    # Calculate and display the square of the number
    print(str(num) + " squared is " + str(num ** 2))


# Required to call main function
if __name__ == '__main__':
    main()
