
def solve(n, points):
    # Sort the points by their x-coordinates
    sorted_points = sorted(points, key=lambda point: point[0])

    # Initialize the minimum number of lines needed to cover all points as infinity
    min_lines = float('inf')

    # Iterate over all possible line combinations
    for i in range(len(sorted_points)):
        for j in range(i+1, len(sorted_points)):
            # Check if the line between the two points covers all points
            if covers_all_points(sorted_points[i], sorted_points[j], points):
                # If so, update the minimum number of lines needed
                min_lines = min(min_lines, 2)
            # If the line does not cover all points, check if it covers any points
            elif covers_any_point(sorted_points[i], sorted_points[j], points):
                # If so, update the minimum number of lines needed
                min_lines = min(min_lines, 1)

    # Return YES if the minimum number of lines needed is 1 or 2, NO otherwise
    return 'YES' if min_lines <= 2 else 'NO'

# Check if the line between two points covers all points
def covers_all_points(point1, point2, points):
    # If the x-coordinates of the two points are the same, the line will not cover all points
    if point1[0] == point2[0]:
        return False

    # Initialize the slope and y-intercept of the line
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    y_intercept = point1[1] - slope * point1[0]

    # Iterate over all points and check if they lie on the line
    for point in points:
        if point[1] != slope * point[0] + y_intercept:
            return False

    # If all points lie on the line, return True
    return True

# Check if the line between two points covers any points
def covers_any_point(point1, point2, points):
    # If the x-coordinates of the two points are the same, the line will not cover any points
    if point1[0] == point2[0]:
        return False

    # Initialize the slope and y-intercept of the line
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    y_intercept = point1[1] - slope * point1[0]

    # Iterate over all points and check if they lie on the line
    for point in points:
        if point[1] == slope * point[0] + y_intercept:
            return True

    # If no points lie on the line, return False
    return False

