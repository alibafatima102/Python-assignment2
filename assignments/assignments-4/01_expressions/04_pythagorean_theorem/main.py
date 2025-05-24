import math  # Import math library for square root function

def main():
    # Prompt the user for the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse using Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)

    # Display the result
    print("The length of BC (the hypotenuse) is: " + str(bc))

# Required to call main function
if __name__ == "__main__":
    main()
