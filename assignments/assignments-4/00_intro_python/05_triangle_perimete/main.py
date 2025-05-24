def main():
    # Prompt the user to input the lengths of the triangle's sides
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Output the result
    print("The perimeter of the triangle is " + str(perimeter))


# This line is required to call the main function
if __name__ == '__main__':
    main()
