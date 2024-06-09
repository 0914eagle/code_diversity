
def get_min_distance(N, K, x_coords):
    # Initialize the minimum distance to infinity
    min_distance = float('inf')
    
    # Loop through all possible combinations of robots
    for i in range(2**N):
        # Convert the binary representation of i to a list of booleans
        robot_types = [bool(i & (1 << j)) for j in range(N)]
        
        # Initialize the total distance covered to 0
        total_distance = 0
        
        # Loop through each robot and calculate the distance covered
        for j in range(N):
            # If the j-th robot is type A, calculate the distance from (0, j) to (x_j, j)
            if robot_types[j]:
                total_distance += abs(x_coords[j] - j)
            # If the j-th robot is type B, calculate the distance from (K, j) to (x_j, j)
            else:
                total_distance += abs(x_coords[j] - K - j)
        
        # Update the minimum distance if the total distance covered is less than the current minimum distance
        min_distance = min(min_distance, total_distance)
    
    # Return the minimum distance
    return min_distance

def main():
    # Read the input data from stdin
    N, K = map(int, input().split())
    x_coords = list(map(int, input().split()))
    
    # Call the get_min_distance function and print the result
    print(get_min_distance(N, K, x_coords))

if __name__ == '__main__':
    main()

