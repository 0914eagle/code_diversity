
import math

def generate_convex_polygon(n):
    # Validate input
    if n < 3:
        raise ValueError("Number of vertices must be at least 3")
    if n > 400000:
        raise ValueError("Number of vertices must be less than 400000")
    
    # Initialize the polygon with the first vertex at (0, 0)
    polygon = [(0, 0)]
    
    # Iterate until the polygon has the desired number of vertices
    while len(polygon) < n:
        # Generate a random integer in the range [1, 400000]
        x = math.floor(math.random() * 400000)
        y = math.floor(math.random() * 400000)
        
        # Check if the point is not already in the polygon
        if (x, y) not in polygon:
            # Add the point to the polygon
            polygon.append((x, y))
    
    return polygon

