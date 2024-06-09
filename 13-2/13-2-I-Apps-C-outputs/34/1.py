
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
            # If the grid is not solved, recursively call the solve function with the cloned grid as input
            else:
                solve(grid_clone)
    
    # Return the minimum number of moves and the optimal solution
    return min_moves, optimal_solution

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

# Test case 1:
grid = [[2, 2, 2, 3, 2], [0, 0, 0, 1, 0], [1, 1, 1, 2, 1]]
min_moves, optimal_solution = solve(grid)
print(min_moves)
print(optimal_solution)

# Test case 2:
grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
min_moves, optimal_solution = solve(grid)
print(min_moves)
print(optimal_solution)

# Test case 3:
grid = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
min_moves, optimal_solution = solve(grid)
print(min_moves)
print(optimal_solution)

