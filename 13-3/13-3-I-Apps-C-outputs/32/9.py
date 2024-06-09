
def solve(n, m, map):
    # Initialize a 2D array to store the number of cells needed to reach each cell from each state
    dp = [[0] * m for _ in range(n)]

    # Initialize a 2D array to store the number of cells needed to reach each cell from each state, considering the road built in that cell
    dp_road = [[0] * m for _ in range(n)]

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

    # Loop through each cell in the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable and the road is built in it, update the number of cells needed to reach it from each state
            if map[i][j] != '#' and dp[i][j] != 0:
                for k in range(3):
                    if map[i][j] == str(k + 1):
                        dp_road[i][j] = 0
                    else:
                        dp_road[i][j] = 1 + min(dp_road[i - 1][j], dp_road[i][j - 1], dp_road[i + 1][j], dp_road[i][j + 1])

    # Find the minimum number of cells needed to reach any cell of any state from any cell of any other state
    min_cells = float('inf')
    for i in range(n):
        for j in range(m):
            for k in range(3):
                if map[i][j] == str(k + 1):
                    min_cells = min(min_cells, dp_road[i][j])

    # If it is not possible to reach any cell of any state from any cell of any other state, return -1
    if min_cells == float('inf'):
        return -1

    # Otherwise, return the minimum number of cells needed to reach any cell of any state from any cell of any other state
    return min_cells

