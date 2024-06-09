
def solve(n, m, t, op):
    # Initialize a 2D array to store the grid
    grid = [[0 for _ in range(n)] for _ in range(n)]
    
    # Fill in the grid with the given values
    for i in range(m):
        r, c = map(int, input().split())
        grid[r-1][c-1] = i+1
    
    # Use recursion to find the number of valid ways to fill in the section
    return count_ways(grid, t, op)

def count_ways(grid, t, op):
    # Base case: if the target value is 0, return 1
    if t == 0:
        return 1
    
    # Initialize the number of valid ways to 0
    ways = 0
    
    # Iterate over the possible values that can be placed in the current grid square
    for i in range(len(grid)):
        # If the current grid square is not empty, skip it
        if grid[i][i] != 0:
            continue
        
        # Place the current value in the grid square
        grid[i][i] = t
        
        # Recursively call the function to find the number of valid ways to fill in the rest of the section
        ways += count_ways(grid, t-1, op)
        
        # Backtrack and remove the current value from the grid square
        grid[i][i] = 0
    
    # Return the number of valid ways to fill in the section
    return ways

