
def is_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables for the left and right endpoints of the lines
    left_endpoint = (0, 0)
    right_endpoint = (0, 0)

    # Iterate through the points and find the left and right endpoints of the lines
    for point in sorted_points:
        if point[0] < left_endpoint[0]:
            left_endpoint = point
        if point[0] > right_endpoint[0]:
            right_endpoint = point

    # Check if all points lie on at least one of the lines
    for point in sorted_points:
        if point not in [left_endpoint, right_endpoint]:
            return "NO"

    return "YES"

