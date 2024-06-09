
def solve(n, x):
    # Calculate the maximum distance between any two computers
    max_distance = max(x) - min(x)
    
    # Initialize the sum
    sum = 0
    
    # Iterate over all non-empty subsets of the set of hacked computers
    for i in range(1, 2**n):
        # Get the current subset
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(j + 1)
        
        # If the subset is not empty, calculate the maximum distance between any two computers in the subset
        if subset:
            max_distance_subset = max(x[subset[j] - 1] - x[subset[j - 1] - 1] for j in range(1, len(subset)))
            sum += max_distance_subset
    
    # Return the sum modulo 10^9 + 7
    return sum % 1000000007

