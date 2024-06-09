
def solve(x1, y1, x2, y2, x3, y3):
    # Calculate the distance between the points
    d1 = abs(x2 - x1) + abs(y2 - y1)
    d2 = abs(x3 - x2) + abs(y3 - y2)
    d3 = abs(x1 - x3) + abs(y1 - y3)

    # Return the minimum number of segments
    return min(d1, d2, d3)

