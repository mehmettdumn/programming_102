# Prompting the user to enter a number
number = int(input("Enter a number: "))


if number % 6 == 0:
    print("The number is divisible by 6 .")
# If it's not divisible by 6 at all, print a message stating that
else:
    print("The number is not divisible by 6.")
