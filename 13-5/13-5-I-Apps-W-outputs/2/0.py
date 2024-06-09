
def solve(bombs, cords):
    # Sort the bombs by their coordinates
    bombs.sort(key=lambda x: x[0])
    
    # Initialize a set to store the cords that should be cut
    cut_cords = set()
    
    # Iterate through the cords
    for cord in cords:
        # Check if the cord intersects with any of the bombs
        for bomb in bombs:
            # If the cord intersects with the bomb, switch the state of the bomb
            if cord[0] <= bomb[0] <= cord[1] or cord[0] <= bomb[1] <= cord[1]:
                bomb[1] = 1 - bomb[1]
                break
        # Add the cord to the set of cords that should be cut
        cut_cords.add(cord)
    
    # Return the set of cords that should be cut
    return cut_cords

