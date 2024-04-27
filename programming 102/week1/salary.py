# Prompting the user to enter the price of the computer
T = int(input("Enter the price of the computer: "))

# Prompting the user to enter the percentage rate the employee will receive
P = int(input("Enter the percentage rate the employee will receive: "))

# Calculating the amount the employee will receive
amount_received = T * (P / 100)

# Printing the amount the employee will receive
print("The amount the employee will receive is:", amount_received)
