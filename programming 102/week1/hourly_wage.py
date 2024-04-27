# Prompting the user to enter the number of hours worked by the employee
hours_worked = int(input("Enter the number of hours worked by the employee: "))

# Prompting the user to enter the hourly wage of the employee
hourly_wage = int(input("Enter the hourly wage: "))

# Calculating the gross salary
gross_salary = hours_worked * hourly_wage

# Calculating the tax (assuming a tax rate of 15%)
tax = gross_salary * 15 / 100

# Calculating the net salary after deducting the tax
net_salary = gross_salary - tax

# Printing the gross and net salaries
print("Gross salary: ", gross_salary)
print("Net salary: ", net_salary)
