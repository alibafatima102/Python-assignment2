# Speed of light constant in meters per second
C = 299792458

def main():
    # Prompt user to enter mass in kilograms
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate energy using E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Output the details and result
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_joules) + " joules of energy!")

# Required to run main function
if __name__ == "__main__":
    main()
