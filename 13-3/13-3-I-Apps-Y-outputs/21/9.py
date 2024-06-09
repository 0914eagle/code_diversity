
import sys

n = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Initialize the maximum possible value of X-Y
max_value = 0

# Iterate over all possible combinations of gems
for i in range(2**n):
    # Convert the binary representation of i to a list of booleans
    choices = [bool(i & (1 << j)) for j in range(n)]
    
    # Calculate the sum of values and costs for the current combination of gems
    x = sum(values[j] for j in range(n) if choices[j])
    y = sum(costs[j] for j in range(n) if choices[j])
    
    # Update the maximum possible value of X-Y
    max_value = max(max_value, x - y)

print(max_value)

