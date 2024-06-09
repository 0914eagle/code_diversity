
def solve(n, m, map):
    # Initialize a 2D array to store the number of cells needed to reach each cell from each state
    dp = [[0] * m for _ in range(n)]

    # Loop through each cell in the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable, update the number of cells needed to reach it from each state
            if map[i][j] != '#':
                for k in range(3):
                    if map[i][j] == str(k + 1):
                        dp[i][j] = 0
                    else:
                        dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i + 1][j], dp[i][j + 1])

    # Find the minimum number of cells needed to reach any cell from any state
    return min(min(row) for row in dp)

