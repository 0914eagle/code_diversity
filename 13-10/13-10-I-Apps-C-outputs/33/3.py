
def get_rectangular_area_points(n, points):
    
    # Sort the points by their x-coordinate
    points.sort(key=lambda x: x[0])

    # Initialize the number of different non-empty sets to 0
    num_sets = 0

    # Iterate through the points
    for i in range(n):
        # Get the current point
        current_point = points[i]

        # Get the x-coordinate of the current point
        current_x = current_point[0]

        # Get the number of points to the right of the current point
        num_points_right = n - i - 1

        # Iterate through the points to the right of the current point
        for j in range(num_points_right):
            # Get the point to the right of the current point
            right_point = points[i + j + 1]

            # Get the x-coordinate of the point to the right of the current point
            right_x = right_point[0]

            # Check if the point to the right of the current point is in the rectangular area
            if right_x <= current_x:
                break

            # Get the y-coordinate of the point to the right of the current point
            right_y = right_point[1]

            # Check if the point to the right of the current point is above the line x = current_x
            if right_y <= current_x:
                break

            # Increment the number of different non-empty sets
            num_sets += 1

    return num_sets

def main():
    # Read the number of points from stdin
    n = int(input())

    # Read the coordinates of the points from stdin
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))

    # Call the function to get the number of different non-empty sets
    num_sets = get_rectangular_area_points(n, points)

    # Print the number of different non-empty sets
    print(num_sets)

if __name__ == '__main__':
    main()

