
# Read the input
A, B = map(int, input().split())

# Calculate the three expressions
expressions = [A+B, A-B, A*B]

# Find the largest value
largest = max(expressions)

# Print the largest value
print(largest)

