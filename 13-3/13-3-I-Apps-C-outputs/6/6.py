
def is_safe_bending(wire_length, points):
    # Initialize a list to store the bending directions
    directions = []
    
    # Iterate through the points and append the bending directions to the list
    for point, direction in points:
        directions.append(direction)
    
    # Initialize a set to store the positions of the wire where it touches itself
    touching_points = set()
    
    # Iterate through the points and check if the wire touches itself at that point
    for i in range(len(points)):
        point, direction = points[i]
        if direction == "C":
            touching_points.add(point)
        else:
            touching_points.add(point - 1)
    
    # Check if the wire touches itself at any point during the bending process
    for i in range(1, len(points)):
        point1, direction1 = points[i - 1]
        point2, direction2 = points[i]
        if direction1 == "C":
            touching_points.add(point1)
        else:
            touching_points.add(point1 - 1)
        if direction2 == "C":
            touching_points.add(point2)
        else:
            touching_points.add(point2 - 1)
    
    # If the wire touches itself at any point, return "GHOST", otherwise return "SAFE"
    if len(touching_points) > 0:
        return "GHOST"
    else:
        return "SAFE"

