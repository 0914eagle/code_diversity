
# Read from stdin, A and B
A, B = map(int, input().split())

# Calculate the three expressions
sum = A + B
diff = A - B
product = A * B

# Find the largest value
largest = max(sum, diff, product)

# Print the largest value
print(largest)

