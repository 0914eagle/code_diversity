
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
            
            # Update the current side length if necessary
            current_side_length = min(current_side_length, get_side_length(point, points))
        
        # Update the minimum side length if necessary
        min_side_length = min(min_side_length, current_side_length)
    
    # Return the minimum side length
    return min_side_length

def get_side_length(point, points):
    # Initialize the side length to infinity
    side_length = float('inf')
    
    # Iterate over each point
    for other_point in points:
        # If the point is not the same as the current point
        if other_point != point:
            # Update the side length if necessary
            side_length = min(side_length, get_distance(point, other_point))
    
    # Return the side length
    return side_length

def get_distance(point1, point2):
    # Get the x and y coordinates of the two points
    x1, y1 = point1
    x2, y2 = point2
    
    # Calculate the distance between the two points
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    # Return the distance
    return distance

# Test the solve function
n = 3
q = 2
x = [1, 0, 1000]
y = [0, 1, 1]
a = [1, 3]
b = [3, 3]
print(solve(n, q, x, y, a, b))

