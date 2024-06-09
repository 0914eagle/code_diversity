
import sys

def count_permutations(n, s):
    # Initialize the number of permutations to 0
    permutations = 0
    
    # Iterate over each permutation of size n
    for p in permutations(range(1, n + 1)):
        # Initialize the number of bad sequences to 0
        bad_sequences = 0
        
        # Iterate over each pair in the sequence
        for i in range(n):
            # Check if the sequence is sorted in non-descending order by first elements
            if s[i][0] != p[i]:
                bad_sequences += 1
                break
        
        # If the sequence is not sorted in non-descending order by first elements,
        # check if it is sorted in non-descending order by second elements
        if bad_sequences == 0:
            for i in range(n):
                if s[i][1] != p[i]:
                    bad_sequences += 1
                    break
        
        # If the sequence is not sorted in non-descending order by first or second elements,
        # it is a good sequence
        if bad_sequences == 0:
            permutations += 1
    
    # Return the number of permutations modulo 998244353
    return permutations % 998244353

# Define the permutations function
def permutations(iterable):
    pool = tuple(iterable)
    n = len(pool)
    if n == 1:
        yield pool
    elif n > 1:
        for i in range(n):
            for p in permutations(pool[:i] + pool[i+1:]):
                yield pool[i] + p

# Get the number of pairs from the input
n = int(input())

# Initialize the sequence
s = []

# Iterate through each pair and add it to the sequence
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

# Call the count_permutations function and print the result
print(count_permutations(n, s))


