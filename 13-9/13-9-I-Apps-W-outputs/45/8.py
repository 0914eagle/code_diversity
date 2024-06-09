
def rotate_lock(rotations):
    # Initialize the pointer at zero
    pointer = 0
    
    # Iterate over the rotations
    for rotation in rotations:
        # Check if the rotation is clockwise
        if rotation > 0:
            # Rotate the pointer clockwise
            pointer = (pointer + rotation) % 360
        else:
            # Rotate the pointer counterclockwise
            pointer = (pointer - rotation) % 360
    
    # Check if the pointer is back at zero
    if pointer == 0:
        return "YES"
    else:
        return "NO"

