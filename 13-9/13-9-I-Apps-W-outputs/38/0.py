
def solve(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    
    # Sort the points by their x-coordinates
    points = sorted(points, key=lambda x: x[0])
    
    # Initialize the minimum number of segments to 0
    min_segments = 0
    
    # If all three points are on the same line
    if x1 == x2 == x3:
        # The minimum number of segments is 1
        min_segments = 1
    # If the first two points are on the same line and the third point is not
    elif x1 == x2 and x3 != x1:
        # The minimum number of segments is 2
        min_segments = 2
    # If the first point is on a line that passes through the third point
    elif x1 == x3 and y3 != y1:
        # The minimum number of segments is 2
        min_segments = 2
    # If the second point is on a line that passes through the third point
    elif x2 == x3 and y3 != y2:
        # The minimum number of segments is 2
        min_segments = 2
    # If the first two points are on different lines and the third point is between them
    elif x1 != x2 and x3 >= min(x1, x2) and x3 <= max(x1, x2) and y3 >= min(y1, y2) and y3 <= max(y1, y2):
        # The minimum number of segments is 3
        min_segments = 3
    # If the first two points are on different lines and the third point is not between them
    elif x1 != x2 and x3 < min(x1, x2) or x3 > max(x1, x2) or y3 < min(y1, y2) or y3 > max(y1, y2):
        # The minimum number of segments is 2
        min_segments = 2
    
    return min_segments

