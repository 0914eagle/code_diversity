
def solve(n, k, p):
    # Calculate the number of permutations of length n with runs of length at most k
    num_permutations = 1
    for i in range(1, n+1):
        # Calculate the number of permutations with runs of length i
        num_runs = (k+1) * (k+2) // 2
        num_permutations = (num_permutations * num_runs) % p
    
    return num_permutations

