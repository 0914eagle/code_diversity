def max_fill(grid, capacity):
    import math
    
    # Find the number of wells
    wells = []
    for row in grid:
        for col in row:
            if col == 1:
                wells.append(1)
    # Find the number of buckets
    buckets = len(grid)
    # Find the number of times we need to lower the buckets
    times = math.ceil(sum(wells) / capacity)
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