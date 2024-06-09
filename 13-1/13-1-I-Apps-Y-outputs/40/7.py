
A, B = map(int, input().split())

# Initialize the lowest price that satisfies the condition
lowest_price = -1

# Iterate through all possible prices
for price in range(1, 101):
    # Calculate the amount of consumption tax for both rates
    tax_8 = int(price * 0.08)
    tax_10 = int(price * 0.1)
    
    # Check if the amount of consumption tax for both rates is within the given range
    if A <= tax_8 <= B and A <= tax_10 <= B:
        # If the price satisfies the condition, update the lowest price
        lowest_price = price
        break

print(lowest_price)

