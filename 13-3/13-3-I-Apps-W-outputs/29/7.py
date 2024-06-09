
def solve(n, prizes):
    # Sort the prizes in ascending order
    prizes.sort()
    
    # Initialize the minimum time to collect all prizes
    min_time = 0
    
    # Iterate through the prizes
    for i in range(n):
        # Calculate the distance between the current prize and the previous prize
        distance = abs(prizes[i] - prizes[i-1]) if i > 0 else 1
        
        # Add the distance to the minimum time
        min_time += distance
    
    return min_time

