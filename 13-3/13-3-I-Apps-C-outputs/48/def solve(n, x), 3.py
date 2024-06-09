
def solve(n, x):
    # Calculate the maximum distance between any two computers
    max_distance = max(x[i] - x[i-1] for i in range(1, n))
    
    # Initialize the sum
    sum = 0
    
    # Iterate over all non-empty subsets of the set of hacked computers
    for subset in range(1, 2**n):
        # Initialize the current subset sum
        current_sum = 0
        
        # Iterate over all computers in the current subset
        for i in range(n):
            # Check if the current computer is in the subset
            if subset & (1 << i):
                # Add the distance between the current computer and the previous computer to the current subset sum
                current_sum += x[i] - x[i-1]
        
        # Add the current subset sum to the total sum
        sum += current_sum
    
    # Return the total sum modulo 10^9 + 7
    return sum % 1000000007

