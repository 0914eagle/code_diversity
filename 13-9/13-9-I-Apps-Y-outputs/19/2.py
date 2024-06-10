
def get_platform_coordinates(x_coordinates, y_coordinates, platform_length):
    # Sort the x-coordinates in ascending order
    sorted_x_coordinates = sorted(x_coordinates)

    # Initialize the platform coordinates as empty lists
    left_platform_coordinates = []
    right_platform_coordinates = []

    # Iterate through the sorted x-coordinates
    for i in range(len(sorted_x_coordinates)):
        # Check if the current x-coordinate is within the platform length from the previous x-coordinate
        if i > 0 and sorted_x_coordinates[i] - sorted_x_coordinates[i - 1] <= platform_length:
            # If so, add the current x-coordinate to the left platform coordinates
            left_platform_coordinates.append(sorted_x_coordinates[i])
        else:
            # If not, add the current x-coordinate to the right platform coordinates
            right_platform_coordinates.append(sorted_x_coordinates[i])

    # Return the platform coordinates as a tuple of lists
    return (left_platform_coordinates, right_platform_coordinates)

def get_saved_points(x_coordinates, y_coordinates, platform_coordinates):
    # Initialize the saved points as an empty set
    saved_points = set()

    # Iterate through the x-coordinates and y-coordinates
    for i in range(len(x_coordinates)):
        # Check if the current point is within the platform coordinates
        if platform_coordinates[0][0] <= x_coordinates[i] <= platform_coordinates[0][-1] and y_coordinates[i] >= 0:
            # If so, add the current point to the saved points
            saved_points.add((x_coordinates[i], y_coordinates[i]))

    # Return the saved points as a list
    return list(saved_points)

def get_maximum_saved_points(x_coordinates, y_coordinates, platform_length):
    # Get the platform coordinates for the given x-coordinates and platform length
    platform_coordinates = get_platform_coordinates(x_coordinates, platform_length)

    # Get the saved points for the given x-coordinates and platform coordinates
    saved_points = get_saved_points(x_coordinates, y_coordinates, platform_coordinates)

    # Return the maximum number of saved points
    return len(saved_points)

def main():
    # Read the number of test cases
    num_test_cases = int(input())

    # Iterate through the test cases
    for test_case in range(num_test_cases):
        # Read the number of points and platform length
        n, k = map(int, input().split())

        # Read the x-coordinates and y-coordinates of the points
        x_coordinates = list(map(int, input().split()))
        y_coordinates = list(map(int, input().split()))

        # Get the maximum number of saved points for the given points and platform length
        maximum_saved_points = get_maximum_saved_points(x_coordinates, y_coordinates, k)

        # Print the maximum number of saved points
        print(maximum_saved_points)

if __name__ == '__main__':
    main()

