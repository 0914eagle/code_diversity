
def solve(n, x):
    # Calculate the maximum distance between any two computers
    max_distance = max(x[i] - x[i-1] for i in range(1, n))
    
    # Initialize the sum
    sum = 0
    
    # Iterate over all non-empty subsets of the set of hacked computers
    for subset in range(1, 2**n):
        # Initialize the current subset
        current_subset = []
        
        # Iterate over all bits in the binary representation of the subset
        for i in range(n):
            # If the i-th bit is set, add the i-th computer to the current subset
            if subset & (1 << i):
                current_subset.append(i+1)
                
        # If the current subset is not empty, calculate the maximum distance between any two computers in the subset
        if current_subset:
            max_distance_subset = max(x[current_subset[i]] - x[current_subset[i-1]] for i in range(1, len(current_subset)))
            
            # Add the maximum distance to the sum
            sum += max_distance_subset
    
    # Return the sum modulo 10^9 + 7
    return sum % 1000000007

