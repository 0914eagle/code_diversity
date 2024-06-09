
import itertools

def count_good_permutations(n, s):
    # Convert the input sequence to a list of pairs
    pairs = [(a, b) for a, b in s]
    
    # Initialize the count of good permutations to 0
    count = 0
    
    # Iterate over all permutations of size n
    for perm in itertools.permutations(range(1, n + 1)):
        # Check if the permutation turns the input sequence into a good sequence
        if is_good_sequence(pairs, perm):
            # Increment the count of good permutations
            count += 1
    
    # Return the count of good permutations modulo 998244353
    return count % 998244353

def is_good_sequence(pairs, perm):
    # Convert the permutation to a list of pairs
    perm_pairs = [(pairs[i - 1][0], pairs[i - 1][1]) for i in perm]
    
    # Check if the sequence is sorted in non-descending order by first elements
    if is_sorted_by_first_elements(perm_pairs):
        return False
    
    # Check if the sequence is sorted in non-descending order by second elements
    if is_sorted_by_second_elements(perm_pairs):
        return False
    
    # If neither of the above conditions are met, the sequence is good
    return True

def is_sorted_by_first_elements(pairs):
    # Sort the sequence by first elements in non-descending order
    sorted_pairs = sorted(pairs, key=lambda x: x[0])
    
    # Check if the sequence is sorted in non-descending order
    for i in range(len(sorted_pairs) - 1):
        if sorted_pairs[i][0] > sorted_pairs[i + 1][0]:
            return False
    
    # If the sequence is sorted in non-descending order, return True
    return True

def is_sorted_by_second_elements(pairs):
    # Sort the sequence by second elements in non-descending order
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    
    # Check if the sequence is sorted in non-descending order
    for i in range(len(sorted_pairs) - 1):
        if sorted_pairs[i][1] > sorted_pairs[i + 1][1]:
            return False
    
    # If the sequence is sorted in non-descending order, return True
    return True

n = int(input())
s = []
for i in range(n):
    a, b = map(int, input().split())
    s.append((a, b))

print(count_good_permutations(n, s))


