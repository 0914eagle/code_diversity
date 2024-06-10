
def move_left(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == 0:
                continue
            for k in range(j+1, 4):
                if grid[i][k] == 0:
                    grid[i][j] = 0
                    break
                if grid[i][j] == grid[i][k]:
                    grid[i][j] *= 2
                    grid[i][k] = 0
                    break
    return grid

def move_up(grid):
    for i in range(3):
        for j in range(4):
            if grid[i][j] == 0:
                continue
            for k in range(i+1, 4):
                if grid[k][j] == 0:
                    grid[i][j] = 0
                    break
                if grid[i][j] == grid[k][j]:
                    grid[i][j] *= 2
                    grid[k][j] = 0
                    break
    return grid

def move_right(grid):
    for i in range(4):
        for j in range(3, -1, -1):
            if grid[i][j] == 0:
                continue
            for k in range(j-1, -1, -1):
                if grid[i][k] == 0:
                    grid[i][j] = 0
                    break
                if grid[i][j] == grid[i][k]:
                    grid[i][j] *= 2
                    grid[i][k] = 0
                    break
    return grid

def move_down(grid):
    for i in range(3, -1, -1):
        for j in range(4):
            if grid[i][j] == 0:
                continue
            for k in range(i-1, -1, -1):
                if grid[k][j] == 0:
                    grid[i][j] = 0
                    break
                if grid[i][j] == grid[k][j]:
                    grid[i][j] *= 2
                    grid[k][j] = 0
                    break
    return grid

def solve(grid, direction):
    if direction == 0:
        return move_left(grid)
    elif direction == 1:
        return move_up(grid)
    elif direction == 2:
        return move_right(grid)
    else:
        return move_down(grid)

if __name__ == '__main__':
    grid = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        line = list(map(int, input().split()))
        for j in range(4):
            grid[i][j] = line[j]
    direction = int(input())
    solution = solve(grid, direction)
    for i in range(4):
        print(*solution[i])

