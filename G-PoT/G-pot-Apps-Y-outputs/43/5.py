
# Read the input
S = input().strip()

# Initialize the base price of ramen
price = 700

# Count the number of toppings
toppings = S.count('o')

# Calculate the total price
total_price = price + toppings * 100

# Print the total price
print(total_price)
