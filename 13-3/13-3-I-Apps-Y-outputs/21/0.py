
import sys

n = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Initialize the maximum possible value of X-Y to 0
max_value = 0

# Iterate over all possible combinations of gems
for i in range(1 << n):
    # Initialize the sum of values and costs for this combination to 0
    value = 0
    cost = 0
    
    # Iterate over the gems and add their values and costs if they are selected in this combination
    for j in range(n):
        if i & (1 << j):
            value += values[j]
            cost += costs[j]
    
    # Update the maximum possible value of X-Y if this combination has a higher value
    max_value = max(max_value, value - cost)

print(max_value)

