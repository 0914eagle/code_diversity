
def is_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the minimum number of lines needed to cover all points as infinity
    min_lines = float('inf')

    # Loop through all possible line slopes (y2 - y1) / (x2 - x1)
    for slope in range(-10**9, 10**9):
        # Initialize the current line as a set of points
        current_line = set()

        # Loop through all points
        for i in range(len(sorted_points)):
            # Check if the current point is on the current line
            if sorted_points[i][1] - slope * sorted_points[i][0] in current_line:
                # If it is, add it to the current line
                current_line.add(sorted_points[i])

        # Check if the current line covers all points
        if len(current_line) >= min_lines:
            # If it does, update the minimum number of lines needed
            min_lines = len(current_line)

    # Return YES if the minimum number of lines needed is equal to the number of points, NO otherwise
    return "YES" if min_lines == len(points) else "NO"

