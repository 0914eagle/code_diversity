
def solve(n, points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables for the left and right endpoints of the line
    left, right = sorted_points[0], sorted_points[-1]

    # Iterate through the points and check if they lie on the line
    for point in sorted_points[1:-1]:
        # If the point does not lie on the line, return False
        if point[0] < left[0] or point[0] > right[0]:
            return "NO"

    # If all points lie on the line, return True
    return "YES"

