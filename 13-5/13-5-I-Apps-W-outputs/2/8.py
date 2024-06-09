
def solve(bombs, cords):
    # Sort the bombs by their coordinates
    bombs.sort(key=lambda x: x[0])
    
    # Initialize the set of cords to cut
    cords_to_cut = set()
    
    # Iterate through the cords
    for cord in cords:
        # Find the range of bombs that are affected by this cord
        affected_bombs = [bomb for bomb in bombs if cord[0] <= bomb[0] <= cord[1]]
        
        # If all the affected bombs are deactivated, add this cord to the set of cords to cut
        if all(bomb[1] == 0 for bomb in affected_bombs):
            cords_to_cut.add(cord[2])
    
    # If all the bombs are deactivated, return the set of cords to cut
    if all(bomb[1] == 0 for bomb in bombs):
        return cords_to_cut
    
    # Otherwise, return -1
    return -1

