
def solve(x1, y1, x2, y2, x3, y3):
    # Calculate the slope of the line that passes through the first two points
    m1 = (y2-y1)/(x2-x1)
    # Calculate the slope of the line that passes through the first and third points
    m2 = (y3-y1)/(x3-x1)
    # If the slopes are equal, the polyline can be a single segment
    if m1 == m2:
        return 1
    # If the slopes are not equal, the polyline must consist of at least two segments
    else:
        return 2

