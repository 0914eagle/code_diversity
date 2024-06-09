
# Read input
N = int(input())
array = [int(input()) for _ in range(N)]

# Calculate the sum of prices
total_price = 0
for i in range(N):
    for j in range(i, N):
        sub_array = array[i:j+1]
        min_val = min(sub_array)
        max_val = max(sub_array)
        length = len(sub_array)
        price = min_val * max_val * length
        total_price += price

# Output the last 9 digits of the total price
print(total_price % 1000000000)
