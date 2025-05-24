# Define a constant for the maximum value
MAX_VALUE = 10000

def main():
    # Starting terms
    a, b = 0, 1

    # Print Fibonacci terms until MAX_VALUE
    while a < MAX_VALUE:
        print(a, end=" ")
        a, b = b, a + b

# Run the main function
if __name__ == "__main__":
    main()
