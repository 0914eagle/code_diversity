
def solve(n, m, a, b, l, r):
    # Initialize a set to store the coordinates of the activated bombs
    activated_bombs = set()
    # Iterate through the list of bomb coordinates and bomb states
    for i in range(n):
        # If the bomb is activated, add its coordinate to the set
        if b[i] == 1:
            activated_bombs.add(a[i])
    
    # Initialize a list to store the cords that should be cut
    cords_to_cut = []
    # Iterate through the list of cords
    for j in range(m):
        # If the cord intersects with any activated bomb, add it to the list of cords to cut
        if any(l[j] <= x <= r[j] for x in activated_bombs):
            cords_to_cut.append(j+1)
    
    # If all bombs are deactivated, return -1
    if not activated_bombs:
        return -1
    # Otherwise, return the list of cords to cut
    return cords_to_cut

