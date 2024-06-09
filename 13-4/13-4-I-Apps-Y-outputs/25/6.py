
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
    # Create a set to store the indices of the stars that have been used
    used_stars = set()
    # Loop through the stars and draw them on the grid
    for i, j, size in stars:
        if (i, j) in used_stars:
            continue
        # Draw the star on the grid
        for x in range(i - size + 1, i + size):
            for y in range(j - size + 1, j + size):
                if 0 <= x < n and 0 <= y < m:
                    grid[x][y] = '*'
        used_stars.add((i, j))
    # Check if the grid is completely filled with stars
    if "." in "".join(["".join(row) for row in grid]):
        return "-1"
    # Return the number of stars used and their positions
    return str(len(stars)) + "\n" + "\n".join([" ".join(map(str, star)) for star in stars])

