
def is_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables for the left and right endpoints of the lines
    left_endpoint = sorted_points[0]
    right_endpoint = sorted_points[-1]

    # Iterate through the points and check if they lie on the line
    for i in range(1, len(sorted_points)):
        current_point = sorted_points[i]

        # Check if the current point lies on the line between the left and right endpoints
        if current_point[0] == left_endpoint[0] and current_point[1] == left_endpoint[1]:
            continue

        # Check if the current point lies on the line between the left and right endpoints
        if current_point[0] == right_endpoint[0] and current_point[1] == right_endpoint[1]:
            continue

        # If the current point does not lie on either line, return False
        return False

    # If all points lie on at least one of the lines, return True
    return True

