
def solve(n, m, map):
    # Initialize a 2D array to store the minimum number of cells required to reach each cell from each state
    dp = [[[float('inf')] * 3 for _ in range(n)] for _ in range(m)]

    # Initialize the first row and column with the values from the map
    for i in range(n):
        for j in range(m):
            if map[i][j] != '#':
                dp[i][j][map[i][j] - 1] = 0

    # Fill the 2D array using the recurrence relation
    for i in range(n):
        for j in range(m):
            if map[i][j] != '#':
                for k in range(3):
                    if i > 0 and dp[i - 1][j][k] != float('inf'):
                        dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k] + 1)
                    if j > 0 and dp[i][j - 1][k] != float('inf'):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][j - 1][k] + 1)

    # Find the minimum number of cells required to reach any cell from any state
    min_cells = float('inf')
    for i in range(n):
        for j in range(m):
            if map[i][j] != '#':
                min_cells = min(min_cells, dp[i][j][0] + dp[i][j][1] + dp[i][j][2])

    return -1 if min_cells == float('inf') else min_cells

