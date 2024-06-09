
def solve(bombs, cords):
    # Sort the bombs by their coordinates
    bombs.sort(key=lambda x: x[0])
    
    # Initialize the set of cords to cut
    cords_to_cut = set()
    
    # Iterate through the cords
    for cord in cords:
        # Check if the cord intersects with any bomb
        for bomb in bombs:
            # If the cord intersects with the bomb, add the cord to the set of cords to cut
            if cord[0] <= bomb[0] <= cord[1] or cord[0] <= bomb[1] <= cord[1]:
                cords_to_cut.add(cord[2])
                break
    
    # If all the bombs are deactivated, return the set of cords to cut
    if all(bomb[1] == 0 for bomb in bombs):
        return cords_to_cut
    
    # If not all the bombs are deactivated, return -1
    return -1

