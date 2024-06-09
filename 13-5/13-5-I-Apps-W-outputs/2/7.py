
def solve(n, m, a, b, l, r):
    # Initialize a set to store the coordinates of the activated bombs
    activated_bombs = set()
    # Loop through each bomb and add its coordinate to the set if it is activated
    for i in range(n):
        if b[i] == 1:
            activated_bombs.add(a[i])
    
    # Initialize a set to store the coordinates of the deactivated bombs
    deactivated_bombs = set()
    # Loop through each bomb and add its coordinate to the set if it is deactivated
    for i in range(n):
        if b[i] == 0:
            deactivated_bombs.add(a[i])
    
    # Initialize a list to store the cords that should be cut
    cords_to_cut = []
    # Loop through each cord and check if it can be used to deactivate all the bombs
    for i in range(m):
        # Get the coordinates of the bombs planted between the left and right ends of the cord
        bombs_between_cord = set(range(l[i], r[i]+1))
        # Check if the coordinates of the activated bombs are a subset of the coordinates of the bombs between the cord
        if activated_bombs.issubset(bombs_between_cord):
            # If they are, add the cord to the list of cords to cut
            cords_to_cut.append(i+1)
    
    # If the list of cords to cut is empty, it is not possible to deactivate all the bombs
    if not cords_to_cut:
        return -1
    
    # Sort the list of cords to cut in ascending order
    cords_to_cut.sort()
    # Return the list of cords to cut
    return len(cords_to_cut), *cords_to_cut

