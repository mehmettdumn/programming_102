# Prompting the user to enter the lengths of the three edges of the rectangular prism
a = int(input("Enter the length of edge 'a': "))
b = int(input("Enter the length of edge 'b': "))
c = int(input("Enter the length of edge 'c': "))

# Calculating the surface area of the rectangular prism using the formula: 2ab + 2bc + 2ac
surface_area = 2 * a * b + 2 * b * c + 2 * a * c

# Printing the surface area
print("Surface area of the rectangular prism is:", surface_area)
