
def get_platform_coordinates(x_coordinates, y_coordinates, k):
    
    # Sort the x coordinates in increasing order
    sorted_x_coordinates = sorted(x_coordinates)

    # Initialize the platform coordinates as the first and last x coordinate
    platform_coordinates = [sorted_x_coordinates[0], sorted_x_coordinates[-1]]

    # Iterate through the x coordinates and find the optimal platform coordinates
    for i in range(1, len(sorted_x_coordinates)):
        current_x = sorted_x_coordinates[i]
        previous_x = sorted_x_coordinates[i - 1]

        # If the current x coordinate is within the platform length of the previous platform, include it in the platform
        if current_x - previous_x <= k:
            platform_coordinates[1] = current_x
        # Otherwise, start a new platform
        else:
            platform_coordinates = [current_x, current_x]

    return platform_coordinates

def get_saved_points(x_coordinates, y_coordinates, platform_coordinates):
    
    saved_points = 0

    # Iterate through the points and check if they fall within any platform
    for i in range(len(x_coordinates)):
        x = x_coordinates[i]
        y = y_coordinates[i]

        # Check if the point is within the platform
        if platform_coordinates[0] <= x <= platform_coordinates[1]:
            saved_points += 1

    return saved_points

def main():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        x_coordinates = list(map(int, input().split()))
        y_coordinates = list(map(int, input().split()))

        platform_coordinates = get_platform_coordinates(x_coordinates, y_coordinates, k)
        saved_points = get_saved_points(x_coordinates, y_coordinates, platform_coordinates)

        print(saved_points)

if __name__ == '__main__':
    main()

