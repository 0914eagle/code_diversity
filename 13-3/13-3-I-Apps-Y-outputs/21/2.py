
import sys

n = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Initialize the maximum possible value of X-Y
max_value = 0

# Iterate over all possible combinations of gems
for i in range(1 << n):
    # Calculate the sum of values and costs for the current combination
    current_values = 0
    current_costs = 0
    for j in range(n):
        if i & (1 << j):
            current_values += values[j]
            current_costs += costs[j]
    
    # Update the maximum possible value of X-Y
    max_value = max(max_value, current_values - current_costs)

print(max_value)

