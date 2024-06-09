
def solve(n, q, x, y, a, b):
    # Convert the input coordinates into a set of points
    points = set()
    for i in range(n):
        points.add((x[i], y[i]))
    
    # Initialize the minimum side length to infinity
    min_side_length = float('inf')
    
    # Iterate over each zoning request
    for i in range(q):
        # Get the start and end addresses of the request
        start, end = a[i], b[i]
        
        # Initialize the current side length to infinity
        current_side_length = float('inf')
        
        # Iterate over each point in the request
        for j in range(start, end + 1):
            # Get the current point
            point = points[j - 1]
            
            # Check if the point is on the border of the current square
            if point in points:
                # If it is, update the current side length
                current_side_length = min(current_side_length, abs(point[0]) + abs(point[1]))
        
        # Update the minimum side length
        min_side_length = min(min_side_length, current_side_length)
    
    # Return the minimum side length
    return min_side_length

