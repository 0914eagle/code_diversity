
def solve(bombs, cords):
    # Sort the bombs by their coordinates
    bombs.sort(key=lambda x: x[0])
    
    # Initialize the set of cords to cut
    cords_to_cut = set()
    
    # Iterate through the cords
    for i in range(len(cords)):
        # Get the current cord
        cord = cords[i]
        
        # Get the range of bombs affected by the current cord
        affected_bombs = [bomb for bomb in bombs if cord[0] <= bomb[0] <= cord[1]]
        
        # If all the bombs in the range are activated, add the current cord to the set of cords to cut
        if all(bomb[1] == 1 for bomb in affected_bombs):
            cords_to_cut.add(i+1)
    
    # If all the bombs are deactivated, return -1
    if not cords_to_cut:
        return -1
    
    # Otherwise, return the set of cords to cut
    return len(cords_to_cut), *cords_to_cut

