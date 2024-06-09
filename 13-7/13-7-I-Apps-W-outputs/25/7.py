
def is_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables for the left and right endpoints of the lines
    left_x = sorted_points[0][0]
    right_x = sorted_points[-1][0]
    left_y = sorted_points[0][1]
    right_y = sorted_points[-1][1]

    # Iterate through the points and update the left and right endpoints of the lines
    for i in range(1, len(sorted_points)):
        current_x = sorted_points[i][0]
        current_y = sorted_points[i][1]

        # If the current point is not on the line defined by the left endpoint, update the left endpoint
        if current_y != left_y:
            left_x = current_x
            left_y = current_y

        # If the current point is not on the line defined by the right endpoint, update the right endpoint
        if current_y != right_y:
            right_x = current_x
            right_y = current_y

    # Check if all points are on at least one of the lines
    for point in points:
        if point[1] < left_y or point[1] > right_y:
            return "NO"

    return "YES"

