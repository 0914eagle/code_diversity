
def solve(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations *= n - i
    
    # Initialize the number of permutations with runs of length k or less
    num_permutations_with_runs = 0
    
    # Iterate through all possible runs of length k or less
    for i in range(k + 1):
        # Calculate the number of permutations with exactly i runs of length k or less
        num_permutations_with_i_runs = 1
        for j in range(i):
            num_permutations_with_i_runs *= n - j
        
        # Add the number of permutations with exactly i runs of length k or less to the total
        num_permutations_with_runs += num_permutations_with_i_runs
    
    # Return the number of permutations with runs of length k or less, modulo p
    return num_permutations_with_runs % p

