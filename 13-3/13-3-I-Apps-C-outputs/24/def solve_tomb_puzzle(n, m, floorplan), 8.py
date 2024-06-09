
def solve_tomb_puzzle(n, m, floorplan):
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
        # Initialize a variable to store the number of gargoyles that are in the correct position
        correct_positions = 0

        # Loop through each gargoyle position
        for i in range(len(gargoyle_positions)):
            # Get the current gargoyle position
            pos = gargoyle_positions[i]

            # If the gargoyle is in the correct position, increment the number of correct positions
            if is_gargoyle_in_correct_position(pos, rotation, gargoyle_positions):
                correct_positions += 1

        # If the number of correct positions is equal to the number of gargoyles, we have found a solution
        if correct_positions == len(gargoyle_positions):
            return rotation

        # If the number of correct positions is greater than the current minimum, update the minimum
        if correct_positions < min_rotations:
            min_rotations = correct_positions

    # If we reach this point, there is no solution
    return -1

# Check if a gargoyle is in the correct position
def is_gargoyle_in_correct_position(pos, rotation, gargoyle_positions):
    # Get the x and y coordinates of the gargoyle
    x, y = pos

    # If the gargoyle is a "V" gargoyle, check if it is in the correct position for a "V" gargoyle
    if floorplan[x][y] == "V":
        # If the gargoyle is in the correct position, return True
        if rotation % 2 == 0 and x == 0 and y == 0:
            return True
        elif rotation % 2 == 1 and x == n-1 and y == m-1:
            return True
        else:
            return False

    # If the gargoyle is an "H" gargoyle, check if it is in the correct position for an "H" gargoyle
    elif floorplan[x][y] == "H":
        # If the gargoyle is in the correct position, return True
        if rotation % 2 == 0 and x == 0 and y == m-1:
            return True
        elif rotation % 2 == 1 and x == n-1 and y == 0:
            return True
        else:
            return False

    # If the gargoyle is not a "V" or "H" gargoyle, return False
    else:
        return False

