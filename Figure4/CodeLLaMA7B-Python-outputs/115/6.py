def max_fill(grid, capacity):
    import math
    
    # Find the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])
    # Find the number of buckets
    buckets = rows
    # Find the capacity of the buckets
    capacity = capacity
    # Find the number of wells
    wells = 0
    # Find the number of times the buckets have to be lowered
    times = 0
    # Find the number of wells
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                wells += 1
    # Find the number of times the buckets have to be lowered
    while wells > 0:
        # Find the number of wells that can be filled in a single iteration
        wells_filled = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    wells_filled += 1
        # Find the number of wells that can be filled in a single iteration
        wells_filled = min(wells_filled, buckets)
        # Find the number of wells that can be filled in a single iteration
        wells -= wells_filled
        # Find the number of times the buckets have to be lowered
        times += 1
    return times


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(max_fill(grid, capacity))
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(max_fill(grid, capacity))
    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))