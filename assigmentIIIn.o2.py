# Define the conversion function
def convert(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

# Ask the user to input temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Call the convert function
celsius = convert(fahrenheit)

# Print the Celsius temperature
print(f"Temperature in Celsius: {celsius:.2f}")

# Check if it's hot or cold
if celsius > 20:
    print("IT'S HOT HERE")
else:
    print("IT’S COLD HERE")
