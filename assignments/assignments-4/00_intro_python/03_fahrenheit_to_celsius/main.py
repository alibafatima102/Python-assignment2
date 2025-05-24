def main():
    # Prompt the user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert to Celsius using the formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print("Temperature:", str(fahrenheit) + "F =", str(celsius) + "C")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == "__main__":
    main()
