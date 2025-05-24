class TemperatureConverter:
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

# Call the static method without creating an object
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)

# Output the result
print(f"{temp_c}°C is equal to {temp_f}°F")
