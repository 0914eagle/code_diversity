
def is_safe_bending(wire_length, points):
    # Initialize the current position as the middle of the wire
    current_position = wire_length // 2
    
    # Iterate through the points and check if the wire will touch itself
    for point, direction in points:
        # Calculate the new position based on the direction and point
        if direction == "C":
            new_position = current_position - (point - current_position)
        else:
            new_position = current_position + (point - current_position)
        
        # Check if the new position is valid (i.e., not negative and not greater than the length of the wire)
        if new_position < 0 or new_position >= wire_length:
            return "GHOST"
        
        # Update the current position to the new position
        current_position = new_position
    
    # If the wire does not touch itself, return "SAFE"
    return "SAFE"

