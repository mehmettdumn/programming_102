# Prompting the user to enter a temperature in Celsius
C = int(input("Enter the temperature in Celsius: "))

# Converting Celsius to Fahrenheit using the formula: F = (C / 100) * 180 + 32
F = C / 100 * 180 + 32

# Printing the result
print("Temperature in Fahrenheit =", F)
