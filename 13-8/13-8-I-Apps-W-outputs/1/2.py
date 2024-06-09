
def solve(grid):
    # Convert grid to a 2D array
    grid = [[int(cell) for cell in row] for row in grid]
    
    # Get the dimensions of the grid
    n = len(grid)
    m = len(grid[0])
    
    # Initialize a 2D array to store the levels of Zombie Contamination for each cell
    contamination = [[0] * m for _ in range(n)]
    
    # Loop through each cell in the grid
    for i in range(n):
        for j in range(m):
            # If the cell is inside the lair, add its level of Zombie Contamination to the contamination array
            if grid[i][j] != 0:
                contamination[i][j] = grid[i][j]
            # If the cell is on the border of the lair, add the level of Zombie Contamination of the adjacent cells to the contamination array
            else:
                contamination[i][j] = sum(grid[i][j:j+2]) + sum(grid[i+1][j:j+2])
    
    # Loop through each cell in the grid again
    for i in range(n):
        for j in range(m):
            # If the cell is inside the lair and has a level of Zombie Contamination that is not the same as the one reported in the input, return "No"
            if grid[i][j] != 0 and grid[i][j] != contamination[i][j]:
                return "No"
    
    # If all cells have the same level of Zombie Contamination as reported in the input, return "Yes"
    return "Yes"

