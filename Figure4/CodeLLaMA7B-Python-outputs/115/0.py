def max_fill(grid, capacity):
    import math
    
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # n = number of wells
    n = len(grid)
    if n == 0:
        return 0

    # find the number of wells with water
    n_water = 0
    for row in grid:
        n_water += row.count(1)

    # if there is no water, return 0
    if n_water == 0:
        return 0

    # find the number of buckets
    n_buckets = math.ceil(n_water / capacity)

    # find the number of times we need to lower the buckets
    n_lower = 0
    for row in grid:
        # count the number of water units in the row
        n_water = 0
        for col in row:
            if col == 1:
                n_water += 1
        # if we have enough water, we don't need to lower the buckets
        if n_water >= capacity:
            continue
        # otherwise, we need to lower the buckets
        n_lower += n_buckets - n_water // capacity

    return n_lower


print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))
print(max_fill([[0,0,0], [0,0,0]], 5))
