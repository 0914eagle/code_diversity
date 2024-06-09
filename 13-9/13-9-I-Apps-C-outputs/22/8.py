
def is_loop_possible(points):
    # Sort the points by their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the previous and next points
    previous_point = sorted_points[0]
    next_point = sorted_points[1]

    # Iterate through the points and check if they form a valid loop
    for i in range(2, len(sorted_points)):
        current_point = sorted_points[i]

        # Check if the current point is aligned with the previous and next points
        if current_point[0] != previous_point[0] and current_point[0] != next_point[0]:
            return False

        # Check if the current point is between the previous and next points
        if current_point[0] < previous_point[0] or current_point[0] > next_point[0]:
            return False

        # Update the previous and next points
        previous_point = current_point
        next_point = sorted_points[i + 1]

    # Check if the first and last points are the same
    if previous_point != sorted_points[0]:
        return False

    return True

