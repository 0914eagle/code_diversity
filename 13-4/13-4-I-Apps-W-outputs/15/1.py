
def is_possible(n, points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables to keep track of the number of lines and the current line
    num_lines = 0
    current_line = []

    # Iterate through the sorted points
    for i in range(n):
        # If the current point is not on the current line, add it to the current line
        if sorted_points[i] not in current_line:
            current_line.append(sorted_points[i])
        # If the current point is on the current line, check if the current line is valid
        else:
            # If the current line has only one point, it is not valid
            if len(current_line) == 1:
                return "NO"
            # If the current line has more than one point, check if it is valid
            else:
                # Get the slope of the current line
                slope = (current_line[1][1] - current_line[0][1]) / (current_line[1][0] - current_line[0][0])
                # Check if the slope is equal to the slope of the previous line
                if len(current_line) > 2 and slope == (current_line[2][1] - current_line[1][1]) / (current_line[2][0] - current_line[1][0]):
                    return "NO"
                # If the current line is valid, add it to the number of lines and start a new line
                num_lines += 1
                current_line = []

    # If all the points are on at least one line, return YES
    if num_lines == n:
        return "YES"
    else:
        return "NO"

