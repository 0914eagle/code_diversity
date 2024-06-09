
def solve(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations = (num_permutations * (n - i)) % p
    
    # Calculate the number of permutations with runs of length k
    num_runs = 0
    for i in range(n - k + 1):
        # Calculate the number of permutations with a run of length k starting at position i
        num_runs_at_i = 1
        for j in range(i + 1, i + k):
            num_runs_at_i = (num_runs_at_i * (n - j + 1)) % p
        num_runs = (num_runs + num_runs_at_i) % p
    
    # Calculate the number of permutations with runs of length less than k
    num_permutations_with_runs = (num_permutations - num_runs) % p
    
    return num_permutations_with_runs

