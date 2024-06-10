
def get_grid_size():
    return list(map(int, input().split()))

def get_grid():
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))
    return grid

def get_path_count(grid, x, y, k, visited):
    if x == n and y == m:
        return 1 if grid[x][y] ^ k == 0 else 0
    
    count = 0
    for i in range(x, n):
        for j in range(y, m):
            if grid[i][j] ^ k == 0 and (i, j) not in visited:
                visited.add((i, j))
                count += get_path_count(grid, i, j, k, visited)
                visited.remove((i, j))
    
    return count

n, m, k = get_grid_size()
grid = get_grid()
visited = set()
count = get_path_count(grid, 0, 0, k, visited)
print(count)

