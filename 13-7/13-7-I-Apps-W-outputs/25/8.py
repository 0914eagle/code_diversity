
def solve(n, points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda x: x[0])

    # Initialize the variables to keep track of the number of lines and the current x-coordinate
    num_lines = 0
    current_x = sorted_points[0][0]

    # Iterate through the points and check if they lie on the current line
    for i in range(1, n):
        if sorted_points[i][0] == current_x:
            num_lines += 1
        else:
            current_x = sorted_points[i][0]

    # If the number of lines is equal to the number of points, return YES, otherwise return NO
    if num_lines == n:
        return "YES"
    else:
        return "NO"

