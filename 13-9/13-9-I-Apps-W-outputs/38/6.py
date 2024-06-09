
def solve(x1, y1, x2, y2, x3, y3):
    # Calculate the slope of the line that passes through the first two points
    slope1 = (y2 - y1) / (x2 - x1)
    
    # Calculate the slope of the line that passes through the first and third points
    slope2 = (y3 - y1) / (x3 - x1)
    
    # If the slopes are equal, the line can be drawn as a single segment parallel to the x-axis
    if slope1 == slope2:
        return 1
    
    # If the slopes are not equal, the line can be drawn as two segments, one parallel to the x-axis and the other parallel to the y-axis
    return 2

