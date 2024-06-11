def minPath(grid, k):
    
    if not grid or not grid[0]:
        return []
    if k == 1:
        return grid[0]
    if k == 2:
        return min(grid[0], key=lambda x: x[0])
    if k == 3:
        return min(grid[0], key=lambda x: x[0]) + min(grid[1], key=lambda x: x[0])
    if k == 4:
        return min(grid[0], key=lambda x: x[0]) + min(grid[1], key=lambda x: x[0]) + min(grid[2], key=lambda x: x[0])
    if k == 5:
        return min(grid[0], key=lambda x: x[0]) + min(grid[1], key=lambda x: x[0]) + min(grid[2], key=lambda x: x[0]) + min(grid[3], key=lambda x: x[0])
    if k == 6:
        return min(grid[0], key=lambda x: x[0]) + min(grid[1], key=lambda x: x[0]) + min(grid[2], key=lambda x: x[0]) + min(grid[3], key=lambda x: x[0]) + min(grid[4], key=lambda x: x[0])
    if k == 7:
        return min(grid[0], key=lambda x: x[0]) + min(grid[1], key=lambda x: x[0]) + min(grid[2], key=lambda x: x[0]) + min(grid[3], key=lambda x: x[0]) + min(grid[4], key=lambda x: x[0]) + min(grid[5], key=lambda x: x[0])
    if k == 8:
        return min(grid[0], key=lambda x: x[0]) + min(grid[1], key=lambda x: x[0]) + min(grid[2], key=lambda x: x[0]) + min(grid[3], key=lambda x: x[0]) + min(grid[4], key=lambda x: x[0]) + min(grid[5], key=lambda x: x[