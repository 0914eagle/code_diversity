
def solve(wire_length, points):
    # Initialize a list to store the bends
    bends = []
    
    # Iterate through the points and directions
    for point, direction in points:
        # If the direction is clockwise, add the point to the list of bends
        if direction == "C":
            bends.append(point)
        # If the direction is counterclockwise, remove the point from the list of bends
        else:
            bends.remove(point)
    
    # Check if the list of bends is empty, if it is, return "SAFE"
    if not bends:
        return "SAFE"
    
    # If the list of bends is not empty, return "GHOST"
    return "GHOST"

