
def solve(n, m, bombs, cords):
    # Initialize a set to store the indices of the bombs that are activated
    activated_bombs = set()

    # Iterate over the bombs and add the indices of the activated bombs to the set
    for i in range(n):
        if bombs[i][1] == 1:
            activated_bombs.add(i)

    # Initialize a list to store the cords that should be cut
    cords_to_cut = []

    # Iterate over the cords and check if cutting the cord will deactivate all the bombs
    for i in range(m):
        # Get the coordinates of the cord
        left, right = cords[i]

        # Initialize a set to store the indices of the bombs that will be switched by cutting the cord
        switched_bombs = set()

        # Iterate over the bombs and check if they are between the coordinates of the cord
        for j in range(n):
            if left <= bombs[j][0] <= right:
                switched_bombs.add(j)

        # Check if the set of switched bombs is a subset of the set of activated bombs
        if switched_bombs.issubset(activated_bombs):
            cords_to_cut.append(i + 1)

    # If all the bombs are deactivated, return the list of cords to cut
    if len(activated_bombs) == 0:
        return cords_to_cut

    # Otherwise, return -1
    return -1

