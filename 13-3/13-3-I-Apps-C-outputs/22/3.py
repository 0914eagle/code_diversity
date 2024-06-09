
def solve(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations = (num_permutations * (n - i)) % p
    
    # Calculate the number of permutations with runs of length k
    num_runs = 0
    for i in range(n - k + 1):
        # Calculate the number of runs of length k starting at position i
        num_runs_i = 1
        for j in range(i + 1, i + k):
            if j < n and (j == i or j % 2 == 1):
                num_runs_i = (num_runs_i * 2) % p
        num_runs = (num_runs + num_runs_i) % p
    
    # Calculate the number of permutations with runs of length at most k
    return (num_permutations - num_runs + p) % p

