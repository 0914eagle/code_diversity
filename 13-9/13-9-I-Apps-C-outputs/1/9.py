
def solve(grid):
    n, m = len(grid), len(grid[0])
    north_cells, south_cells = set(), set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                south_cells.add((i, j))
            elif grid[i][j] == "#":
                north_cells.add((i, j))
    
    # Check if there is at least one south magnet in every row and every column
    for i in range(n):
        if not any(j in south_cells for j in range(m)):
            return -1
    for j in range(m):
        if not any(i in south_cells for i in range(n)):
            return -1
    
    # Check if it is possible to place north magnets such that they can move to all black cells
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "#" and (i, j) not in north_cells:
                return -1
    
    # Check if it is possible to place north magnets such that they can move to all white cells
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "." and (i, j) not in north_cells:
                return -1
    
    # Count the minimum number of north magnets required
    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "." and (i, j) not in north_cells:
                count += 1
    
    return count

