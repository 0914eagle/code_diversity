def max_fill(grid, capacity):
    import math
    
    if capacity == 1:
        return sum(sum(row) for row in grid)
    else:
        return math.ceil(sum(sum(row) for row in grid) / capacity)

if __name__ == "__main__":
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    print(max_fill(grid, capacity))

    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    print(max_fill(grid, capacity))

    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    print(max_fill(grid, capacity))/leetcode/1001-1100/1001-1010/1004MaxConsecutiveOnesIII.py
