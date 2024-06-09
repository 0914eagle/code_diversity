
def solve(n, q, x, y, a, b):
    # Convert the input coordinates into a set of points
    points = set()
    for i in range(n):
        points.add((x[i], y[i]))
    
    # Initialize the minimum side length to infinity
    min_side_length = float('inf')
    
    # Iterate over each zoning request
    for i in range(q):
        # Find the bounding box of the request
        min_x = min(x[a[i] - 1], x[b[i] - 1])
        max_x = max(x[a[i] - 1], x[b[i] - 1])
        min_y = min(y[a[i] - 1], y[b[i] - 1])
        max_y = max(y[a[i] - 1], y[b[i] - 1])
        
        # Calculate the side length of the bounding box
        side_length = max_x - min_x
        if side_length < min_side_length:
            min_side_length = side_length
        
        # Check if the request is a square
        if side_length == max_y - min_y:
            return min_side_length
    
    # If the request is not a square, return the minimum side length
    return min_side_length

