
def solve_tomb_raider_puzzle(n, m, floorplan):
    # Initialize a list to store the gargoyles' positions
    gargoyles = []

    # Iterate through the floorplan and find the gargoyles' positions
    for i in range(n):
        for j in range(m):
            if floorplan[i][j] == "V" or floorplan[i][j] == "H":
                gargoyles.append((i, j))

    # Initialize a variable to store the minimum number of gargoyles that need to be rotated
    min_rotations = float("inf")

    # Iterate through all possible combinations of gargoyles' rotations
    for rotation in range(len(gargoyles) + 1):
        # Initialize a list to store the current configuration of the gargoyles
        current_configuration = []

        # Iterate through the gargoyles and add their current positions to the list
        for i in range(len(gargoyles)):
            current_configuration.append(gargoyles[i])

        # Iterate through the gargoyles and rotate them by 90 degrees
        for i in range(rotation):
            current_configuration[i] = (current_configuration[i][0] + 1, current_configuration[i][1])

        # Initialize a variable to store the number of gargoyles that are facing each other
        num_facing_gargoyles = 0

        # Iterate through the gargoyles and check if they are facing each other
        for i in range(len(gargoyles)):
            for j in range(i + 1, len(gargoyles)):
                if current_configuration[i][0] == current_configuration[j][0] and current_configuration[i][1] == current_configuration[j][1]:
                    num_facing_gargoyles += 1

        # If the number of gargoyles that are facing each other is equal to the total number of gargoyles, then we have found a solution
        if num_facing_gargoyles == len(gargoyles):
            min_rotations = min(min_rotations, rotation)

    # If no solution is found, return -1
    if min_rotations == float("inf"):
        return -1

    # Otherwise, return the minimum number of gargoyles that need to be rotated
    return min_rotations

