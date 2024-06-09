
def solve(n, points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the variables to keep track of the lines
    line1 = []
    line2 = []

    # Iterate through the points and add them to either line1 or line2
    for i in range(n):
        if i % 2 == 0:
            line1.append(sorted_points[i])
        else:
            line2.append(sorted_points[i])

    # Check if all points are on at least one of the lines
    for point in sorted_points:
        if point not in line1 and point not in line2:
            return "NO"

    return "YES"

