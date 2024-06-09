
import itertools

def count_good_permutations(n, s):
    # Initialize the number of good permutations to 0
    num_good_permutations = 0
    
    # Iterate over all permutations of size n
    for perm in itertools.permutations(range(1, n + 1)):
        # Check if the permutation turns the sequence into a good sequence
        if is_good_sequence(s, perm):
            # Increment the number of good permutations
            num_good_permutations += 1
    
    # Return the number of good permutations modulo 998244353
    return num_good_permutations % 998244353

def is_good_sequence(s, perm):
    # Initialize the first and second elements as sorted sequences
    first_elements, second_elements = sorted(s[i][0] for i in perm), sorted(s[i][1] for i in perm)
    
    # Check if either of the sequences is sorted
    if first_elements == list(range(1, len(s) + 1)) or second_elements == list(range(1, len(s) + 1)):
        return False
    
    # Check if the first and second elements are not sorted
    for i in range(len(s) - 1):
        if first_elements[i] > first_elements[i + 1] or second_elements[i] > second_elements[i + 1]:
            return False
    
    # If none of the above conditions are met, the sequence is good
    return True

n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

print(count_good_permutations(n, s))

