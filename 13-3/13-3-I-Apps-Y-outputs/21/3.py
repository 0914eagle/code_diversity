
import sys

n = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Initialize the maximum value of X-Y
max_value = 0

# Iterate over all possible combinations of gems
for i in range(1 << n):
    # Calculate the value and cost of the current combination
    value = 0
    cost = 0
    for j in range(n):
        if i & (1 << j):
            value += values[j]
            cost += costs[j]
    
    # Update the maximum value of X-Y
    max_value = max(max_value, value - cost)

print(max_value)

