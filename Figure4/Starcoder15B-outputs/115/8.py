def max_fill(grid, capacity):
    import math
    
    # TODO: Write your code here
    if capacity == 0:
        return 0
    if capacity == 1:
        return sum(sum(row) for row in grid)
    if capacity == 2:
        return sum(math.ceil(sum(row)/2) for row in grid)
    if capacity == 3:
        return sum(math.ceil(sum(row)/3) for row in grid)
    if capacity == 4:
        return sum(math.ceil(sum(row)/4) for row in grid)
    if capacity == 5:
        return sum(math.ceil(sum(row)/5) for row in grid)
    if capacity == 6:
        return sum(math.ceil(sum(row)/6) for row in grid)
    if capacity == 7:
        return sum(math.ceil(sum(row)/7) for row in grid)
    if capacity == 8:
        return sum(math.ceil(sum(row)/8) for row in grid)
    if capacity == 9:
        return sum(math.ceil(sum(row)/9) for row in grid)
    if capacity == 10:
        return sum(math.ceil(sum(row)/10) for row in grid)

