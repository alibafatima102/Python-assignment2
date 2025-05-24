"""
Program: Feet to Inches Converter
---------------------------------
Converts a measurement in feet to inches.
There are 12 inches in one foot.
"""

# Constant for conversion
INCHES_IN_FOOT = 12

def main():
    # Ask user for the number of feet
    feet = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT

    # Display the result
    print("That is", inches, "inches!")

# Required to run main function
if __name__ == "__main__":
    main()
