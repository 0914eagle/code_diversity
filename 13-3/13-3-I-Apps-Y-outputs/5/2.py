
def solve(N, K, x_coordinates):
    # Sort the x_coordinates in ascending order
    x_coordinates.sort()
    
    # Initialize the total distance covered by robots to 0
    total_distance = 0
    
    # Loop through each x_coordinate and calculate the distance covered by the robots
    for i in range(N):
        # Calculate the distance from the robot to the ball
        distance = abs(x_coordinates[i] - i)
        
        # Add the distance to the total distance covered by robots
        total_distance += distance
    
    # Return the minimum possible total distance covered by robots
    return total_distance

