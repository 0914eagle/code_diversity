
def surgical_procedure(grid):
    # Initialize the number of organs and the empty space
    num_organs = 4 * len(grid) + 1
    empty_space = None

    # Find the empty space in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "E":
                empty_space = (i, j)
                break

    # Initialize the sequence of moves
    sequence = []

    # Loop through each organ and move it to its correct position
    for i in range(1, num_organs + 1):
        # Find the current position of the organ
        current_position = None
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                if grid[j][k] == i:
                    current_position = (j, k)
                    break

        # Move the organ to its correct position
        if current_position[0] < empty_space[0]:
            sequence.append("u")
        elif current_position[0] > empty_space[0]:
            sequence.append("d")
        elif current_position[1] < empty_space[1]:
            sequence.append("l")
        else:
            sequence.append("r")

    # Return the sequence of moves
    return "".join(sequence)

