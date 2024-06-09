
import sys

n = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Initialize the maximum possible value of X-Y
max_value = 0

# Iterate over all possible combinations of gems
for i in range(1 << n):
    # Calculate the value of the gems chosen in this combination
    x = 0
    for j in range(n):
        if i & (1 << j):
            x += values[j]
    
    # Calculate the cost of the gems chosen in this combination
    y = 0
    for j in range(n):
        if i & (1 << j):
            y += costs[j]
    
    # Update the maximum possible value of X-Y
    max_value = max(max_value, x - y)

print(max_value)

