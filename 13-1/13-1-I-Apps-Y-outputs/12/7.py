
def draw_grid(grid):
    # Initialize variables
    n, m = len(grid), len(grid[0])
    stars = []
    visited = [[False] * m for _ in range(n)]
    
    # Iterate through the grid
    for i in range(n):
        for j in range(m):
            # If the current cell is a star, mark it as visited and add it to the list of stars
            if grid[i][j] == '*':
                visited[i][j] = True
                stars.append((i, j))
    
    # If there are no stars in the grid, return -1
    if not stars:
        return -1
    
    # Initialize the number of stars needed to draw the grid
    k = 0
    
    # Iterate through the stars
    for i, j in stars:
        # If the current star is not visited, mark it as visited and add it to the list of stars needed to draw the grid
        if not visited[i][j]:
            visited[i][j] = True
            k += 1
    
    # If the number of stars needed to draw the grid is greater than the number of stars in the grid, return -1
    if k > len(stars):
        return -1
    
    # Return the list of stars needed to draw the grid
    return [(i, j, 1) for i, j in stars if not visited[i][j]]

