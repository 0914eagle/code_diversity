
def draw_grid(grid):
    # Initialize variables
    n, m = len(grid), len(grid[0])
    stars = []
    visited = [[False] * m for _ in range(n)]
    
    # Iterate through the grid
    for i in range(n):
        for j in range(m):
            # If the current cell is a star, add it to the list of stars
            if grid[i][j] == '*':
                stars.append((i, j))
                visited[i][j] = True
                
                # Check if the star is valid (i.e., it is not overlapping with any other star)
                for star in stars:
                    if i == star[0] and j == star[1]:
                        continue
                    if abs(i - star[0]) + abs(j - star[1]) <= star[2]:
                        return -1
    
    # If all stars are valid, return the list of stars
    return stars

