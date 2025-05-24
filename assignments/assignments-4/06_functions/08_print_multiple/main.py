def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    try:
        repeats = int(input("Enter a number of times to repeat your message: "))
        print_multiple(message, repeats)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == '__main__':
    main()
