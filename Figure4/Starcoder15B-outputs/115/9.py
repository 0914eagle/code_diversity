def max_fill(grid, capacity):
    import math
    
    # Write your code here
    if capacity == 0:
        return 0
    if capacity == 1:
        return sum([sum(row) for row in grid])
    # if capacity > 1:
    #     return sum([math.ceil(sum(row)/capacity) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in grid])
    #     # return sum([sum(row) for row in