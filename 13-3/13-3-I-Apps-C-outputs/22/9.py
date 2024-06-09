
def solve(n, k, p):
    # Calculate the number of permutations of length n with runs of length at most k
    num_permutations = 1
    for i in range(1, n+1):
        # Calculate the number of permutations with a run of length i
        num_permutations_with_run = (i * (i+1)) // 2
        # If the run length is greater than k, break the loop
        if i > k:
            break
        # Add the number of permutations with a run of length i to the total
        num_permutations += num_permutations_with_run
    
    # Return the result modulo p
    return num_permutations % p

