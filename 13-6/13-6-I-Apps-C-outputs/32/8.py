
def solve(n, k, p):
    # Calculate the number of permutations of length n
    # with runs of length at most k
    num_permutations = 1
    for i in range(1, n+1):
        num_permutations = (num_permutations * (k+1-i)) % p
    
    # Calculate the number of permutations of length n
    # with runs of length exactly k
    num_permutations_exact = 1
    for i in range(1, n-k+1):
        num_permutations_exact = (num_permutations_exact * (k-i)) % p
    
    # Subtract the number of permutations of length n
    # with runs of length exactly k from the total number of permutations
    num_permutations = (num_permutations - num_permutations_exact + p) % p
    
    return num_permutations

