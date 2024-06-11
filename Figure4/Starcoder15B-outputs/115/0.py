def max_fill(grid, capacity):
    import math
    
    # TODO: Write your code here
    # return -1

    # 1. Find the max number of buckets needed
    # 2. Find the max number of buckets needed to fill the wells
    # 3. Return the max of the two numbers

    # 1. Find the max number of buckets needed
    max_buckets = 0
    for row in grid:
        max_buckets += sum(row)

    # 2. Find the max number of buckets needed to fill the wells
    max_buckets_to_fill = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] == 1:
                max_buckets_to_fill += math.ceil(i / capacity)

    return max(max_buckets, max_buckets_to_fill)

