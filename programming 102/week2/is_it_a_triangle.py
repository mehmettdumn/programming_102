# Prompting the user to enter the lengths of the sides of the triangle
a = int(input("Enter the length of the first side of the triangle: "))
b = int(input("Enter the length of the second side of the triangle: "))
c = int(input("Enter the length of the third side of the triangle: "))

# Checking if the given lengths form a valid triangle
if a + b > c and a + c > b and b + c > a:
    # If the triangle is valid, further classify its type
    if a == b == c:
        print("This is an equilateral triangle.")
    elif a == b or b == c or a == c:
        print("This is an isosceles triangle.")
    else:
        print("This is a scalene triangle.")
else:
    # If the given lengths do not form a valid triangle
    print("This is not a triangle.")
