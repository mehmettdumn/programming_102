# Providing information about the optimal temperature ranges for different bacteria species
print("Optimal temperature range for Streptococcus is between 40-45 degrees Celsius.")
print("Optimal temperature range for Lactobacillus is between 35-38 degrees Celsius.")
print("Optimal temperature range for Escherichia is between 35-40 degrees Celsius.")

# Prompting the user to enter the temperature
temperature = int(input("Enter the temperature: "))

# Checking if the entered temperature is within the valid range (-20 to 100 degrees Celsius)
if temperature >= -20 and temperature <= 100:
    # Checking if the temperature falls within the optimal range for Streptococcus
    if temperature >= 40 and temperature <= 45:
        print("Streptococcus can survive.")
    # Checking if the temperature falls within the optimal range for Lactobacillus
    if temperature >= 35 and temperature <= 38:
        print("Lactobacillus can survive.")
    # Checking if the temperature falls within the optimal range for Escherichia
    if temperature >= 35 and temperature <= 40:
        print("Escherichia can survive.")
    # If the temperature doesn't fall within any optimal range, printing that all bacteria would die
    else:
        print("All bacteria would die.")
# If the entered temperature is outside the valid range, printing an error message
else:
    print("You entered a value outside the measurement range of the thermometer!")
