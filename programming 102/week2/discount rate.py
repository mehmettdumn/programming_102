# Defining the discount rate
discount_rate = 20 / 100

# Prompting the user to enter the price of the item
price = int(input("Enter the price of the item: "))

# Checking if the price is at least 100 units
if price >= 100:
    # Calculating the discounted price
    discounted_price = price - (price * discount_rate)
    print("Discounted price: ", discounted_price)
else:
    # Printing a message indicating that no discount is applied
    print("No discount applied.")
