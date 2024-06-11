def minPath(grid, k):
    
    # Your code here
    if not grid:
        return []
    if k == 1:
        return grid[0]
    if k == 2:
        return min(grid[0], grid[1])
    if k == 3:
        return min(min(grid[0], grid[1]), grid[2])
    if k == 4:
        return min(min(min(grid[0], grid[1]), grid[2]), grid[3])
    if k == 5:
        return min(min(min(min(grid[0], grid[1]), grid[2]), grid[3]), grid[4])
    if k == 6:
        return min(min(min(min(min(grid[0], grid[1]), grid[2]), grid[3]), grid[4]), grid[5])
    if k == 7:
        return min(min(min(min(min(min(grid[0], grid[1]), grid[2]), grid[3]), grid[4]), grid[5]), grid[6])
    if k == 8:
        return min(min(min(min(min(min(min(grid[0], grid[1]), grid[2]), grid[3]), grid[4]), grid[5]), grid[6]), grid[7])
    if k == 9:
        return min(min(min(min(min(min(min(min(grid[0], grid[1]), grid[2]), grid[3]), grid[4]), grid[5]), grid[6]), grid[7]), grid[8])
    return []

if __name__ == '__main__':
    grid = [[1,2,3], [4,5,6], [7,8,9]]
    k = 3
    print(minPath(grid, k))