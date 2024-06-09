
def solve(K, N):
    # Initialize a list to store the results
    results = []
    
    # Loop through each possible sum
    for i in range(1, 2*K+1):
        # Initialize a count variable to store the number of combinations
        count = 0
        
        # Loop through each possible combination of dice
        for dice in itertools.combinations(range(1, K+1), N):
            # Check if the sum of the dice is equal to the current sum
            if sum(dice) == i:
                # Increment the count
                count += 1
        
        # Add the count to the results list
        results.append(count)
    
    # Return the results list
    return results

