
import math

def count_permutations(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = math.factorial(n)
    
    # Calculate the number of permutations with runs of length k
    num_runs = 0
    for i in range(1, n - k + 2):
        num_runs += math.comb(n - i, k - 1)
    
    # Calculate the number of permutations with runs of length k or less
    num_permutations_with_runs = num_permutations - num_runs
    
    # Return the result modulo p
    return num_permutations_with_runs % p

n, k, p = map(int, input().split())
print(count_permutations(n, k, p))

