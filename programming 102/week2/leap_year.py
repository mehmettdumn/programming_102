# Take the year from the user
year = int(input("Enter the year: "))

# Function to determine if it's a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Check if it's a leap year using the function
if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
