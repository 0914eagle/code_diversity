
def solve(grid):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Initialize the optimal solution as an empty list
    optimal_solution = []
    
    # Loop through each possible move (row or column)
    for move in range(1, len(grid) + 1):
        # Check if the move is valid (i.e., the move is within the bounds of the grid)
        if move <= len(grid):
            # Clone the grid to prevent modifying the original grid
            grid_clone = grid.copy()
            # Perform the move by adding 1 to all cells in the selected row or column
            for i in range(len(grid_clone)):
                if move == 1:
                    grid_clone[i][move - 1] += 1
                else:
                    grid_clone[move - 1][i] += 1
            # Check if the grid is solved after the move
            if is_solved(grid_clone):
                # If the grid is solved, calculate the number of moves required
                num_moves = len(grid_clone)
                # If the number of moves is less than the minimum number of moves, update the minimum number of moves and the optimal solution
                if num_moves < min_moves:
                    min_moves = num_moves
                    optimal_solution = [move]
            # If the grid is not solved, recursively call the solve function to find the optimal solution
            else:
                solution = solve(grid_clone)
                # If a solution is found, add the move to the solution and update the minimum number of moves
                if solution:
                    solution.insert(0, move)
                    min_moves = len(solution)
                    optimal_solution = solution
    
    # Return the optimal solution
    return optimal_solution

# Check if the grid is solved
def is_solved(grid):
    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the cell value is not equal to the target value, return False
            if grid[i][j] != grid[0][0]:
                return False
    # If all cells are equal to the target value, return True
    return True

# Test the solve function
grid = [[2, 2, 2, 3, 2], [0, 0, 0, 1, 0], [1, 1, 1, 2, 1]]
print(solve(grid))

