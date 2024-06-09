
import sys

n = int(input())
lengths = list(map(int, input().split()))

# Sort the lengths in non-decreasing order
lengths.sort()

# Initialize the number of triples to 0
num_triples = 0

# Iterate over all possible values of i
for i in range(n - 2):
    # Initialize j to i + 1
    j = i + 1
    # Initialize k to j + 1
    k = j + 1
    # While k is less than n
    while k < n:
        # If lengths[i], lengths[j], and lengths[k] form a triangle
        if lengths[i] + lengths[j] > lengths[k] and lengths[j] + lengths[k] > lengths[i] and lengths[i] + lengths[k] > lengths[j]:
            # Increment the number of triples
            num_triples += 1
        # Increment k
        k += 1

# Print the number of triples
print(num_triples)

