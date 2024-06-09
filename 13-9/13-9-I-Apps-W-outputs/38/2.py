
def solve(x1, y1, x2, y2, x3, y3):
    # Calculate the slopes of the lines passing through the points
    m1 = (y2 - y1) / (x2 - x1)
    m2 = (y3 - y1) / (x3 - x1)

    # If the slopes are equal, the points are collinear, and the minimum number of segments is 2
    if m1 == m2:
        return 2

    # If the slopes are not equal, the minimum number of segments is 3
    return 3

