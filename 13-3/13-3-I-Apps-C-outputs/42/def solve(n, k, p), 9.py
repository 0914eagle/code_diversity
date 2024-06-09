
def solve(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations = (num_permutations * (n - i)) % p
    
    # Initialize the number of permutations with runs of length k
    num_permutations_with_runs = 0
    
    # Iterate over all possible runs of length k
    for i in range(n - k + 1):
        # Calculate the number of permutations with a run of length k starting at position i
        num_permutations_with_run = 1
        for j in range(i, i + k):
            num_permutations_with_run = (num_permutations_with_run * (n - j)) % p
        
        # Add the number of permutations with a run of length k starting at position i to the total
        num_permutations_with_runs = (num_permutations_with_runs + num_permutations_with_run) % p
    
    # Return the number of permutations of length n with runs of length at most k, modulo p
    return (num_permutations - num_permutations_with_runs + p) % p

