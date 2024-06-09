
def min_segments(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    # Sort the points by their x-coordinates
    points = sorted(points, key=lambda x: x[0])

    # Initialize the minimum number of segments to 2
    min_segments = 2

    # Iterate through the points and check if they are on the same line
    for i in range(2, len(points)):
        x1, y1 = points[i - 2]
        x2, y2 = points[i - 1]
        x3, y3 = points[i]

        # Check if the points are collinear
        if x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2) == 0:
            min_segments = 1
            break

    return min_segments

