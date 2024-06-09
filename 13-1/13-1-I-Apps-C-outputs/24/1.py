
def solve(n, k, p):
    # Calculate the number of permutations of length n
    num_permutations = 1
    for i in range(n):
        num_permutations *= n - i
    
    # Calculate the number of permutations with runs of length k
    num_runs = 0
    for i in range(n - k + 1):
        # Check if the run is increasing
        if i % 2 == 0:
            # Increasing run
            num_runs += (n - i - k + 1)
        else:
            # Decreasing run
            num_runs += i + 1
    
    # Return the result modulo p
    return num_permutations - num_runs

