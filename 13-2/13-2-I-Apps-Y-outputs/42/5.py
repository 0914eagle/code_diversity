
import sys

# Get the number of relatives
N = int(input())

# Initialize the total value to 0
total_value = 0

# Loop through each relative
for i in range(N):
    # Get the amount and currency of the otoshidama
    amount, currency = input().split()
    
    # If the currency is JPY, add the amount to the total value
    if currency == "JPY":
        total_value += float(amount)
    
    # If the currency is BTC, convert it to JPY and add it to the total value
    elif currency == "BTC":
        total_value += float(amount) * 380000.0

# Print the total value
print(total_value)

