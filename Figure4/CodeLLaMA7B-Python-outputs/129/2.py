def minPath(grid, k):
    
    n = len(grid)
    m = len(grid[0])
    if k > n*m:
        return []
    if k == 0:
        return []
    if k == 1:
        return [min(grid[0])]
    if k == 2:
        return [min(grid[0]), min(grid[1])]
    if k == n*m:
        return [grid[i][j] for i in range(n) for j in range(m)]

    # 1. Find the kth smallest element in the grid
    # 2. Find the path that goes through the kth smallest element
    # 3. Repeat 1 and 2 until k == 1
    # 4. Return the path

    # 1. Find the kth smallest element in the grid
    # 2. Find the path that goes through the kth smallest element
    # 3. Repeat 1 and 2 until k == 1
    # 4. Return the path

    # 1. Find the kth smallest element in the grid
    # 2. Find the path that goes through the kth smallest element
    # 3. Repeat 1 and 2 until k == 1
    # 4. Return the path

    # 1. Find the kth smallest element in the grid
    # 2. Find the path that goes through the kth smallest element
    # 3. Repeat 1 and 2 until k == 1
    # 4. Return the path

    # 1. Find the kth smallest element in the grid
    # 2. Find the path that goes through the kth smallest element
    # 3. Repeat 1 and 2 until k == 1
    # 4. Return the path

    # 1. Find the kth smallest element in the grid
    # 2. Find the path that goes through the kth smallest element
    # 3. Repeat 1 and 2 until k == 1
    # 4. Return the path

    # 1. Find the kth smallest element in the grid
    # 2. Find the path that goes through the kth smallest