def minPath(grid, k):
    
    # initialize the grid
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            grid[i][j] = (grid[i][j], i, j)

    # initialize the priority queue
    pq = []
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                pq.append(grid[i][j])
            elif i == 0:
                pq.append(grid[i][j] + (m * grid[i][j - 1],))
            elif j == 0:
                pq.append(grid[i][j] + (grid[i - 1][j],))
            else:
                pq.append(grid[i][j] + (min(grid[i - 1][j], grid[i][j - 1]),))

    # initialize the visited set
    visited = set()
    visited.add((0, 0))

    # initialize the result
    result = []

    # initialize the counter
    count = 0

    # initialize the k
    k = k - 1

    # initialize the current position
    i = 0
    j = 0

    # initialize the previous position
    prev_i = 0
    prev_j = 0

    # initialize the direction
    direction = 0

    # initialize the min value
    min_value = 0

    # initialize the max value
    max_value = 0

    # initialize the min index
    min_index = 0

    # initialize the max index
    max_index = 0

    # initialize the min direction
    min_direction = 0

    # initialize the max direction
    max_direction = 0

    # initialize the min index direction
    min_index_direction = 0

    # initialize the max index direction
    max_index_direction = 0

    # initialize the min index value
    min_index_value = 0

    # initialize the max index value