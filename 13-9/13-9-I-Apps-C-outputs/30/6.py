
def solve(grid):
    # Convert the grid to a list of lists
    grid = [[int(x) for x in row] for row in grid]
    
    # Initialize the empty space coordinates
    empty_space = [0, 0]
    
    # Initialize the moves list
    moves = []
    
    # Loop through the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is empty, set the empty space coordinates
            if grid[i][j] == 0:
                empty_space = [i, j]
                break
    
    # Loop through the grid again
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current cell is not empty and is not in its correct position, make a move
            if grid[i][j] != 0 and grid[i][j] != empty_space[0] + 1:
                # If the current cell is in the first row, move it to the left or right
                if i == 0:
                    if j > 0 and grid[i][j - 1] == 0:
                        moves.append("l")
                        empty_space[1] -= 1
                    elif j < len(grid[0]) - 1 and grid[i][j + 1] == 0:
                        moves.append("r")
                        empty_space[1] += 1
                    else:
                        return "SURGERY FAILED"
                # If the current cell is in the second row, move it up or down
                elif i == 1:
                    if j > 0 and grid[i - 1][j] == 0:
                        moves.append("u")
                        empty_space[0] -= 1
                    elif j < len(grid[0]) - 1 and grid[i + 1][j] == 0:
                        moves.append("d")
                        empty_space[0] += 1
                    else:
                        return "SURGERY FAILED"
    
    # Return the moves list
    return "SURGERY COMPLETE\n" + "".join(moves)

