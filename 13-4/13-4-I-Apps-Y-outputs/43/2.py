
def get_min_distance(N, K, x_coords):
    # Initialize the minimum distance to a large value
    min_distance = float('inf')
    
    # Loop through all possible combinations of robots
    for i in range(2**N):
        # Convert the binary representation of i to a list of booleans
        robot_types = [bool(i & (1 << j)) for j in range(N)]
        
        # Initialize the total distance covered to 0
        total_distance = 0
        
        # Loop through all balls and robots
        for j in range(N):
            # If the j-th robot is type A, calculate the distance from the robot to the ball
            if robot_types[j]:
                distance = abs(x_coords[j] - 0)
            # If the j-th robot is type B, calculate the distance from the robot to the ball
            else:
                distance = abs(x_coords[j] - K)
            
            # Add the distance to the total distance covered
            total_distance += distance
        
        # If the total distance covered is less than the minimum distance, update the minimum distance
        if total_distance < min_distance:
            min_distance = total_distance
    
    # Return the minimum distance
    return min_distance

def main():
    # Read the input data
    N, K = map(int, input().split())
    x_coords = list(map(int, input().split()))
    
    # Calculate the minimum distance
    min_distance = get_min_distance(N, K, x_coords)
    
    # Print the minimum distance
    print(min_distance)

if __name__ == '__main__':
    main()

