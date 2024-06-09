
def solve(N, L, x):
    # Calculate the minimum distance between any two luggage pieces
    min_dist = 1 + 1e-9
    
    # Loop through all possible speeds
    for v in range(10, 100):
        # Calculate the distance traveled by each luggage piece at speed v
        dist = [int(x_i / v) for x_i in x]
        
        # Calculate the minimum distance between any two luggage pieces at this speed
        curr_dist = min(dist)
        
        # If the current minimum distance is less than the previous minimum distance, update the minimum distance and the optimal speed
        if curr_dist < min_dist:
            min_dist = curr_dist
            optimal_v = v
    
    # Return the optimal speed
    return optimal_v

