
def is_valid_move(grid, row, col, direction):
    # Check if the move is valid
    if direction == "u":
        if row == 0:
            return False
        if grid[row - 1][col] != "E":
            return False
    elif direction == "d":
        if row == len(grid) - 1:
            return False
        if grid[row + 1][col] != "E":
            return False
    elif direction == "l":
        if col == 0:
            return False
        if grid[row][col - 1] != "E":
            return False
    elif direction == "r":
        if col == len(grid[0]) - 1:
            return False
        if grid[row][col + 1] != "E":
            return False
    return True

def get_valid_moves(grid, row, col):
    # Get all valid moves from the current position
    valid_moves = []
    if is_valid_move(grid, row, col, "u"):
        valid_moves.append("u")
    if is_valid_move(grid, row, col, "d"):
        valid_moves.append("d")
    if is_valid_move(grid, row, col, "l"):
        valid_moves.append("l")
    if is_valid_move(grid, row, col, "r"):
        valid_moves.append("r")
    return valid_moves

def solve(grid):
    # Initialize the solution grid
    solution_grid = []
    for row in grid:
        solution_grid.append(row.copy())

    # Initialize the current position
    current_row, current_col = 0, 0
    while True:
        # Get the current organ
        current_organ = solution_grid[current_row][current_col]

        # If the current organ is not an integer, we have reached the end of the solution
        if not current_organ.isdigit():
            break

        # Get all valid moves from the current position
        valid_moves = get_valid_moves(solution_grid, current_row, current_col)

        # If there are no valid moves, the solution is not possible
        if len(valid_moves) == 0:
            return False

        # Choose a random valid move
        move = valid_moves[0]

        # Make the move
        if move == "u":
            current_row -= 1
        elif move == "d":
            current_row += 1
        elif move == "l":
            current_col -= 1
        elif move == "r":
            current_col += 1

        # Update the solution grid
        solution_grid[current_row][current_col] = current_organ
        solution_grid[current_row + (move == "u")][current_col + (move == "l")] = "E"

    # If we reach this point, the solution is possible
    return solution_grid

def main():
    # Read the input
    t = int(input())
    for _ in range(t):
        k = int(input())
        grid = []
        for _ in range(2 * k + 1):
            grid.append(list(input()))

        # Solve the problem
        solution_grid = solve(grid)

        # Check if the solution is possible
        if solution_grid:
            print("SURGERY COMPLETE")
            for row in solution_grid:
                print("".join(row))
        else:
            print("SURGERY FAILED")

if __name__ == '__main__':
    main()

