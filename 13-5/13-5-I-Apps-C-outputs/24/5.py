
def solve(n, x):
    # Calculate the maximum distance between any two computers
    max_distance = max(x[i] - x[i-1] for i in range(1, n))
    
    # Initialize the sum
    sum = 0
    
    # Iterate over all non-empty subsets of the set of hacked computers
    for subset in range(1, 2**n):
        # Initialize the distance between all pairs of computers in the current subset
        distance = 0
        
        # Iterate over all pairs of computers in the current subset
        for i in range(n):
            for j in range(i+1, n):
                # If the current pair of computers is in the current subset, calculate the distance between them
                if subset & (1 << i) and subset & (1 << j):
                    distance = max(distance, abs(x[i] - x[j]))
        
        # Add the maximum distance between all pairs of computers in the current subset to the sum
        sum += distance
    
    # Return the sum modulo 10^9 + 7
    return sum % 1000000007

