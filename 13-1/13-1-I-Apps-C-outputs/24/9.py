
import sys

n, k, p = map(int, input().split())

# Initialize the result
result = 1

# Iterate over all possible runs of length k
for i in range(1, k+1):
    # Calculate the number of permutations with a run of length i
    num_permutations = (n-i+1) * (n-i+2) * ... * (n-i+i)
    
    # Calculate the number of permutations with a run of length i or less
    num_permutations_less = num_permutations * (n-i+1)
    
    # Add the number of permutations with a run of length i or less to the result
    result = (result + num_permutations_less) % p

print(result)

