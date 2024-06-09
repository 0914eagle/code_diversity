
def solve(grid):
    n, m = len(grid), len(grid[0])
    stars = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '*':
                stars.append((i, j))
    # Check if the grid is valid
    if len(stars) > n * m:
        return "-1"
    # Sort the stars by size in descending order
    stars.sort(key=lambda x: x[2], reverse=True)
    # Create a set to keep track of the used stars
    used_stars = set()
    # Loop through the stars and draw them
    for i, j, size in stars:
        if (i, j) in used_stars:
            continue
        # Draw the star
        draw_star(grid, i, j, size)
        # Mark the star as used
        used_stars.add((i, j))
    return "".join(["".join(row) for row in grid])

def draw_star(grid, i, j, size):
    n, m = len(grid), len(grid[0])
    # Draw the rays of the star
    for k in range(size):
        # Draw the left ray
        for l in range(k+1):
            if 0 <= i-k-l < n and 0 <= j-k-l < m and grid[i-k-l][j-k-l] == '.':
                grid[i-k-l][j-k-l] = '*'
        # Draw the right ray
        for l in range(k+1):
            if 0 <= i-k-l < n and 0 <= j+k+l < m and grid[i-k-l][j+k+l] == '.':
                grid[i-k-l][j+k+l] = '*'
        # Draw the top ray
        for l in range(k+1):
            if 0 <= i-k-l < n and 0 <= j-k-l < m and grid[i-k-l][j-k-l] == '.':
                grid[i-k-l][j-k-l] = '*'
        # Draw the bottom ray
        for l in range(k+1):
            if 0 <= i+k+l < n and 0 <= j-k-l < m and grid[i+k+l][j-k-l] == '.':
                grid[i+k+l][j-k-l] = '*'

