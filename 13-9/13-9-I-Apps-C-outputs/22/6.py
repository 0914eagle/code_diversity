
def is_loop_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a dictionary to keep track of the points that have been visited
    visited = {}

    # Initialize the current point to the first point in the list
    current_point = sorted_points[0]

    # Loop through the points and check if it is possible to form a loop
    for i in range(1, len(sorted_points)):
        # If the current point has already been visited, return False
        if current_point in visited:
            return False

        # If the current point is not the same as the previous point, check if it is possible to form a perpendicular line segment
        if current_point != sorted_points[i]:
            # If the current point is not on the same axis as the previous point, check if it is possible to form a perpendicular line segment
            if current_point[0] != sorted_points[i][0] and current_point[1] != sorted_points[i][1]:
                return False

        # Add the current point to the visited dictionary
        visited[current_point] = True

        # Set the current point to the next point in the list
        current_point = sorted_points[i]

    # If all the points have been visited and the first and last points are the same, return True
    if len(visited) == len(points) and current_point == sorted_points[0]:
        return True

    # Otherwise, return False
    return False

