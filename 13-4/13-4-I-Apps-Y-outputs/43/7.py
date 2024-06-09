
def get_min_distance(n, k, x_coords):
    # Initialize the minimum distance to a large value
    min_distance = float('inf')
    
    # Loop through each possible combination of robot types
    for i in range(2**n):
        # Convert the binary representation of i to a list of robot types
        robot_types = [int(j) for j in bin(i)[2:]]
        
        # Initialize the total distance covered to 0
        total_distance = 0
        
        # Loop through each robot and calculate the distance covered
        for j in range(n):
            # Calculate the distance from the robot to the ball
            distance = abs(x_coords[j] - robot_types[j] * k)
            
            # Add the distance to the total distance covered
            total_distance += distance
        
        # If the total distance covered is less than the minimum distance, update the minimum distance
        if total_distance < min_distance:
            min_distance = total_distance
    
    # Return the minimum distance
    return min_distance

def main():
    # Read the input data from stdin
    n, k = map(int, input().split())
    x_coords = list(map(int, input().split()))
    
    # Call the get_min_distance function and print the result
    print(get_min_distance(n, k, x_coords))

if __name__ == '__main__':
    main()

