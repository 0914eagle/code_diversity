
def get_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(points):
    # Sort the points by their x-coordinate, then by their y-coordinate
    points.sort(key=lambda x: (x[0], x[1]))
    
    # Initialize the current point to (0, 0)
    current_point = (0, 0)
    
    # Initialize the total distance to 0
    total_distance = 0
    
    # Iterate through the points and visit each one
    for point in points:
        # Calculate the distance from the current point to the next point
        distance = get_distance(current_point, point)
        
        # Add the distance to the total distance
        total_distance += distance
        
        # Set the current point to the next point
        current_point = point
    
    # Return the total distance
    return total_distance

