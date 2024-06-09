
import sys

def get_permutation_count(n, s):
    # Initialize the permutation count to 0
    permutation_count = 0
    
    # Iterate over all permutations of size n
    for permutation in itertools.permutations(range(1, n + 1)):
        # Convert the permutation to a list
        permutation_list = list(permutation)
        
        # Initialize two flags to keep track of whether the sequence is sorted by first or second elements
        sorted_by_first = False
        sorted_by_second = False
        
        # Iterate over the pairs in the sequence
        for i in range(n - 1):
            # If the first elements are not sorted, check if the current pair is sorted
            if not sorted_by_first:
                if s[permutation_list[i] - 1][0] > s[permutation_list[i + 1] - 1][0]:
                    sorted_by_first = True
            # If the second elements are not sorted, check if the current pair is sorted
            if not sorted_by_second:
                if s[permutation_list[i] - 1][1] > s[permutation_list[i + 1] - 1][1]:
                    sorted_by_second = True
        
        # If neither the first elements nor the second elements are sorted, the sequence is good
        if not sorted_by_first and not sorted_by_second:
            permutation_count += 1
    
    # Return the permutation count modulo 998244353
    return permutation_count % 998244353

