
def solve(points):
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]
    
    # Sort the points by their x-coordinates
    points = sorted(points, key=lambda x: x[0])
    
    # Initialize the minimum number of segments to 3
    min_segments = 3
    
    # Iterate over the points and calculate the slope of the line segment between them
    for i in range(3):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        slope = (y2-y1)/(x2-x1)
        
        # If the slope is infinite, set the minimum number of segments to 2
        if slope == float('inf') or slope == float('-inf'):
            min_segments = 2
            break
    
    return min_segments

