
n = int(input())

# Calculate the number of 1000-yen bills needed to pay the price
num_bills = n // 1000

# Calculate the change
change = n - (num_bills * 1000)

# Print the change
print(change)

