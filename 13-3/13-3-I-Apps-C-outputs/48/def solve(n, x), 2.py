
def solve(n, x):
    # Calculate the maximum distance between any two computers
    max_dist = max(x) - min(x)
    
    # Initialize the sum
    sum = 0
    
    # Iterate over all non-empty subsets of the set of hacked computers
    for subset in range(1, 2**n):
        # Initialize the maximum distance within the subset
        max_subset_dist = 0
        
        # Iterate over all pairs of computers in the subset
        for i in range(n):
            for j in range(i+1, n):
                # If the computers are in the subset, calculate the distance between them
                if subset & (1 << i) and subset & (1 << j):
                    subset_dist = abs(x[i] - x[j])
                    
                    # Update the maximum distance within the subset
                    max_subset_dist = max(max_subset_dist, subset_dist)
                    
        # Add the maximum distance within the subset to the sum
        sum += max_subset_dist
    
    # Return the sum modulo 10^9 + 7
    return sum % 1000000007

