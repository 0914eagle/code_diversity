
def is_safe_bending(wire_length, points):
    # Initialize a list to store the bends
    bends = []

    # Iterate through the points and directions
    for point, direction in points:
        # Check if the bend would cause the wire to touch itself
        if direction == "C" and point in bends:
            return "GHOST"
        # Add the bend to the list
        bends.append(point)

    # If the wire does not touch itself, return "SAFE"
    return "SAFE"

