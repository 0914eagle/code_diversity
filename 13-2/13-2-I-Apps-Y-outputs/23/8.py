
n, k = map(int, input().split())

# Calculate the minimum difference
diff = n // k

# Calculate the remainder
rem = n % k

# Distribute the remainder equally among the first k-1 users
for i in range(k-1):
    diff += 1

# Print the minimum difference
print(diff)

