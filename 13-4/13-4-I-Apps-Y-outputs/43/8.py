
def get_min_distance(N, K, x_coordinates):
    # Initialize the minimum distance to a large value
    min_distance = float('inf')
    
    # Loop through each possible combination of robot types
    for i in range(2**N):
        # Convert the binary representation of i to a list of robot types
        robot_types = [int(j) for j in bin(i)[2:]]
        
        # Initialize the total distance covered to 0
        total_distance = 0
        
        # Loop through each robot and calculate the distance covered
        for j in range(N):
            # If the j-th robot is of type A, calculate the distance from the robot to the ball
            if robot_types[j] == 0:
                total_distance += abs(x_coordinates[j] - 0)
            # If the j-th robot is of type B, calculate the distance from the robot to the ball
            else:
                total_distance += abs(x_coordinates[j] - K)
        
        # If the total distance covered is less than the minimum distance, update the minimum distance
        if total_distance < min_distance:
            min_distance = total_distance
    
    # Return the minimum distance
    return min_distance

