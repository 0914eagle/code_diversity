
def get_min_segments(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    # Sort the points by their x-coordinate
    points = sorted(points, key=lambda x: x[0])

    # Initialize the minimum number of segments to 2
    min_segments = 2

    # Check if the points are collinear
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        # If the points are collinear, return 1 segment
        return 1

    # Check if the points are on the same line
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        # If the points are on the same line, return 1 segment
        return 1

    # Check if the points are in a straight line
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        # If the points are in a straight line, return 2 segments
        return 2

    # Check if the points are in a straight line
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        # If the points are in a straight line, return 2 segments
        return 2

    # Check if the points are in a straight line
    if (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0:
        # If the points are in a straight line, return 2 segments
        return 2

    # If the points are not in a straight line, return 3 segments
    return 3

