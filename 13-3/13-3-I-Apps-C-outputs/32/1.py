
def solve(n, m, map):
    # Initialize a 2D array to store the number of cells needed to reach each cell from each state
    dp = [[0] * m for _ in range(n)]

    # Initialize a 2D array to store the number of cells needed to reach each cell from each state
    dp = [[0] * m for _ in range(n)]

    # Loop through each row and column of the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable, set the number of cells needed to reach it from each state to 1
            if map[i][j] != '#':
                dp[i][j] = 1
            # If the current cell is not passable, set the number of cells needed to reach it from each state to 0
            else:
                dp[i][j] = 0

    # Loop through each row and column of the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable, continue to the next cell
            if map[i][j] == '#':
                continue
            # If the current cell is not passable, continue to the next cell
            if dp[i][j] == 0:
                continue
            # Loop through the four directions (up, down, left, and right)
            for k in range(4):
                # If the current cell is at the edge of the map, continue to the next cell
                if i + (k // 2) < 0 or i + (k // 2) >= n or j + (k % 2) < 0 or j + (k % 2) >= m:
                    continue
                # If the cell in the current direction is passable, set the number of cells needed to reach it from each state to the minimum of the current number and the number of cells needed to reach the current cell from each state plus 1
                if map[i + (k // 2)][j + (k % 2)] != '#':
                    dp[i + (k // 2)][j + (k % 2)] = min(dp[i + (k // 2)][j + (k % 2)], dp[i][j] + 1)

    # Initialize a variable to store the minimum number of cells needed to reach any cell from any state
    min_cells = float('inf')

    # Loop through each row and column of the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable, set the minimum number of cells needed to reach any cell from any state to the minimum of the current number and the number of cells needed to reach the current cell from each state
            if map[i][j] != '#':
                min_cells = min(min_cells, dp[i][j])

    # If the minimum number of cells needed to reach any cell from any state is infinite, return -1
    if min_cells == float('inf'):
        return -1
    # Otherwise, return the minimum number of cells needed to reach any cell from any state
    else:
        return min_cells

