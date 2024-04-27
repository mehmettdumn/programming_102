# Prompting the user to enter their weight in kilograms
weight = int(input("Enter your weight in kilograms: "))

# Prompting the user to enter their height in meters
height = float(input("Enter your height in meters: "))

# Calculating the Body Mass Index (BMI)
bmi = weight / (height * height)
print("Your BMI is", bmi)

# Providing a classification based on the BMI
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print("Your weight is normal.")
elif bmi >= 25 and bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
