
# Read input
S = input().strip()

# Calculate the price based on the toppings
price = 700 + S.count('o') * 100

# Print the price
print(price)
