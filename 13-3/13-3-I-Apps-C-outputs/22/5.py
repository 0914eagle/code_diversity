
def solve(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations = (num_permutations * (n - i)) % p
    
    # Initialize the number of permutations with runs of length k
    num_runs = 0
    
    # Iterate through each possible run length
    for run_length in range(1, k + 1):
        # Calculate the number of runs of length run_length
        num_runs_of_length = 1
        for i in range(n - run_length):
            num_runs_of_length = (num_runs_of_length * (n - i - run_length + 1)) % p
        
        # Add the number of runs of length run_length to the total
        num_runs = (num_runs + num_runs_of_length) % p
    
    # Return the number of permutations with runs of length at most k
    return num_permutations - num_runs

