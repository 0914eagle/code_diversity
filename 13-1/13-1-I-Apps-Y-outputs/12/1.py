
def draw_grid(grid):
    # Initialize variables
    n, m = len(grid), len(grid[0])
    stars = []
    visited = [[False] * m for _ in range(n)]

    # Iterate over the grid
    for i in range(n):
        for j in range(m):
            # If the current cell is a star, add it to the list of stars
            if grid[i][j] == "*":
                stars.append((i, j))
                visited[i][j] = True

    # Check if the grid is valid
    if len(stars) > n * m:
        return -1

    # Draw the grid using the stars
    for i, j in stars:
        # Check if the star is completely inside the grid
        if i < 0 or i >= n or j < 0 or j >= m:
            return -1

        # Check if the star overlaps with any other star
        for k, l in stars:
            if i == k and j == l:
                continue
            if abs(i - k) + abs(j - l) <= 1:
                return -1

        # Mark the cell as visited
        visited[i][j] = True

    # Check if all cells are visited
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                return -1

    # Return the number of stars and their positions
    return len(stars), stars

