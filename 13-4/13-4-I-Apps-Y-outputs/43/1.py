
def get_min_distance(N, K, x_coords):
    # Initialize the minimum distance to a large value
    min_distance = float('inf')
    
    # Loop through each possible combination of robots
    for i in range(2**N):
        # Convert the binary representation of i to a list of booleans
        robot_types = [bool(i & (1 << j)) for j in range(N)]
        
        # Initialize the total distance covered to 0
        total_distance = 0
        
        # Loop through each robot and calculate the distance covered
        for j in range(N):
            # If the j-th robot is type A, calculate the distance from the robot to the ball
            if robot_types[j]:
                total_distance += abs(x_coords[j] - 0)
            
            # If the j-th robot is type B, calculate the distance from the robot to the ball
            else:
                total_distance += abs(x_coords[j] - K)
        
        # Update the minimum distance if the total distance covered is smaller than the current minimum distance
        min_distance = min(min_distance, total_distance)
    
    # Return the minimum distance
    return min_distance

