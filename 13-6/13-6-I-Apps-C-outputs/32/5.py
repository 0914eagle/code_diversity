
def solve(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations *= n - i
    
    # Calculate the number of permutations with runs of length k
    num_runs = 0
    for i in range(n - k + 1):
        # Calculate the number of permutations with a run of length k at position i
        num_runs += (n - i) * (n - i - k + 1) // 2
    
    # Return the result modulo p
    return num_runs % p

