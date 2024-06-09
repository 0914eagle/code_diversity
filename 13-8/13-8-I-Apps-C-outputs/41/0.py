
def solve(N, L, x):
    # Calculate the minimum distance between two luggage positions
    min_dist = 1 + 1e-9
    
    # Initialize the maximum speed to the minimum value
    max_speed = 0.1
    
    # Iterate through all possible speeds
    for speed in range(1, 11):
        # Calculate the time it takes for each luggage to travel the length of the conveyor belt
        time = [x_i / speed for x_i in x]
        
        # Calculate the position of each luggage at the end of the conveyor belt
        pos = [x_i + time_i * speed for x_i, time_i in zip(x, time)]
        
        # Calculate the minimum distance between any two luggage positions
        dist = [abs(pos_i - pos_j) for pos_i, pos_j in combinations(pos, 2)]
        min_dist = min(min_dist, min(dist))
        
        # If the minimum distance is less than the length of the circular conveyor belt, update the maximum speed
        if min_dist < L:
            max_speed = speed
    
    # Return the maximum speed that avoids collisions
    return max_speed

