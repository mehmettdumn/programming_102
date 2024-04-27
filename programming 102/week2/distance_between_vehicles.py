# Prompting the user to enter the distance traveled by the first vehicle (eastward)
first_vehicle_distance = int(input("Enter the distance traveled by the first vehicle (eastward): "))

# Prompting the user to enter the distance traveled by the second vehicle (westward)
second_vehicle_distance = int(input("Enter the distance traveled by the second vehicle (westward): "))

# Comparing the absolute distances traveled by the two vehicles
if abs(first_vehicle_distance) > second_vehicle_distance:
    print("The first vehicle has traveled a greater distance.")
else:
    print("The second vehicle has traveled a greater distance.")
