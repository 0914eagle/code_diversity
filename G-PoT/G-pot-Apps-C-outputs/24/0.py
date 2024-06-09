
n = int(input())

# Calculate the maximum beauty
max_beauty = n
for i in range(n):
    max_beauty ^= i

# Generate a permutation with the maximum beauty
permutation = [0]
for i in range(1, n+1):
    permutation.append(i)
    permutation.append(i-1)

# Print the results
print(max_beauty)
print(" ".join(map(str, permutation)))
