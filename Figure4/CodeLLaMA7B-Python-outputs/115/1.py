def max_fill(grid, capacity):
    import math
    
    # Find the maximum number of wells that can be filled
    # using the given capacity
    max_fill = 0
    for row in grid:
        max_fill += sum(row)
    # If the maximum number of wells that can be filled
    # using the given capacity is less than or equal to 0,
    # then we can't use the buckets to empty the wells
    if max_fill <= 0:
        return 0
    # If the maximum number of wells that can be filled
    # using the given capacity is greater than the capacity,
    # then we can't use the buckets to empty the wells
    if max_fill > capacity:
        return -1
    # If the maximum number of wells that can be filled
    # using the given capacity is equal to the capacity,
    # then we can use the buckets to empty the wells
    if max_fill == capacity:
        return 1
    # If the maximum number of wells that can be filled
    # using the given capacity is less than the capacity,
    # then we can use the buckets to empty the wells
    if max_fill < capacity:
        return math.ceil(max_fill / capacity)


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