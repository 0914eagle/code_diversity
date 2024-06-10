
def get_input():
    grid = []
    for i in range(4):
        grid.append(list(map(int, input().split())))
    direction = int(input())
    return grid, direction

def move(grid, direction):
    if direction == 0:
        return move_left(grid)
    elif direction == 1:
        return move_up(grid)
    elif direction == 2:
        return move_right(grid)
    else:
        return move_down(grid)

def move_left(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                for k in range(j, -1, -1):
                    if grid[i][k] == 0:
                        new_grid[i][k] = grid[i][j]
                        break
                    elif grid[i][k] == grid[i][j]:
                        new_grid[i][k] = grid[i][j] * 2
                        break
                    else:
                        new_grid[i][k] = grid[i][j]
                        break
    return new_grid

def move_up(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 0:
                for k in range(i, -1, -1):
                    if grid[k][j] == 0:
                        new_grid[k][j] = grid[i][j]
                        break
                    elif grid[k][j] == grid[i][j]:
                        new_grid[k][j] = grid[i][j] * 2
                        break
                    else:
                        new_grid[k][j] = grid[i][j]
                        break
    return new_grid

def move_right(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                for k in range(j+1, 4):
                    if grid[i][k] == 0:
                        new_grid[i][k] = grid[i][j]
                        break
                    elif grid[i][k] == grid[i][j]:
                        new_grid[i][k] = grid[i][j] * 2
                        break
                    else:
                        new_grid[i][k] = grid[i][j]
                        break
    return new_grid

def move_down(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    for i in range(3, -1, -1):
        for j in range(4):
            if grid[i][j] != 0:
                for k in range(i+1, 4):
                    if grid[k][j] == 0:
                        new_grid[k][j] = grid[i][j]
                        break
                    elif grid[k][j] == grid[i][j]:
                        new_grid[k][j] = grid[i][j] * 2
                        break
                    else:
                        new_grid[k][j] = grid[i][j]
                        break
    return new_grid

def print_grid(grid):
    for row in grid:
        print(*row)

if __name__ == '__main__':
    grid, direction = get_input()
    new_grid = move(grid, direction)
    print_grid(new_grid)

