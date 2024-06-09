
def is_safe_bending(wire_length, points):
    # Initialize a list to store the bending directions
    directions = []
    
    # Iterate over the points and append the bending directions to the list
    for point, direction in points:
        directions.append(direction)
    
    # Initialize a set to store the indices of the points that have been bended
    bended_points = set()
    
    # Iterate over the points and check if the wire will touch itself
    for i in range(len(points)):
        # Get the current point and direction
        point, direction = points[i]
        
        # Check if the point has already been bended
        if point in bended_points:
            return "GHOST"
        
        # Add the current point to the set of bended points
        bended_points.add(point)
        
        # Check if the next point is within the range of the wire
        if i + 1 < len(points):
            next_point = points[i + 1][0]
            if next_point - point > wire_length // 2:
                return "GHOST"
    
    return "SAFE"

