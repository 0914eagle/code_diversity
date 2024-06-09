
n = int(input())

# Calculate the number of 1000-yen bills needed to pay the price
num_bills = n // 1000

# Calculate the amount of change
change = n - (num_bills * 1000)

# Print the amount of change
print(change)

