
def get_platform_coordinates(x_coordinates, k):
    # Find the minimum and maximum x-coordinates
    min_x = min(x_coordinates)
    max_x = max(x_coordinates)
    
    # Calculate the number of platforms that can be placed
    num_platforms = (max_x - min_x) // k
    
    # Initialize a list to store the platform coordinates
    platform_coordinates = []
    
    # Loop through the number of platforms and calculate their coordinates
    for i in range(num_platforms):
        platform_coordinates.append((min_x + i * k, min_x + (i + 1) * k - 1))
    
    return platform_coordinates

def get_points_in_platform(platform_coordinates, x_coordinates, y_coordinates):
    # Initialize a list to store the points in the platform
    points_in_platform = []
    
    # Loop through the platform coordinates and check if the points are in the platform
    for platform in platform_coordinates:
        for i in range(len(x_coordinates)):
            if platform[0] <= x_coordinates[i] <= platform[1] and y_coordinates[i] == platform[0]:
                points_in_platform.append((x_coordinates[i], y_coordinates[i]))
    
    return points_in_platform

def get_points_lost(platform_coordinates, x_coordinates, y_coordinates):
    # Initialize a list to store the points that will be lost
    points_lost = []
    
    # Loop through the platform coordinates and check if the points will be lost
    for platform in platform_coordinates:
        for i in range(len(x_coordinates)):
            if platform[0] <= x_coordinates[i] <= platform[1] and y_coordinates[i] != platform[0]:
                points_lost.append((x_coordinates[i], y_coordinates[i]))
    
    return points_lost

def get_maximum_points(platform_coordinates, x_coordinates, y_coordinates):
    # Get the points in the platform
    points_in_platform = get_points_in_platform(platform_coordinates, x_coordinates, y_coordinates)
    
    # Get the points that will be lost
    points_lost = get_points_lost(platform_coordinates, x_coordinates, y_coordinates)
    
    # Return the maximum number of points that can be saved
    return len(points_in_platform) + len(points_lost)

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        x_coordinates = list(map(int, input().split()))
        y_coordinates = list(map(int, input().split()))
        
        # Get the platform coordinates
        platform_coordinates = get_platform_coordinates(x_coordinates, k)
        
        # Get the maximum number of points that can be saved
        maximum_points = get_maximum_points(platform_coordinates, x_coordinates, y_coordinates)
        
        # Print the answer
        print(maximum_points)

if __name__ == '__main__':
    main()

