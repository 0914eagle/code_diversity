
def solve(n, points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda x: x[0])

    # Initialize the minimum number of lines as 2
    min_lines = 2

    # Iterate over the sorted points
    for i in range(n - 1):
        # Get the current point and the next point
        current_point = sorted_points[i]
        next_point = sorted_points[i + 1]

        # Check if the current point and the next point are on the same line
        if current_point[1] == next_point[1]:
            # If they are, increase the minimum number of lines by 1
            min_lines += 1

    # Check if the minimum number of lines is greater than or equal to 2
    if min_lines >= 2:
        return "YES"
    else:
        return "NO"

