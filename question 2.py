def convert(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

# Accept temperature in Fahrenheit from the user
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert the temperature to Celsius
celsius = convert(fahrenheit)

# Check if the temperature is hot or cold
if celsius > 20:
    print("IT'S HOT HERE.")
else:
    print("It'S COLD HERE.")