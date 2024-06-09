
import itertools

def get_good_permutations(n, s):
    # Initialize a list to store the good permutations
    good_permutations = []
    
    # Iterate over all permutations of size n
    for perm in itertools.permutations(range(1, n+1)):
        # Check if the permutation turns the sequence into a good sequence
        if is_good_sequence(s, perm):
            # If it is, add it to the list of good permutations
            good_permutations.append(perm)
    
    # Return the list of good permutations
    return good_permutations

def is_good_sequence(s, perm):
    # Initialize a set to store the first elements of the sequence
    first_elements = set()
    # Initialize a set to store the second elements of the sequence
    second_elements = set()
    
    # Iterate over the sequence and apply the permutation
    for i in range(len(s)):
        first_elements.add(s[i][0])
        second_elements.add(s[i][1])
    
    # Check if the sequence is sorted by first elements or second elements
    if sorted(first_elements) == list(first_elements) or sorted(second_elements) == list(second_elements):
        return False
    
    # If it is not sorted, return True
    return True

n = int(input())
s = []

# Read the input sequence
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

# Get the good permutations
good_permutations = get_good_permutations(n, s)

# Print the number of good permutations modulo 998244353
print(len(good_permutations) % 998244353)

