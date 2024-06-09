
def solve(R, C, K, grid, a):
    # Initialize the maximum score to 0
    max_score = 0
    # Loop through all possible directions for the conveyor belts
    for dir1 in ["R", "L"]:
        for dir2 in ["R", "L"]:
            # Set the directions for the conveyor belts
            grid[0] = dir1 * C
            grid[R-1] = dir2 * C
            # Initialize the current score to 0
            current_score = 0
            # Initialize the current position to (0, 0)
            current_pos = (0, 0)
            # Initialize the number of cells visited to 0
            cells_visited = 0
            # Loop through the rows of the grid
            for i in range(R):
                # Loop through the columns of the current row
                for j in range(C):
                    # If the current cell is empty, move the ball to the next cell
                    if grid[i][j] == ".":
                        current_pos = (i, j+1)
                    # If the current cell is an obstacle, the exam ends
                    elif grid[i][j] == "X":
                        break
                    # If the current cell is a conveyor belt, move the ball accordingly
                    elif grid[i][j] == "R":
                        current_pos = (i, j+1)
                    elif grid[i][j] == "L":
                        current_pos = (i, j-1)
                    # If the current cell is a cell with points, add the score to the current score
                    elif grid[i][j].isdigit():
                        current_score += int(grid[i][j])
                    # If the current cell is not empty, an obstacle, a conveyor belt, or a cell with points, the exam ends
                    else:
                        break
                    # Increment the number of cells visited
                    cells_visited += 1
                    # If the number of cells visited exceeds 10^20, the exam ends
                    if cells_visited > 10**20:
                        break
                # If the exam has ended, break out of the loop
                if current_pos[1] == -1 or current_pos[1] == C:
                    break
            # If the exam has not ended and the current score is higher than the maximum score, update the maximum score
            if current_pos[1] != -1 and current_pos[1] != C and current_score > max_score:
                max_score = current_score
    # Return the maximum score
    return max_score

