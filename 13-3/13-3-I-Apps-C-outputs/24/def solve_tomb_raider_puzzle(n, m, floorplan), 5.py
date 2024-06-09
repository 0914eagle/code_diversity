
def solve_tomb_raider_puzzle(n, m, floorplan):
    # Initialize a list to store the gargoyle positions
    gargoyle_positions = []

    # Loop through each row of the floorplan
    for i in range(n):
        # Loop through each column of the floorplan
        for j in range(m):
            # If the current cell is a gargoyle, add its position to the list
            if floorplan[i][j] in ["V", "H"]:
                gargoyle_positions.append((i, j))

    # Initialize a variable to store the minimum number of gargoyles that need to be rotated
    min_rotations = float("inf")

    # Loop through each possible rotation of the gargoyles
    for rotation in range(4):
        # Initialize a variable to store the number of gargoyles that are facing the correct direction
        correct_gargoyles = 0

        # Loop through each gargoyle position
        for i, j in gargoyle_positions:
            # If the gargoyle is facing the correct direction, increment the number of correct gargoyles
            if floorplan[i][j] == "V" and rotation % 2 == 0:
                correct_gargoyles += 1
            elif floorplan[i][j] == "H" and rotation % 2 == 1:
                correct_gargoyles += 1

        # If the number of correct gargoyles is equal to the number of gargoyles, we have found a solution
        if correct_gargoyles == len(gargoyle_positions):
            return rotation

        # If the number of correct gargoyles is greater than the current minimum, update the minimum
        if correct_gargoyles < min_rotations:
            min_rotations = correct_gargoyles

    # If no solution is found, return -1
    return -1

