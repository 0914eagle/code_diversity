
def get_platform_positions(x_coords, y_coords, k):
    
    # Sort the points by their x coordinate
    sorted_points = sorted(zip(x_coords, y_coords))

    # Initialize the platform positions
    platform_positions = []

    # Loop through the points and add them to the platform positions
    for i in range(len(sorted_points)):
        # If the current point is not already in a platform, create a new platform for it
        if i == 0 or sorted_points[i][0] - sorted_points[i - 1][0] >= k:
            platform_positions.append((sorted_points[i][0], sorted_points[i][0] + k))
        # If the current point is already in a platform, extend the platform to include the current point
        else:
            platform_positions[-1] = (platform_positions[-1][0], sorted_points[i][0] + k)

    return platform_positions

def get_lost_points(platform_positions, x_coords, y_coords):
    
    # Initialize the number of lost points
    lost_points = 0

    # Loop through the points and check if they will be lost
    for i in range(len(x_coords)):
        # If the point is not in any platform, it will be lost
        if all(platform_positions[i] not in range(x_coords[i], x_coords[i] + k) for k in platform_positions):
            lost_points += 1

    return lost_points

def get_max_lost_points(x_coords, y_coords, k):
    
    # Get the optimal positions for the platforms
    platform_positions = get_platform_positions(x_coords, y_coords, k)

    # Get the number of lost points if the platforms are placed at the given positions
    lost_points = get_lost_points(platform_positions, x_coords, y_coords)

    return len(x_coords) - lost_points

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        x_coords = list(map(int, input().split()))
        y_coords = list(map(int, input().split()))

        # Get the maximum number of points that can be saved if both platforms are placed optimally
        max_lost_points = get_max_lost_points(x_coords, y_coords, k)

        # Print the answer
        print(max_lost_points)

if __name__ == '__main__':
    main()

