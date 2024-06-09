
def solve_puzzle(grid):
    # Initialize the minimum number of moves to infinity
    min_moves = float('inf')
    # Initialize the optimal solution as an empty list
    optimal_solution = []
    
    # Loop through each row of the grid
    for row in range(len(grid)):
        # Loop through each column of the grid
        for col in range(len(grid[0])):
            # Check if the current cell is equal to the target value
            if grid[row][col] == grid[0][0]:
                # If it is, add a move to select the current row to the optimal solution
                optimal_solution.append(f"row {row + 1}")
                # Add the number of moves to the minimum number of moves
                min_moves += 1
                # Break out of the inner loop
                break
    
    # Loop through each column of the grid
    for col in range(len(grid[0])):
        # Loop through each row of the grid
        for row in range(len(grid)):
            # Check if the current cell is equal to the target value
            if grid[row][col] == grid[0][0]:
                # If it is, add a move to select the current column to the optimal solution
                optimal_solution.append(f"col {col + 1}")
                # Add the number of moves to the minimum number of moves
                min_moves += 1
                # Break out of the inner loop
                break
    
    # Return the minimum number of moves and the optimal solution
    return min_moves, optimal_solution

