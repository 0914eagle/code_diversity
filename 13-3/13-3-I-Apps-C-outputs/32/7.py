
def solve(n, m, map):
    # Initialize a 2D array to store the number of cells needed to reach each cell from each state
    dp = [[0] * m for _ in range(n)]

    # Initialize a 2D array to store the number of cells needed to reach each cell from each state, if a road is built in that cell
    dp_road = [[0] * m for _ in range(n)]

    # Loop through each cell in the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable and belongs to a state, update the number of cells needed to reach it from that state
            if map[i][j] != '#' and map[i][j] != '.':
                dp[i][j] = 1
                dp_road[i][j] = 1

    # Loop through each cell in the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable and belongs to a state, update the number of cells needed to reach it from all other states
            if map[i][j] != '#' and map[i][j] != '.':
                for k in range(n):
                    for l in range(m):
                        # If the current cell is not the same as the cell we are checking and it is passable, update the number of cells needed to reach it from the current state
                        if map[k][l] != '#' and map[k][l] != '.' and (k != i or l != j):
                            dp[i][j] = min(dp[i][j], dp[k][l] + 1)
                            dp_road[i][j] = min(dp_road[i][j], dp_road[k][l] + 1)

    # Loop through each cell in the map
    for i in range(n):
        for j in range(m):
            # If the current cell is passable and belongs to a state, update the number of cells needed to reach it from all other states, if a road is built in that cell
            if map[i][j] != '#' and map[i][j] != '.':
                for k in range(n):
                    for l in range(m):
                        # If the current cell is not the same as the cell we are checking and it is passable, update the number of cells needed to reach it from the current state
                        if map[k][l] != '#' and map[k][l] != '.' and (k != i or l != j):
                            dp_road[i][j] = min(dp_road[i][j], dp[k][l] + 1)

    # Find the minimum number of cells needed to reach any cell of any state from any cell of any other state
    min_cells = float('inf')
    for i in range(n):
        for j in range(m):
            # If the current cell is passable and belongs to a state, update the minimum number of cells needed to reach it from any cell of any other state
            if map[i][j] != '#' and map[i][j] != '.':
                min_cells = min(min_cells, dp_road[i][j])

    # If it is not possible to reach any cell of any state from any cell of any other state, return -1
    if min_cells == float('inf'):
        return -1

    # Otherwise, return the minimum number of cells needed to reach any cell of any state from any cell of any other state
    return min_cells

