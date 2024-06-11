def max_fill(grid, capacity):
    import math
    
    # TODO: Write your code here
    if capacity == 0:
        return 0
    if capacity == 1:
        return sum(sum(row) for row in grid)
    max_row = max(sum(row) for row in grid)
    if max_row <= capacity:
        return max_row
    return math.ceil(max_row / capacity) * len(grid)

