
def solve(n, m, t, op):
    # Initialize a 2D array to store the grid
    grid = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill in the grid with the given values
    for i in range(m):
        r, c = map(int, input().split())
        grid[r-1][c-1] = i+1
    
    # Use recursion to find all possible combinations of numbers that satisfy the conditions
    return count_combinations(grid, t, op)

def count_combinations(grid, t, op):
    # Base case: if the grid is empty, return 1 if the target is 0, and 0 otherwise
    if not grid:
        return 1 if t == 0 else 0
    
    # Initialize the number of combinations to 0
    combinations = 0
    
    # Iterate over all possible values for the current grid square
    for i in range(1, len(grid)+1):
        # If the value is valid (i.e., it doesn't appear in the same row or column), recurse with the updated grid and target
        if is_valid(grid, i, op):
            combinations += count_combinations(update_grid(grid, i), t-i, op)
    
    # Return the number of combinations
    return combinations

def is_valid(grid, value, op):
    # Check if the value appears in the same row
    for row in grid:
        if value in row:
            return False
    
    # Check if the value appears in the same column
    for i in range(len(grid)):
        if value == grid[i][i]:
            return False
    
    # Check if the value appears in the same diagonal
    for i in range(len(grid)):
        if value == grid[i][len(grid)-i-1]:
            return False
    
    # If none of the above conditions are met, the value is valid
    return True

def update_grid(grid, value):
    # Create a new grid with the updated value
    new_grid = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == j:
                new_grid[i][j] = value
            else:
                new_grid[i][j] = grid[i][j]
    
    # Return the new grid
    return new_grid

