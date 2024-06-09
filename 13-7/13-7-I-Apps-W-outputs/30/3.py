
import itertools

def count_permutations(n, s):
    # Initialize the number of permutations to 0
    permutations = 0
    
    # Iterate over all permutations of size n
    for perm in itertools.permutations(range(1, n + 1)):
        # Check if the permutation turns the sequence into a good sequence
        if is_good_sequence(s, perm):
            # Increment the number of permutations
            permutations += 1
    
    # Return the number of permutations modulo 998244353
    return permutations % 998244353

def is_good_sequence(s, perm):
    # Initialize the first and second elements as sorted
    first_elements, second_elements = sorted(s), sorted(s)
    
    # Iterate over the pairs in the sequence
    for i in range(len(s)):
        # Update the first and second elements with the permuted values
        first_elements[i], second_elements[i] = s[perm[i] - 1]
    
    # Check if either the first or second elements are sorted
    return not (first_elements == sorted(first_elements) or second_elements == sorted(second_elements))

n = int(input())
s = []

# Iterate through the input and create a list of pairs
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

# Call the count_permutations function and print the result
print(count_permutations(n, s))

