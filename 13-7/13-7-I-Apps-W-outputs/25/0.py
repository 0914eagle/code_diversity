
def is_possible(points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables to keep track of the lines
    line1 = []
    line2 = []

    # Iterate through the points and add them to either line1 or line2
    for i in range(len(sorted_points)):
        if i % 2 == 0:
            line1.append(sorted_points[i])
        else:
            line2.append(sorted_points[i])

    # Check if all points have been assigned to at least one line
    if len(line1) + len(line2) == len(points):
        return "YES"
    else:
        return "NO"

