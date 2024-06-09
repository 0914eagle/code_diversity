
def solve(n, k, p):
    # Calculate the number of permutations of length n with runs of length k
    num_permutations = 1
    for i in range(1, n+1):
        num_permutations = (num_permutations * (k+1-i)) % p
    
    # Calculate the number of permutations of length n with runs of length > k
    num_permutations_with_runs_gt_k = 0
    for i in range(k+1, n+1):
        num_permutations_with_runs_gt_k = (num_permutations_with_runs_gt_k + num_permutations) % p
    
    # Calculate the number of permutations of length n with runs of length at most k
    num_permutations_with_runs_le_k = (num_permutations - num_permutations_with_runs_gt_k + p) % p
    
    return num_permutations_with_runs_le_k

