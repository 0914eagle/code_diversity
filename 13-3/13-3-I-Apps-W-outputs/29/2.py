
def solve(n, prizes):
    # Sort the prizes in ascending order
    prizes.sort()
    
    # Initialize the minimum time to collect all prizes
    min_time = 0
    
    # Iterate through the prizes
    for i in range(n):
        # Calculate the time it takes to reach the current prize
        time = abs(prizes[i] - (i + 1))
        
        # Add the time to the minimum time
        min_time += time
    
    return min_time

