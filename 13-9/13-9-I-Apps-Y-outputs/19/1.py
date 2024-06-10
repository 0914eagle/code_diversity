
def get_platform_coordinates(x_coordinates, y_coordinates, k):
    # Sort the x_coordinates in ascending order
    x_coordinates.sort()
    
    # Initialize the platform coordinates
    platform_coordinates = []
    
    # Loop through the x_coordinates and find the optimal placement of the platforms
    for i in range(len(x_coordinates)):
        # Check if the current x_coordinate is within the range of the current platform
        if x_coordinates[i] <= k:
            # If it is, add it to the platform coordinates
            platform_coordinates.append(x_coordinates[i])
        else:
            # If it is not, add the previous x_coordinate to the platform coordinates
            platform_coordinates.append(x_coordinates[i-1])
    
    return platform_coordinates

def get_number_of_saved_points(x_coordinates, y_coordinates, platform_coordinates):
    # Initialize the number of saved points
    num_saved_points = 0
    
    # Loop through the x_coordinates and check if the point is on the platform
    for i in range(len(x_coordinates)):
        # Check if the current x_coordinate is within the range of the current platform
        if x_coordinates[i] >= platform_coordinates[0] and x_coordinates[i] <= platform_coordinates[1]:
            # If it is, increment the number of saved points
            num_saved_points += 1
    
    return num_saved_points

def main():
    t = int(input())
    
    for _ in range(t):
        n, k = map(int, input().split())
        x_coordinates = list(map(int, input().split()))
        y_coordinates = list(map(int, input().split()))
        
        # Get the optimal platform coordinates
        platform_coordinates = get_platform_coordinates(x_coordinates, y_coordinates, k)
        
        # Get the number of saved points
        num_saved_points = get_number_of_saved_points(x_coordinates, y_coordinates, platform_coordinates)
        
        # Print the answer
        print(num_saved_points)

if __name__ == '__main__':
    main()

