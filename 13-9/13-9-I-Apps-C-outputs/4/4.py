
import sys

n = int(input())
a = list(map(int, input().split()))

# Initialize the number of entirely unsorted sequences to 0
num_sequences = 0

# Iterate over all possible permutations of the input sequence
for perm in itertools.permutations(a):
    # Initialize the number of sorted elements to 0
    num_sorted = 0
    
    # Iterate over all elements in the permutation
    for i in range(n):
        # If the element is sorted, increment the number of sorted elements
        if all(perm[i] >= perm[j] for j in range(i+1, n)):
            num_sorted += 1
    
    # If all elements are sorted, increment the number of entirely unsorted sequences
    if num_sorted == n:
        num_sequences += 1

# Print the number of entirely unsorted sequences modulo 10^9 + 9
print(num_sequences % (10**9 + 9))

