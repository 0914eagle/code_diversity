
import itertools
import math

def count_permutations(n, s):
    # Initialize the number of permutations to 0
    num_permutations = 0
    
    # Iterate over all permutations of size n
    for perm in itertools.permutations(range(1, n + 1)):
        # Convert the permutation to a list of pairs
        perm_list = [(s[i - 1][0], s[i - 1][1]) for i in perm]
        
        # Check if the permutation turns the sequence into a good sequence
        if is_good_sequence(perm_list):
            # Increment the number of permutations
            num_permutations += 1
    
    # Return the number of permutations modulo 998244353
    return num_permutations % 998244353

def is_good_sequence(s):
    # Check if the sequence is sorted in non-descending order by first elements
    if is_sorted_by_first_elements(s):
        return False
    
    # Check if the sequence is sorted in non-descending order by second elements
    if is_sorted_by_second_elements(s):
        return False
    
    # If neither of the above conditions are met, the sequence is good
    return True

def is_sorted_by_first_elements(s):
    # Sort the sequence by first elements in non-descending order
    sorted_s = sorted(s, key=lambda x: x[0])
    
    # Check if the sorted sequence is the same as the original sequence
    return sorted_s == s

def is_sorted_by_second_elements(s):
    # Sort the sequence by second elements in non-descending order
    sorted_s = sorted(s, key=lambda x: x[1])
    
    # Check if the sorted sequence is the same as the original sequence
    return sorted_s == s

n = int(input())
s = []

# Read the sequence of pairs
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

# Call the count_permutations function and print the result
print(count_permutations(n, s))

