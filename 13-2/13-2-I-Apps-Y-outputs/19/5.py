
N = int(input())

# Calculate the number of 1000-yen bills needed to pay the price
num_bills = N // 1000

# Calculate the amount of change
change = N - (num_bills * 1000)

# Print the amount of change
print(change)

