
def is_safe_bending(wire_length, points):
    # Initialize the current position as the middle of the wire
    current_position = wire_length // 2
    
    # Iterate through the points and check if the wire touches itself
    for point, direction in points:
        # Check if the point is to the left or right of the current position
        if point < current_position:
            # If the point is to the left, move left
            current_position = point
        else:
            # If the point is to the right, move right
            current_position = point + 1
        
        # Check if the current position is the same as the point
        if current_position == point:
            # If the current position is the same as the point, the wire touches itself
            return "GHOST"
    
    # If the wire does not touch itself, return SAFE
    return "SAFE"

