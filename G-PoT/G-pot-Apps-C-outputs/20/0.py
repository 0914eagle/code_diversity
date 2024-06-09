
# Read input
N = int(input())
array = [int(input()) for _ in range(N)]

# Calculate the sum of prices
sum_prices = 0
for i in range(N):
    for j in range(i, N):
        min_val = min(array[i:j+1])
        max_val = max(array[i:j+1])
        length = j - i + 1
        price = min_val * max_val * length
        sum_prices += price

# Output the last 9 digits of the sum
print(sum_prices % 10**9)
