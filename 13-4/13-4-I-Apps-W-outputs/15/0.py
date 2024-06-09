
def is_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables to keep track of the number of lines and their slopes
    num_lines = 0
    slopes = set()

    # Iterate through the points and check if they belong to any of the existing lines
    for point in sorted_points:
        # If the point does not belong to any of the existing lines, create a new line and add its slope to the set of slopes
        if not any(point[1] - line[1] == point[0] - line[0] for line in sorted_points):
            num_lines += 1
            slopes.add(point[1] - point[0])

    # If the number of lines is equal to the number of points, return YES, otherwise return NO
    return "YES" if num_lines == len(points) else "NO"

