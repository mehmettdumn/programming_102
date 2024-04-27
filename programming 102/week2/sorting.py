print("PLEASE ENTER DIFFERENT NUMBERS!!!!!!!!!!!!!!!!!!!!")

# Prompt the user to enter three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check if all numbers are different
if number1 != number2 and number1 != number3 and number2 != number3:
    # Find the largest number among the three
    if number1 > number2 and number1 > number3:
        print("The largest number is", number1)
    elif number2 > number1 and number2 > number3:
        print("The largest number is", number2)
    elif number3 > number1 and number3 > number2:
        print("The largest number is", number3)
else:
    print("Please enter different numbers.")
