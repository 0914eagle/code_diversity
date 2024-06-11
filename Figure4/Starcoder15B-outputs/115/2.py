def max_fill(grid, capacity):
    import math
    
    if capacity == 0:
        return 0

    # get the number of rows and columns
    rows = len(grid)
    cols = len(grid[0])

    # get the number of wells
    wells = [0] * cols
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                wells[j] += 1

    # get the number of buckets
    buckets = [0] * cols
    for i in range(cols):
        buckets[i] = math.ceil(wells[i] / capacity)

    # get the number of times you need to lower the buckets
    return sum(buckets)


if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    bucket_capacity = 1
    print(max_fill(grid, bucket_capacity))

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    bucket_capacity = 2
    print(max_fill(grid, bucket_capacity))

    grid = [[0,0,0], [0,0,0]]
    bucket_capacity = 5
    print(max_fill(grid, bucket_capacity))

    grid = [[0,0,0], [0,0,0]]
    bucket_capacity = 0
    print(max_fill(grid, bucket_capacity))/leetcode/easy/202_happy_number.py
