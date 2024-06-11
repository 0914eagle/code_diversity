def max_fill(grid, capacity):
    import math
    
    # 1. Find the number of buckets needed to fill each well
    # 2. Find the number of buckets needed to fill each row
    # 3. Find the number of buckets needed to fill the entire grid
    # 4. Return the maximum of the above three numbers
    # 5. If the maximum is greater than the capacity, return -1
    # 6. Else, return the maximum
    buckets_needed = []
    for row in grid:
        buckets_needed.append(math.ceil(sum(row)/capacity))
    buckets_needed_row = []
    for i in range(len(grid[0])):
        buckets_needed_row.append(math.ceil(sum([row[i] for row in grid])/capacity))
    buckets_needed_grid = math.ceil(sum([sum(row) for row in grid])/capacity)
    return max(max(buckets_needed), max(buckets_needed_row), buckets_needed_grid) if max(buckets_needed) <= capacity and max(buckets_needed_row) <= capacity and buckets_needed_grid <= capacity else -1

