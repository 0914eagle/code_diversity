
n = int(input())

# Calculate the maximum beauty
m = n
for i in range(n):
    m ^= i

# Generate a permutation with the maximum beauty
permutation = list(range(n+1))
permutation[1], permutation[2] = permutation[2], permutation[1]

# Output the result
print(m)
print(" ".join(map(str, permutation)))
