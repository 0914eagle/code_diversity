
def solve(n, m, bombs, cords):
    # Initialize a set to store the coordinates of the bombs
    bomb_coords = set()
    for bomb in bombs:
        bomb_coords.add(bomb[0])
    
    # Initialize a set to store the coordinates of the cords
    cord_coords = set()
    for cord in cords:
        cord_coords.add(cord[0])
        cord_coords.add(cord[1])
    
    # Check if all the bombs are deactivated
    if all(bomb[1] == 0 for bomb in bombs):
        return -1
    
    # Initialize a set to store the cords that should be cut
    cut_cords = set()
    
    # Iterate over the bombs
    for bomb in bombs:
        # If the bomb is activated, find the cords that can be cut to deactivate it
        if bomb[1] == 1:
            # Find the left and right coordinates of the bomb
            left = bomb[0]
            right = bomb[0]
            while left in bomb_coords and left > 1:
                left -= 1
            while right in bomb_coords and right < 10**9:
                right += 1
            
            # Find the cords that intersect with the range of the bomb
            intersecting_cords = cord_coords.intersection(range(left, right + 1))
            
            # Add the intersecting cords to the set of cords to be cut
            cut_cords.update(intersecting_cords)
    
    # If all the bombs are deactivated, return the set of cords to be cut
    if all(bomb[1] == 0 for bomb in bombs):
        return len(cut_cords), *cut_cords
    
    # Otherwise, return -1
    return -1

