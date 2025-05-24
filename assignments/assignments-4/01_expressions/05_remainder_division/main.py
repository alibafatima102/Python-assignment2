def main():
    # Prompt the user for the dividend and divisor as integers
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Calculate quotient and remainder
    quotient = dividend // divisor
    remainder = dividend % divisor

    # Print the result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))

# Required to run the main function
if __name__ == "__main__":
    main()
